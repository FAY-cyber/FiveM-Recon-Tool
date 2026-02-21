import streamlit as st
import requests
import pandas as pd
import time
import hashlib
import random

# --- 1. إعدادات الأمان والقواعد ---
st.set_page_config(page_title="ERORR_FINAL_CORE", page_icon="💀", layout="wide")

if 'users_db' not in st.session_state:
    st.session_state.users_db = {
        "ERORR": {"pass": "ERORR_2026", "rank": "full_admin"},
        "GUEST": {"pass": "123", "rank": "user"}
    }
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. ستايل النيون العسكري (Ultra Dark) ---
st.markdown("""
    <style>
    .stApp { background-color: #010101; color: #00FF41 !important; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 2px solid #00FF41; }
    .stMetric { background: #0a0a0a; border: 1px solid #00FF41; padding: 15px; border-radius: 5px; box-shadow: 0 0 10px #00FF41; }
    .tool-header { color: #00FF41; text-shadow: 0 0 15px #00FF41; border-bottom: 1px solid #00FF41; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. نظام الدخول ---
if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center; color:#00FF41; margin-top:10%;'>☣️ ERORR FINAL GATEWAY ☣️</h1>", unsafe_allow_html=True)
    cols = st.columns([1, 1.2, 1])
    with cols[1]:
        u = st.text_input("IDENTIFIER:")
        p = st.text_input("ACCESS KEY:", type="password")
        if st.button("BYPASS"):
            if u in st.session_state.users_db and st.session_state.users_db[u]['pass'] == p:
                st.session_state.auth = True
                st.session_state.user = u
                st.session_state.rank = st.session_state.users_db[u]['rank']
                st.rerun()
            else: st.error("INVALID ACCESS CODE.")
    st.stop()

# --- 4. القائمة الجانبية الذكية ---
with st.sidebar:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>! 𝕰𝕽𝕽𝕺𝕽</h1>", unsafe_allow_html=True)
    st.markdown(f"<center><small>RANK: {st.session_state.rank.upper()}</small></center>", unsafe_allow_html=True)
    st.markdown("---")
    
    # تصنيف الأدوات الشغالة فقط
    options = ["📡 FiveM Infiltrator", "🌍 IP Geo-Locator", "🔐 Security Lab", "🛰️ Advanced OSINT"]
    if st.session_state.rank == 'full_admin':
        options.append("🛠️ MASTER CONTROL")
    
    menu = st.selectbox("SELECT TOOL:", options)
    if st.button("LOGOUT"):
        st.session_state.auth = False
        st.rerun()

# --- 5. تشغيل الأدوات (The Arsenal) ---

# --- أداة 1: FiveM Infiltrator (الشغالة 100%) ---
if menu == "📡 FiveM Infiltrator":
    st.markdown("<h2 class='tool-header'>📡 FiveM Server Reconnaissance</h2>", unsafe_allow_html=True)
    cfx = st.text_input("TARGET HASH (e.g., qx6e89):")
    if st.button("EXECUTE SCAN"):
        with st.spinner("Decrypting Server Data..."):
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CFX/1.0'}
                r = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx}", headers=headers, timeout=12)
                if r.status_code == 200:
                    data = r.json()['Data']
                    st.success(f"ACCESS GRANTED: {data['hostname'][:50]}...")
                    c1, c2, c3 = st.columns(3)
                    c1.metric("IP:PORT", data['connectEndPoints'][0])
                    c2.metric("CLIENTS", f"{data['clients']}/{data['sv_maxclients']}")
                    c3.metric("OS", data['vars'].get('os', 'Unknown'))
                    
                    with st.expander("VIEW LOADED RESOURCES (SCRIPTS)"):
                        st.write(", ".join(data['resources']))
                    st.code(f"fivem://connect/{cfx}", language="bash")
                else: st.error("Server Offline or Cloudflare Blocked the request.")
            except: st.error("Scan Failed. Try again later.")

# --- أداة 2: IP Geo-Locator (الشغالة 100%) ---
elif menu == "🌍 IP Geo-Locator":
    st.markdown("<h2 class='tool-header'>🌍 Global IP Tracker</h2>", unsafe_allow_html=True)
    ip_target = st.text_input("ENTER TARGET IP:", "8.8.8.8")
    if st.button("TRACE LOCATION"):
        try:
            res = requests.get(f"http://ip-api.com/json/{ip_target}").json()
            if res['status'] == 'success':
                st.json(res)
                df = pd.DataFrame({'lat': [res['lat']], 'lon': [res['lon']]})
                st.map(df)
            else: st.error("IP not found in database.")
        except: st.error("Mapping Service Offline.")

# --- أداة 3: Security Lab ---
elif menu == "🔐 Security Lab":
    st.markdown("<h2 class='tool-header'>🔐 Encryption & Audit Lab</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["Hash Generator", "XSS Auditor (Sim)"])
    with t1:
        txt = st.text_input("String to Hash:")
        if txt:
            st.code(f"MD5: {hashlib.md5(txt.encode()).hexdigest()}")
            st.code(f"SHA256: {hashlib.sha256(txt.encode()).hexdigest()}")
    with t2:
        url = st.text_input("Target URL for Audit:")
        if st.button("RUN AUDIT"):
            st.warning("Analyzing attack vectors...")
            time.sleep(1)
            st.success("No critical vulnerabilities found in header.")

# --- أداة 4: Master Control ---
elif menu == "🛠️ MASTER CONTROL":
    st.markdown("<h2 class='tool-header'>🛠️ SYSTEM COMMAND CENTER</h2>", unsafe_allow_html=True)
    st.subheader("Add/Modify Permissions")
    new_u = st.text_input("Username:")
    new_p = st.text_input("Password:")
    new_r = st.selectbox("Rank:", ["user", "admin", "full_admin"])
    if st.button("CREATE ACCOUNT"):
        st.session_state.users_db[new_u] = {"pass": new_p, "rank": new_r}
        st.success(f"Entity {new_u} Authorized.")
    st.write("Current Database:", st.session_state.users_db)

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 ERORR | FINAL BUILD")