import streamlit as st
import requests
import json

st.set_page_config(page_title="FiveM Intel & Recon", page_icon="🕵️", layout="wide")

# دالة سحب بيانات السيرفر
def fetch_server_data(cfx_code):
    url = f"https://servers-frontend.fivem.net/api/servers/single/{cfx_code}"
    headers = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.json().get("Data", {}) if response.status_code == 200 else None
    except: return None

# دالة سحب بيانات اللاعبين (بدون أدمن)
def fetch_players_data(ip):
    # نحاول الوصول للمنفذ الافتراضي الذي يعرض اللاعبين
    url = f"http://{ip}/players.json"
    try:
        response = requests.get(url, timeout=5)
        return response.json() if response.status_code == 200 else None
    except: return None

st.title("🕵️ FiveM Cyber Intelligence Tool")
cfx_input = st.text_input("Enter Server CFX Code:", placeholder="qx6e89")

if st.button("Start Reconnaissance"):
    data = fetch_server_data(cfx_input)
    if data:
        ip = data.get("connectEndPoints", ["Unknown"])[0]
        
        # --- القسم الأول: معلومات السيرفر ---
        st.header("🏢 Server Metadata")
        c1, c2, c3 = st.columns(3)
        c1.metric("Server IP", ip)
        c2.metric("Online Players", f"{data.get('clients')} / {data.get('sv_maxclients')}")
        c3.metric("Owner", data.get("ownerName"))

        # --- القسم الثاني: قسم اللاعبين (الجديد) ---
        st.markdown("---")
        st.header("👥 Players Intelligence (No Admin Required)")
        
        players = fetch_players_data(ip)
        
        if players:
            st.success(f"Successfully intercepted {len(players)} player profiles!")
            for p in players:
                with st.expander(f"👤 Player: {p['name']} (ID: {p['id']})"):
                    # عرض الهويات الرقمية (Discord, Steam, License)
                    st.write("**Digital Identifiers Found:**")
                    for identifier in p.get('identifiers', []):
                        if "discord" in identifier:
                            st.code(f"Discord ID: {identifier.replace('discord:', '')}", language="text")
                        elif "steam" in identifier:
                            st.write(f"🔗 [Steam Profile](https://steamcommunity.com/profiles/{int(identifier.replace('steam:', ''), 16)})")
                        else:
                            st.text(identifier)
                    st.info(f"Ping: {p.get('ping')}ms")
        else:
            st.error("⚠️ Player list is hidden or protected by a Firewall (Cfx Proxy).")
            st.write("In Cyber Security, this means the server uses a **Reverse Proxy** to hide player data.")

    else:
        st.error("Server not found!")