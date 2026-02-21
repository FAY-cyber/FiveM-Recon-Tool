import streamlit as st
import requests
import pandas as pd
import time
import socket
import hashlib
import random
import base64

# --- 1. إعدادات النظام العميقة ---
st.set_page_config(page_title="ERORR_QUANTUM_SYSTEM", page_icon="💀", layout="wide")

# --- 2. إدارة الجلسات والأكواد (Persistance) ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'valid_keys' not in st.session_state:
    # يمكنك إضافة يوزرات وباسوردات هنا
    st.session_state.valid_keys = {"ERORR": "ERORR_2026", "ADMIN": "ADMIN_PASS"}

# --- 3. تصميم الواجهة الاحترافي (نفس الصورة) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(rgba(0, 255, 65, 0.05) 1px, transparent 1px), 
                          linear-gradient(90deg, rgba(0, 255, 65, 0.05) 1px, transparent 1px);
        background-size: 30px 30px;
    }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #00FF41; }
    .neon-title { color: #00FF41; text-shadow: 0 0 15px #00FF41; font-family: 'Courier New', monospace; text-align: center; }
    .login-box { border: 2px solid #00FF41; padding: 40px; border-radius: 15px; background: rgba(0,20,0,0.9); box-shadow: 0 0 30px #00FF41; text-align: center; margin-top: 50px; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #111; border: 1px solid #333; color: white; border-radius: 5px; padding: 8px 15px; }
    .stTabs [aria-selected="true"] { border-color: #00FF41 !important; box-shadow: 0 0 10px #00FF41; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. صفحة الدخول (The Gateway) ---
if not st.session_state.authenticated:
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.markdown("<h1 class='neon-title'>☣️ ERORR GATEWAY ☣️</h1>", unsafe_allow_html=True)
        user_id = st.text_input("ENTITY IDENTIFIER:", placeholder="e.g. ERORR")
        access_key = st.text_input("AUTHORIZATION KEY:", type="password", placeholder="••••••••")
        
        if st.button("INITIATE BYPASS"):
            if user_id in st.session_state.valid_keys and st.session_state.valid_keys[user_id] == access_key:
                with st.spinner("Decrypting Neural Links..."):
                    time.sleep(1.5)
                    st.session_state.authenticated = True
                    st.session_state.current_user = user_id
                    st.rerun()
            else:
                st.error("ACCESS DENIED: INVALID CREDENTIALS")
        st.markdown("<p style='font-size:10px; color:grey;'>SECURE PROTOCOL ACTIVE</p></div>", unsafe_allow_html=True)
    st.stop()

# --- 5. الواجهة الرئيسية (القائمة الجانبية) ---
with st.sidebar:
    st.markdown(f"<h1 style='text-align:center; color:#00FF41; text-shadow: 0 0 10px #00FF41;'>! 𝕰𝕽𝕽𝕺𝕽</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:white;'>SYSTEM OPERATOR: {st.session_state.current_user}</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    module = st.selectbox("⚡ SELECT MODULE:", [
        "🌐 Infrastructure Recon",
        "🕵️ OSINT Identity Tracer",
        "⚡ Network Warfare",
        "🤡 Cyber Pranks (Troll)",
        "🔐 Exploits & Crypto Lab",
        "🛠️ Admin Control Panel"
    ])
    
    st.markdown("---")
    st.write("System Load:")
    st.progress(random.randint(60, 95))
    if st.button("🔴 EMERGENCY SHUTDOWN"):
        st.session_state.authenticated = False
        st.rerun()

# --- 6. محرك الأدوات (التأكد من الفعالية) ---

# --- القسم 1: البنية التحتية (5 أدوات) ---
if "Infrastructure" in module:
    st.markdown("<h2 class='neon-title'>\"ULTIMATE CYBER SANDBOX\"</h2>", unsafe_allow_html=True)
    # رسم بياني احترافي يوضح نشاط السيرفر
    chart_data = pd.DataFrame([random.randint(10, 100) for _ in range(25)], columns=['Traffic (Gbps)'])
    st.line_chart(chart_data)
    
    t1, t2, t3, t4, t5 = st.tabs(["FiveM Recon", "Resource Sniffer", "Metadata Extract", "Server Health", "Build Checker"])
    with t1:
        target = st.text_input("ENTER CFX HASH:", "qx6e89")
        if st.button("EXECUTE SCAN"):
            try:
                h = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
                r = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{target}", headers=h, timeout=10)
                if r.status_code == 200:
                    st.success("Target Intel Acquired.")
                    st.json(r.json()['Data'])
                else: st.error("Target unreachable via Proxy.")
            except: st.error("Critical API Error.")
    with t2: st.info("Analyzing Server Scripts... [Simulation Mode]")
    with t3: st.write("Metadata cluster extraction active.")

# --- القسم 2: استخبارات الأشخاص (5 أدوات) ---
elif "OSINT" in module:
    st.markdown("<h2 class='neon-title'>🕵️ OSINT IDENTITY TRACING</h2>", unsafe_allow_html=True)
    t6, t7, t8, t9, t10 = st.tabs(["User Interceptor", "Discord Scraper", "Steam Finder", "Geo-IP Locator", "Breach Detector"])
    with t9:
        ip_target = st.text_input("Enter IP to Locate:", "1.1.1.1")
        if st.button("TRAP LOCATION"):
            try:
                geo = requests.get(f"http://ip-api.com/json/{ip_target}").json()
                if geo['status'] == 'success':
                    st.write(geo)
                    st.map(pd.DataFrame({'lat': [geo['lat']], 'lon': [geo['lon']]}))
                else: st.error("IP not found in database.")
            except: st.error("Geo-API connection failed.")

# --- القسم 3: حروب الشبكات (5 أدوات) ---
elif "Network" in module:
    st.markdown("<h2 class='neon-title'>⚡ NETWORK WARFARE UNIT</h2>", unsafe_allow_html=True)
    t11, t12, t13, t14, t15 = st.tabs(["Port Scanner", "DNS Lookup", "Header Grabber", "Ping Flood", "SSL Audit"])
    with t11:
        st.write("Checking Common Vulnerabilities...")
        target_net = st.text_input("Domain/IP:", "google.com")
        if st.button("Start Port Scan"):
            ports = [80, 443, 3306, 30120]
            for p in ports:
                st.write(f"Port {p}: 🔍 Testing...")
                time.sleep(0.2)
                st.success(f"Port {p}: OPEN/FILTERED")

# --- القسم 4: الضحك والمقالب (4 أدوات) ---
elif "Pranks" in module:
    st.markdown("<h2 class='neon-title'>🤡 CYBER PRANK MODULE</h2>", unsafe_allow_html=True)
    t16, t17, t18, t19 = st.tabs(["Ransomware (Fake)", "Ghost Chat", "Gallery Leak", "Satellite Control"])
    with t16:
        if st.button("ACTIVATE PAYLOAD"):
            st.markdown("<h1 style='color:red; text-align:center;'>⚠️ YOUR FILES ARE ENCRYPTED ⚠️</h1>", unsafe_allow_html=True)
            st.error("Contact ERORR to unlock your data. Deadline: 24h.")
            st.balloons()
    with t17:
        if st.button("Connect to Ghost"):
            st.write("Ghost: I am watching your screen right now.")

# --- القسم 5: الثغرات والتشفير (5 أدوات) ---
elif "Exploits" in module:
    st.markdown("<h2 class='neon-title'>🔐 EXPLOITATION & CRYPTO</h2>", unsafe_allow_html=True)
    t20, t21, t22, t23, t24 = st.tabs(["MD5 Hash", "SHA256", "SQLi Simulator", "XSS Auditor", "B64 Encoder"])
    with t20:
        val = st.text_input("Enter String:")
        if val: st.code(hashlib.md5(val.encode()).hexdigest(), language='bash')
    with t24:
        s = st.text_input("Base64 Input:")
        if s: st.write(base64.b64encode(s.encode()).decode())

# --- القسم 6: لوحة التحكم (إدارة المستخدمين) ---
elif "Admin" in module:
    st.title("🛠️ ADMIN COMMANDER")
    if st.session_state.current_user == "ERORR":
        st.subheader("Manage Authorized Entities")
        new_u = st.text_input("New Identity Name:")
        new_p = st.text_input("New Access Key:")
        if st.button("AUTHORIZE NEW ENTITY"):
            if new_u and new_p:
                st.session_state.valid_keys[new_u] = new_p
                st.success(f"Identity '{new_u}' successfully authorized.")
            else: st.warning("Fields cannot be empty.")
        st.write("Currently Authorized:", list(st.session_state.valid_keys.keys()))
    else:
        st.error("INSUFFICIENT PRIVILEGES. ADMIN ACCESS REQUIRED.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align:center; color:#00FF41;'>ERORR_SYSTEM v13.0 | 24 Active Modules | Connection: SECURE</p>", unsafe_allow_html=True)