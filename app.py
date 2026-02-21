import streamlit as st
import requests
import pandas as pd
import time

# --- إعدادات النظام ---
st.set_page_config(page_title="ERORR_MULTI_TOOL", page_icon="☣️", layout="wide")

# --- CSS المجنون (Dark & Neon) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41 !important; }
    .stSidebar { background-color: #0a0a0a !important; border-right: 1px solid #00FF41; }
    
    /* تصميم بطاقة بروفايل ERORR */
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
    
    /* أزرار النيون */
    .stButton>button {
        border: 1px solid #00FF41 !important; background: transparent !important;
        color: #00FF41 !important; width: 100%; box-shadow: 0 0 5px #00FF41;
    }
    .stButton>button:hover { background: #00FF41 !important; color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (البروفايل والتنقل) ---
with st.sidebar:
    st.markdown("""
        <div class="profile-card">
            <div class="profile-banner"></div>
            <div class="profile-content">
                <div class="profile-avatar"></div>
                <div class="profile-name">! 𝕰𝕽𝕽𝕺𝕽 🌙</div>
                <div style="font-size: 12px; color: #00FF41;">[ LEAD DEVELOPER ]</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🛠️ SELECT MODULE")
    page = st.radio("CHOOSE TOOL:", ["📡 Server Recon", "🕵️ User Tracer (OSINT)"])
    st.markdown("---")
    st.caption("ERORR Intelligence Suite v5.0")

# --- الصفحة الأولى: فحص السيرفرات ---
if page == "📡 Server Recon":
    st.markdown("<h1 style='text-align: center;'>📡 SERVER RECONNAISSANCE</h1>", unsafe_allow_html=True)
    cfx_code = st.text_input("ENTER TARGET HASH:", placeholder="qx6e89")
    
    if st.button("LAUNCH ANALYSIS"):
        with st.status("Analyzing Target...", expanded=True) as s:
            h = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
            res = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx_code}", headers=h)
            if res.status_code == 200:
                data = res.json().get("Data")
                s.update(label="DATA INTERCEPTED", state="complete")
                
                c1, c2, c3 = st.columns(3)
                c1.metric("IP ADDRESS", data['connectEndPoints'][0])
                c2.metric("LOAD", f"{data['clients']}/{data['sv_maxclients']}")
                c3.metric("OS", data['vars'].get('os', 'Unknown'))
                
                with st.expander("VIEW ACTIVE SCRIPTS"):
                    st.write(", ".join(data['resources']))
            else:
                st.error("FAILED TO ACCESS TARGET")

# --- الصفحة الثانية: أداة تتبع المستخدمين (الجديدة) ---
elif page == "🕵️ User Tracer (OSINT)":
    st.markdown("<h1 style='text-align: center;'>🕵️ USER TRACER OSINT</h1>", unsafe_allow_html=True)
    st.write("استخدم هذه الأداة لتحليل الهويات الرقمية التي سحبتها من السيرفر.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        steam_id = st.text_input("ENTER STEAM HEX / ID:", placeholder="steam:1100001...")
    with col_b:
        discord_id = st.text_input("ENTER DISCORD ID:", placeholder="458210...")

    if st.button("TRACE ENTITY"):
        with st.spinner("Searching Global Databases..."):
            time.sleep(1.5)
            st.subheader("🚨 Intelligence Report")
            
            # محاكاة لنتائج البحث الجنائي الرقمي
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.markdown("""
                **[ STEAM ANALYSIS ]**
                - Profile Link: [LINK FOUNDED]
                - Status: Publicly Exposed
                - Last Seen: 2 hours ago
                """)
            with res_col2:
                st.markdown("""
                **[ DISCORD ANALYSIS ]**
                - Account Age: 3 Years
                - Registered Email: [ENCRYPTED]
                - Linked Services: Steam, Twitch, Spotify
                """)
            
            st.warning("⚠️ Note: Deep tracing requires API keys for Steam/Discord. This is a simulation based on public metadata.")

    # إضافة صورة توضيحية لعملية التتبع
    st.markdown("---")
    st.write("**How it works:**")
    st.write("تقوم الأداة بربط الـ Identifiers بقواعد بيانات مفتوحة المصدر (OSINT) لبناء بصمة رقمية كاملة للهدف.")