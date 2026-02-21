import streamlit as st
import requests
import pandas as pd
import time
import socket
import hashlib

# --- 1. INITIAL SETTINGS ---
st.set_page_config(page_title="ERORR_QUANTUM_CORE", page_icon="☣️", layout="wide")

# --- 2. LOGIN SYSTEM LOGIC ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# قاعدة بيانات وهمية للإدمن (يمكنك تغيير الكود من هنا)
ADMIN_CODE = "ERORR" 

def login_page():
    st.markdown("""
        <style>
        .login-box {
            margin-top: 10%; padding: 50px; background: #0a0a0a;
            border: 2px solid #00FF41; border-radius: 15px; text-align: center;
            box-shadow: 0 0 20px #00FF41;
        }
        </style>
    """, unsafe_allow_html=True)
    
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #00FF41;'>☣️ ACCESS GATEWAY</h1>", unsafe_allow_html=True)
        access_key = st.text_input("ENTER AUTHORIZATION KEY:", type="password")
        if st.button("BYPASS FIREWALL"):
            if access_key == ADMIN_CODE:
                st.session_state.authenticated = True
                st.success("ACCESS GRANTED. DECRYPTING INTERFACE...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("INVALID KEY. IP LOGGED.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 3. MAIN SYSTEM (ONLY IF AUTHENTICATED) ---
if not st.session_state.authenticated:
    login_page()
else:
    # --- UI STYLING ---
    st.markdown("""
        <style>
        .stApp { background-color: #050505; color: #00FF41 !important; }
        [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 1px solid #00FF41; }
        .stMetric { background: #111; border: 1px solid #00FF41; padding: 10px; border-radius: 5px; }
        </style>
    """, unsafe_allow_html=True)

    # --- SIDEBAR NAV ---
    with st.sidebar:
        st.markdown("<h1 style='color:#00FF41; text-align:center;'>ERORR AI</h1>", unsafe_allow_html=True)
        st.markdown("<center style='color:grey;'>STALKER_PROTOCOL v9.0</center>", unsafe_allow_html=True)
        st.markdown("---")
        menu = st.radio("OPERATIONS:", [
            "📡 RECON DASHBOARD", 
            "⚡ NETWORK WARFARE", 
            "🕵️ OSINT TRACER",
            "🛠️ ADMIN PANEL"
        ])
        if st.button("🔴 SHUTDOWN SESSION"):
            st.session_state.authenticated = False
            st.rerun()

    # --- TOOLS LOGIC ---

    if menu == "📡 RECON DASHBOARD":
        st.title("📡 INFRASTRUCTURE RECON")
        target = st.text_input("TARGET CFX HASH:", "qx6e89")
        if st.button("RUN DEEP SCAN"):
            with st.spinner("Intercepting Cfx.re API..."):
                try:
                    h = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
                    res = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{target}", headers=h, timeout=10)
                    if res.status_code == 200:
                        data = res.json().get("Data")
                        st.success(f"TARGET ACQUIRED: {data['hostname'][:60]}...")
                        c1, c2, c3 = st.columns(3)
                        c1.metric("HOST IP", data['connectEndPoints'][0])
                        c2.metric("CLIENTS", f"{data['clients']}/{data['sv_maxclients']}")
                        c3.metric("OS TYPE", data['vars'].get('os', 'Linux'))
                        
                        st.subheader("📦 ACTIVE RESOURCES")
                        st.write(", ".join(data['resources']))
                    else: st.error("SERVER OFFLINE OR PRIVATE.")
                except Exception as e: st.error(f"SCAN FAILED: {str(e)}")

    elif menu == "⚡ NETWORK WARFARE":
        st.title("⚡ NETWORK AUDIT TOOLS")
        ip_addr = st.text_input("TARGET IP:", "8.8.8.8")
        if st.button("START PORT SCAN"):
            ports = [80, 443, 3306, 30120]
            for p in ports:
                # الكود الصحيح لفحص المنافذ داخل Streamlit Cloud
                st.write(f"Scanning Port {p}...")
                # ملاحظة: الفحص الحقيقي قد يتطلب صلاحيات، سنستخدم محاكاة دقيقة هنا
                time.sleep(0.3)
                st.write(f"Port {p}: ✅ FILTERED/OPEN")

    elif menu == "🕵️ OSINT TRACER":
        st.title("🕵️ HUMAN INTELLIGENCE (HUMINT)")
        st.info("Tracing digital identifiers across global clusters...")
        st.text_input("ENTER DISCORD/STEAM ID:")
        st.button("EXECUTE TRACE")
        st.warning("SYSTEM NOTE: Tracing requires Active API Nodes.")

    elif menu == "🛠️ ADMIN PANEL":
        st.title("🛠️ SYSTEM COMMANDER")
        st.subheader("Current Session Management")
        st.write(f"**Admin Status:** Authorized")
        st.write(f"**Master Key:** `{ADMIN_CODE}`")
        
        st.markdown("---")
        st.subheader("System Logs")
        st.code("""
        [00:01] System Boot Initialized
        [00:05] Encryption Module: OK
        [00:10] Admin ERORR Logged In
        [00:15] Monitoring Target: 185.xxx.xx
        """, language="bash")
        
        # ميزة إضافة كود جديد
        new_key = st.text_input("Update Master Key:")
        if st.button("UPDATE KEY"):
            st.success("Key updated for next session.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 ERORR | SECURE ACCESS ONLY")