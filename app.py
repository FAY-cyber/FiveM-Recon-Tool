import streamlit as st
import requests
import pandas as pd
import time
import socket

# --- إعدادات النظام ---
st.set_page_config(page_title="ERORR_HACKER_SUITE", page_icon="☣️", layout="wide")

# --- CSS المجنون (الخاص بـ ERORR) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41 !important; }
    .stSidebar { background-color: #0a0a0a !important; border-right: 1px solid #00FF41; }
    .profile-card {
        background-color: #111111; border-radius: 12px; overflow: hidden;
        border: 1px solid #333; color: white !important; margin-bottom: 20px;
    }
    .profile-banner { height: 60px; background: linear-gradient(90deg, #00FF41, #000); }
    .profile-content { padding: 15px; position: relative; }
    .profile-avatar {
        width: 60px; height: 60px; border-radius: 50%; border: 3px solid #111;
        position: absolute; top: -30px; left: 15px;
        background-image: url('https://i.imgur.com/M6LpD8t.png'); background-size: cover;
    }
    .profile-name { margin-top: 30px; font-weight: bold; font-size: 18px; }
    .stButton>button {
        border: 1px solid #00FF41 !important; background: transparent !important;
        color: #00FF41 !important; width: 100%; box-shadow: 0 0 5px #00FF41;
    }
    .stButton>button:hover { background: #00FF41 !important; color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية ---
with st.sidebar:
    st.markdown("""
        <div class="profile-card">
            <div class="profile-banner"></div>
            <div class="profile-content">
                <div class="profile-avatar"></div>
                <div class="profile-name">! 𝕰𝕽𝕽𝕺𝕽 🌙</div>
                <div style="font-size: 12px; color: #00FF41;">[ ELITE DEVELOPER ]</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("CHOOSE WEAPON:", ["📡 Server Recon", "🕵️ User Tracer", "⚡ Port Scanner (NEW)"])

# --- الدالة المساعدة لفحص المنافذ ---
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            return s.connect_ex((ip, port)) == 0
    except: return False

# --- الصفحات ---

if page == "📡 Server Recon":
    st.title("📡 FiveM Infrastructure Recon")
    # ... (كود الصفحة الأولى السابق)
    cfx = st.text_input("ENTER CFX HASH:")
    if st.button("RUN SCAN"):
        st.write("Fetching Data...")

elif page == "🕵️ User Tracer":
    st.title("🕵️ Entity OSINT Tracer")
    # ... (كود الصفحة الثانية السابق)
    st.write("Tracing digital footprints...")

elif page == "⚡ Port Scanner (NEW)":
    st.title("⚡ Advanced Port & Service Scanner")
    st.write("هذه الأداة تحاكي عمل Nmap لاكتشاف الخدمات المفتوحة.")
    
    target_ip = st.text_input("ENTER TARGET IP (e.g. 1.1.1.1):", placeholder="127.0.0.1")
    
    ports_to_scan = {
        21: "FTP (File Transfer)",
        22: "SSH (Remote Access)",
        80: "HTTP (Web Server)",
        443: "HTTPS (Secure Web)",
        3306: "MySQL (Database)",
        30120: "FiveM Default Port"
    }

    if st.button("START NETWORK AUDIT"):
        st.info(f"Scanning {target_ip} for common vulnerabilities...")
        results = []
        progress = st.progress(0)
        
        for i, (port, desc) in enumerate(ports_to_scan.items()):
            is_open = scan_port(target_ip, port)
            status = "🔓 OPEN" if is_open else "🔒 CLOSED"
            results.append({"Port": port, "Service": desc, "Status": status})
            progress.progress((i + 1) / len(ports_to_scan))
            time.sleep(0.2)
            
        df = pd.DataFrame(results)
        st.table(df)

        # تحليل سبراني للنتائج
        st.subheader("☣️ Vulnerability Analysis")
        open_ports = [r['Port'] for r in results if "OPEN" in r['Status']]
        if open_ports:
            for p in open_ports:
                if p == 3306: st.error("⚠️ MySQL exposed! Risk: SQL Injection / Brute Force.")
                if p == 22: st.warning("⚠️ SSH open. Risk: Credential Stuffing.")
                if p == 30120: st.info("ℹ️ FiveM Port active. Target is a gaming server.")
        else:
            st.success("No common ports exposed. Target seems hardened.")

st.sidebar.markdown("---")
st.sidebar.caption("System Status: **Encrypted**")