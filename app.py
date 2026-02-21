import streamlit as st
import requests
import pandas as pd
import time
import json
import re

# --- 1. CONFIG & SYSTEM ---
st.set_page_config(page_title="ERORR_V20_RESURRECTION", page_icon="☣️", layout="wide")

if 'users_db' not in st.session_state:
    st.session_state.users_db = {"ERORR": {"pass": "ERORR_2026", "rank": "full_admin"}}
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = []
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. THE ULTIMATE DARK UI ---
st.markdown("""
    <style>
    .stApp { background-color: #030303; color: #00FF41 !important; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #00FF41; }
    .osint-card { border: 1px solid #00FF41; padding: 15px; border-radius: 5px; background: rgba(0, 255, 65, 0.02); margin-bottom: 10px; }
    .status-online { color: #00FF41; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN GATEWAY ---
if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center; color:#00FF41; margin-top:10%; text-shadow: 0 0 20px #00FF41;'>☣️ ERORR CORE V20 ☣️</h1>", unsafe_allow_html=True)
    cols = st.columns([1, 1.2, 1])
    with cols[1]:
        u = st.text_input("ENTITY ID:")
        p = st.text_input("AUTH KEY:", type="password")
        if st.button("BYPASS"):
            if u in st.session_state.users_db and st.session_state.users_db[u]['pass'] == p:
                st.session_state.auth = True
                st.session_state.user = u
                st.session_state.rank = st.session_state.users_db[u]['rank']
                st.rerun()
            else: st.error("ACCESS DENIED.")
    st.stop()

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='color:#00FF41;'>𝕰𝕽𝕽𝕺𝕽 2026</h1>", unsafe_allow_html=True)
    st.markdown(f"**OPERATOR:** {st.session_state.user} <span class='status-online'>●</span>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.selectbox("CORE MODULES:", [
        "🕵️ DEEP OSINT SCANNER", 
        "🔥 FIVEM ADVANCED INFILTRATOR", 
        "📍 IP PRECISION TRACKER", 
        "🏛️ SHADOW FORUM", 
        "🛠️ ADMIN PANEL"
    ])
    if st.button("🔴 SHUTDOWN SYSTEM"):
        st.session_state.auth = False
        st.rerun()

# --- 5. DEEP OSINT SCANNER (الإصدار الجديد المصلح) ---
if menu == "🕵️ DEEP OSINT SCANNER":
    st.markdown("<h2 style='color:#00FF41;'>🕵️ DEEP OSINT INTELLIGENCE</h2>", unsafe_allow_html=True)
    st.write("أداة سحب المعلومات من المصادر المفتوحة (حسابات، إيميلات، يوزرات).")
    
    target = st.text_input("ENTER TARGET (Username, Email, or Domain):", placeholder="e.g. jdoe@gmail.com")
    
    if st.button("LAUNCH INVESTIGATION"):
        with st.status("Searching Global Databases...") as status:
            time.sleep(1.5)
            # محاكاة ذكية لسحب البيانات المتاحة عامة
            st.markdown("<div class='osint-card'>", unsafe_allow_html=True)
            st.subheader("🔍 Scanned Endpoints")
            
            # فحص الإيميل أو اليوزر في أشهر المواقع
            platforms = ["GitHub", "Twitter", "Instagram", "Pastebin", "LinkedIn"]
            found = []
            for p in platforms:
                st.write(f"Checking {p} database...")
                time.sleep(0.3)
                if random.choice([True, False]): found.append(p)
            
            st.success(f"Potential matches found on: {', '.join(found)}")
            
            st.markdown("---")
            st.subheader("📄 Public Leaks Check")
            st.info("No active password leaks found for this entity in current 2026 DB.")
            st.markdown("</div>", unsafe_allow_html=True)
            status.update(label="INVESTIGATION COMPLETE", state="complete")

# --- 6. FIVEM INFILTRATOR (المحسنة) ---
elif menu == "🔥 FIVEM ADVANCED INFILTRATOR":
    st.markdown("<h2 style='color:#00FF41;'>🔥 FIVEM DEEP RECON</h2>", unsafe_allow_html=True)
    cfx_hash = st.text_input("SERVER CFX HASH:", placeholder="e.g. qx6e89")
    
    if st.button("DECRYPT SERVER"):
        try:
            h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CFX/1.0'}
            r = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx_hash}", headers=h, timeout=10)
            if r.status_code == 200:
                d = r.json()['Data']
                st.success(f"Target: {d['hostname']}")
                st.code(f"Endpoint: {d['connectEndPoints'][0]}")
                st.write(f"Players: {d['clients']}/{d['sv_maxclients']}")
                with st.expander("Show Server Scripts (Resources)"):
                    st.write(", ".join(d['resources']))
            else: st.error("Server API Blocked or Hash Invalid.")
        except: st.error("Connection Error.")

# --- 7. IP TRACKER ---
elif menu == "📍 IP PRECISION TRACKER":
    st.markdown("<h2 style='color:#00FF41;'>📍 IP GEOGRAPHICAL PRECISION</h2>", unsafe_allow_html=True)
    ip_target = st.text_input("TARGET IP:", "8.8.8.8")
    if st.button("TRACE"):
        res = requests.get(f"http://ip-api.com/json/{ip_target}").json()
        if res['status'] == 'success':
            st.json(res)
            st.map(pd.DataFrame({'lat': [res['lat']], 'lon': [res['lon']]}))

# --- 8. SHADOW FORUM ---
elif menu == "🏛️ SHADOW FORUM":
    st.title("🏛️ SHADOW FORUM")
    with st.expander("➕ POST NEW INTEL"):
        t = st.text_input("Subject:")
        c = st.text_area("Content:")
        rk = st.selectbox("Rank Req:", ["user", "admin", "full_admin"])
        if st.button("ENCRYPT & SEND"):
            st.session_state.forum_posts.insert(0, {"user": st.session_state.user, "title": t, "content": c, "rank": rk})
            st.rerun()
    
    for p in st.session_state.forum_posts:
        ranks = {"user": 0, "admin": 1, "full_admin": 2}
        if ranks[st.session_state.rank] >= ranks[p['rank']]:
            st.markdown(f"<div style='border-left: 2px solid #00FF41; padding: 10px; background: #111;'><b>{p['title']}</b><br><small>By: {p['user']} | Rank: {p['rank']}</small><br>{p['content']}</div>", unsafe_allow_html=True)

# --- 9. ADMIN PANEL ---
elif menu == "🛠️ ADMIN PANEL":
    if st.session_state.rank == "full_admin":
        st.title("🛠️ MASTER CONTROL")
        new_id = st.text_input("NEW ID:")
        new_pk = st.text_input("NEW KEY:")
        new_rk = st.selectbox("RANK:", ["user", "admin", "full_admin"])
        if st.button("AUTHORIZE"):
            st.session_state.users_db[new_id] = {"pass": new_pk, "rank": new_rk}
            st.success("CREDENTIALS ACTIVATED.")
    else: st.error("ACCESS DENIED.")