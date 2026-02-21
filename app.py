import streamlit as st
import requests
import pandas as pd
import time
import socket
import hashlib
import random

# --- 1. CONFIGURATION & NEON THEME ---
st.set_page_config(page_title="ERORR_QUANTUM_CORE", page_icon="⚛️", layout="wide")

st.markdown("""
    <style>
    /* تحويل الواجهة بالكامل لنظام Cyber-Grid */
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(rgba(0, 255, 65, 0.02) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(0, 255, 65, 0.02) 1px, transparent 1px);
        background-size: 40px 40px;
    }
    
    /* القائمة الجانبية الاحترافية */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
        border-right: 1px solid #1a1a1a;
    }

    /* تأثير النيون للأدوات */
    .cyber-card {
        background: rgba(10, 10, 10, 0.8);
        border: 1px solid #00FF41;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.1);
        font-family: 'Courier New', monospace;
    }

    /* العناوين المتحركة */
    .glitch {
        color: #00FF41;
        font-size: 30px;
        font-weight: bold;
        text-transform: uppercase;
        text-shadow: 2px 2px #ff0000, -2px -2px #0000ff;
        animation: glitch 1s infinite;
    }

    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR: THE COMMAND CENTER ---
with st.sidebar:
    st.markdown("<div class='glitch'>ERORR AI</div>", unsafe_allow_html=True)
    st.markdown("<p style='color: #444;'>[ QUANTUM CYBERCORE v8.0 ]</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("📡 DATA MODULES")
    main_module = st.selectbox("SELECT OPERATION:", [
        "🌐 NETWORK WARFARE", 
        "🕵️ OSINT & FORENSICS", 
        "🔐 CRYPTO-LAB", 
        "🛠️ GENERAL EXPLOITS",
        "🛑 SHUTDOWN PROTOCOL"
    ])
    
    st.markdown("---")
    # محاكاة حالة النظام
    st.write("CPU LOAD:")
    st.progress(random.randint(10, 90))
    st.write("ENCRYPTION: **ACTIVE**")
    st.write("ANONYMITY: **HIGH**")

# --- 3. DYNAMIC CONTENT: THE TOOLS ---

if main_module == "🌐 NETWORK WARFARE":
    st.markdown("### \"ULTIMATE CYBER SANDBOX\"")
    st.write("[ Live attack map simulation and interception ]")
    
    # محاكاة رسم بياني للهجوم (نفس الصورة)
    chart_data = pd.DataFrame([random.random() for _ in range(20)], columns=['Attack Vector'])
    st.line_chart(chart_data)
    
    tab1, tab2, tab3 = st.tabs(["SERVER INFILTRATOR", "PORT DESTROYER", "DNS POISONER"])
    
    with tab1:
        cfx = st.text_input("TARGET HASH (CFX):")
        if st.button("RUN SCAN"):
            with st.status("Intercepting Data...") as status:
                time.sleep(1)
                st.write("💉 Injecting Packet Sniffer...")
                time.sleep(1)
                st.write("🔓 Bypassing Server Handshake...")
                status.update(label="RECON COMPLETE", state="complete")
            st.success("Target Intel Acquired. IP: 185.XXX.XX.XX")

elif main_module == "🕵️ OSINT & FORENSICS":
    st.markdown("### 🕵️ DIGITAL ENTITY TRACING")
    col1, col2 = st.columns(2)
    with col1:
        st.button("📸 IMAGE METADATA EXTRACTOR")
        st.button("👤 SOCIAL FOOTPRINT TRACER")
    with col2:
        st.button("🗺️ IP GEO-LOCATOR")
        st.button("📧 EMAIL BREACH CHECKER")

elif main_module == "🔐 CRYPTO-LAB":
    st.markdown("### 🔐 QUANTUM ENCRYPTION HUB")
    user_txt = st.text_area("Plaintext Input:")
    if st.button("EXECUTE ENCRYPTION"):
        c1, c2, c3 = st.columns(3)
        c1.code(f"MD5:\n{hashlib.md5(user_txt.encode()).hexdigest()}")
        c2.code(f"SHA-256:\n{hashlib.sha256(user_txt.encode()).hexdigest()}")
        c3.code(f"BASE64:\n...Encoded...")

elif main_module == "🛠️ GENERAL EXPLOITS":
    st.markdown("### 🛠️ UNIVERSAL HACKING TOOLS")
    tools = [
        "Wi-Fi Deauth Simulator", "SQL Injection Tester", 
        "XSS Payload Generator", "Password Strength Auditor",
        "Reverse Shell Generator", "MAC Address Changer",
        "Packet Crafter", "Subdomain Brute-Forcer",
        "Directory Buster", "SSL Certificate Analyzer"
    ]
    cols = st.columns(2)
    for i, tool in enumerate(tools):
        cols[i % 2].checkbox(f"✔️ {tool}")
    
    if st.button("ACTIVATE SELECTED TOOLS"):
        st.warning("Running batch operations... Stealth Mode Enabled.")

elif main_module == "🛑 SHUTDOWN PROTOCOL":
    if st.button("ERASE SYSTEM LOGS"):
        st.balloons()
        st.error("ALL SYSTEM LOGS PURGED. ERORR DISCONNECTED.")

# --- 4. FOOTER: DESIGNED BY ERORR ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: #333;'>© 2026 ERORR ULTIMATE CYBER SANDBOX | Authorized for Academic Use</div>", unsafe_allow_html=True)