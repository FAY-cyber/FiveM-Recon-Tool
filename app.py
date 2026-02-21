import streamlit as st
import requests
import pandas as pd
import socket
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="FiveM Cyber Auditor", page_icon="🛡️", layout="wide")

def get_geo_info(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        return res
    except: return None

def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip.split(':')[0], port))
        sock.close()
        return result == 0
    except: return False

# واجهة الموقع
st.title("🛡️ FiveM Server Security Auditor")
cfx_code = st.sidebar.text_input("Enter Target CFX:", "qx6e89")

if st.sidebar.button("Run Full Security Audit"):
    headers = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
    data = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx_code}", headers=headers).json().get("Data")
    
    if data:
        full_ip = data['connectEndPoints'][0]
        pure_ip = full_ip.split(':')[0]
        
        # --- قسم الخريطة والموقع ---
        st.header("📍 Server Geo-Location")
        geo = get_geo_info(pure_ip)
        if geo and geo['status'] == 'success':
            m = folium.Map(location=[geo['lat'], geo['lon']], zoom_start=10)
            folium.Marker([geo['lat'], geo['lon']], popup=geo['isp']).add_to(m)
            st_folium(m, height=300, width=1200)
            st.write(f"**Hosting:** {geo['isp']} | **City:** {geo['city']}, {geo['country']}")

        # --- قسم فحص الثغرات (Vulnerability Scanner) ---
        st.markdown("---")
        st.header("🔍 Security Vulnerability Report")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🛠️ Port Scanning")
            # فحص الـ RCON (أخطر ثغرة في فايف ام)
            is_rcon_open = check_port(pure_ip, 30120) # المنفذ الافتراضي
            if is_rcon_open:
                st.error("❌ CRITICAL: RCON Port (30120) is Open! Possible Remote Code Execution.")
            else:
                st.success("✅ RCON Port is filtered/closed.")

            # فحص قاعدة البيانات (MySQL/MariaDB)
            if check_port(pure_ip, 3306):
                st.warning("⚠️ WARNING: MySQL Port (3306) is Publicly Exposed. Risk of Brute Force.")

        with col2:
            st.subheader("📄 Configuration Leaks")
            # فحص ملفات الحساسة
            test_files = ["/players.json", "/info.json", "/dynamic.json"]
            for file in test_files:
                try:
                    r = requests.get(f"http://{full_ip}{file}", timeout=2)
                    if r.status_code == 200:
                        st.warning(f"⚠️ Information Leak: `{file}` is accessible to anyone.")
                except: pass

        # --- قسم تحليل الـ Artifacts (الإصدار) ---
        st.markdown("---")
        server_version = data['vars'].get('gamename', 'Unknown')
        st.subheader(f"⚙️ Artifacts Analysis: {data.get('server', 'N/A')}")
        if "linux" in data.get('server', '').lower():
            st.info("System running on Linux. Generally more secure against certain exploits.")
        else:
            st.warning("System running on Windows. Ensure latest security patches are applied.")

    else:
        st.error("Could not reach server.")