import streamlit as st
import requests
import pandas as pd
import time

# --- إعدادات الصفحة ---
st.set_page_config(page_title="ERORR_EXPLOIT_SYSTEM", page_icon="💀", layout="wide")

# --- حقن CSS لتحويل الواجهة وتصميم البروفايل ---
st.markdown("""
    <style>
    /* تنسيق الخلفية العامة */
    .stApp { background-color: #050505; color: #00FF41 !important; }

    /* تصميم بطاقة البروفايل (نفس الصورة) */
    .profile-card {
        background-color: #111111;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #333;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: white !important;
        margin-bottom: 20px;
    }
    .profile-banner {
        height: 80px;
        background-color: #1a1a1a;
        background-image: url('https://i.imgur.com/8Q9YQ8H.gif'); /* يمكنك وضع رابط خلفية متحركة هنا */
        background-size: cover;
    }
    .profile-content { padding: 15px; position: relative; }
    .profile-avatar {
        width: 80px; height: 80px;
        border-radius: 50%;
        border: 4px solid #111;
        position: absolute;
        top: -40px; left: 15px;
        background-image: url('https://i.imgur.com/M6LpD8t.png'); /* رابط صورتك الشخصية */
        background-size: cover;
    }
    .status-dot {
        width: 20px; height: 20px;
        background-color: #f1c40f; /* لون Idle نفس الصورة */
        border: 3px solid #111;
        border-radius: 50%;
        position: absolute;
        top: 15px; left: 75px;
    }
    .profile-info { margin-top: 45px; }
    .profile-name { font-size: 20px; font-weight: bold; color: white !important; }
    .profile-tag { color: #b9bbbe; font-size: 14px; margin-bottom: 10px; }
    .badges { display: flex; gap: 5px; margin-top: 5px; }
    .badge-icon { width: 18px; height: 18px; }
    
    .watching-box {
        background-color: #0c0c0c;
        border-radius: 8px;
        padding: 10px;
        margin-top: 15px;
        border: 1px solid #222;
    }
    .neon-btn {
        width: 100%; background: transparent;
        border: 1px solid #00FF41; color: #00FF41;
        padding: 8px; border-radius: 5px; cursor: pointer;
        margin-top: 10px; transition: 0.3s;
    }
    .neon-btn:hover { background: #00FF41; color: black; box-shadow: 0 0 15px #00FF41; }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (اسم المبرمج والبروفايل) ---
st.sidebar.markdown("<h2 style='text-align: center; color: #00FF41;'>DEVELOPER HUB</h2>", unsafe_allow_html=True)

# تصميم البروفايل المستوحى من صورتك
st.sidebar.markdown("""
    <div class="profile-card">
        <div class="profile-banner"></div>
        <div class="profile-content">
            <div class="profile-avatar"></div>
            <div class="status-dot"></div>
            <div class="profile-info">
                <div class="profile-name">! 𝕰𝕽𝕽𝕺𝕽 🌙</div>
                <div class="profile-tag">6h__ • Evil ⚡Evil</div>
                <div class="badges">
                    <img src="https://raw.githubusercontent.com/mezotv/discord-badges/main/assets/hypesquadbravery.svg" class="badge-icon">
                    <img src="https://raw.githubusercontent.com/mezotv/discord-badges/main/assets/discordnitro.svg" class="badge-icon">
                    <img src="https://raw.githubusercontent.com/mezotv/discord-badges/main/assets/boost1month.svg" class="badge-icon">
                </div>
                <div class="watching-box">
                    <div style="font-size: 12px; color: #b9bbbe;">Watching</div>
                    <div style="font-weight: bold; color: white;">My mind runs on code.</div>
                    <div style="font-size: 11px; color: #00FF41;">● 54:51</div>
                    <button class="neon-btn">ddd</button>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")
cfx_code = st.sidebar.text_input("TARGET CFX HASH:", "qx6e89")
scan_btn = st.sidebar.button("EXECUTE SYSTEM SCAN")

# --- الواجهة الرئيسية ---
st.markdown("<h1 style='text-align: center; text-shadow: 0 0 10px #00FF41;'>☣️ ERORR INTELLIGENCE TERMINAL ☣️</h1>", unsafe_allow_html=True)

if scan_btn:
    with st.status("ERORR Protocol Initiated...", expanded=True) as status:
        st.write("Intercepting Handshakes...")
        time.sleep(1)
        
        headers = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
        r = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx_code}", headers=headers)
        
        if r.status_code == 200:
            data = r.json().get("Data")
            status.update(label="SCAN COMPLETE", state="complete", expanded=False)
            
            # عرض النتائج بشكل احترافي
            st.subheader("📡 Server Interception Data")
            col1, col2, col3 = st.columns(3)
            col1.metric("IP ADDRESS", data['connectEndPoints'][0])
            col2.metric("LOAD", f"{data['clients']}/{data['sv_maxclients']}")
            col3.metric("OS", data['vars'].get('os', 'Unknown'))
            
            st.json(data['vars'])
        else:
            st.error("Target Connection Failed.")

st.sidebar.markdown("<br><center>System Created by <b>ERORR</b></center>", unsafe_allow_html=True)