import streamlit as st
import requests
import pandas as pd
import time
import hashlib
import random

# --- 1. CONFIG & SYSTEM ---
st.set_page_config(page_title="ERORR_V18_PREMIUM", page_icon="☣️", layout="wide")

if 'users_db' not in st.session_state:
    st.session_state.users_db = {
        "ERORR": {"pass": "ERORR_2026", "rank": "full_admin"},
        "GUEST": {"pass": "123", "rank": "user"}
    }
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = [{"user": "SYSTEM", "msg": "Shadow Forum Initialized.", "rank_req": "user"}]
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. CYBER UI STYLE ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41 !important; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #080808 !important; border-right: 2px solid #00FF41; }
    .neon-border { border: 1px solid #00FF41; padding: 20px; border-radius: 10px; background: rgba(0, 255, 65, 0.05); box-shadow: 0 0 15px #00FF41; }
    .forum-post { border-left: 4px solid #00FF41; padding: 10px; background: #111; margin-bottom: 10px; }
    .rank-badge { font-size: 10px; padding: 2px 5px; border-radius: 3px; background: #00FF41; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. GATEWAY ---
if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center; color:#00FF41; margin-top:10%; text-shadow: 0 0 20px #00FF41;'>☣️ ERORR CORE V18 ☣️</h1>", unsafe_allow_html=True)
    cols = st.columns([1, 1.2, 1])
    with cols[1]:
        u = st.text_input("IDENTIFIER:")
        p = st.text_input("ACCESS KEY:", type="password")
        if st.button("INITIATE BYPASS"):
            if u in st.session_state.users_db and st.session_state.users_db[u]['pass'] == p:
                st.session_state.auth = True
                st.session_state.user = u
                st.session_state.rank = st.session_state.users_db[u]['rank']
                st.rerun()
            else: st.error("ACCESS DENIED.")
    st.stop()

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>! 𝕰𝕽𝕽𝕺𝕽</h1>", unsafe_allow_html=True)
    st.markdown(f"<center><span class='rank-badge'>{st.session_state.rank.upper()}</span></center>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.selectbox("CORE MODULES:", ["🔥 FiveM Ultra-Recon", "📍 IP Precision Tracker", "🕵️ OSINT Deep Search", "🏛️ Shadow Forum", "🛠️ ADMIN PANEL"])
    if st.button("🔴 SHUTDOWN"):
        st.session_state.auth = False
        st.rerun()

# --- 5. MODULES EXECUTION ---

# --- A: FIVEM ULTRA-RECON ---
if menu == "🔥 FiveM Ultra-Recon":
    st.markdown("<h2 style='color:#00FF41;'>🔥 FIVEM ADVANCED INFILTRATOR</h2>", unsafe_allow_html=True)
    cfx_hash = st.text_input("ENTER SERVER HASH (CFX):", placeholder="qx6e89")
    if st.button("START DEEP SCAN"):
        with st.status("Intercepting Server Metadata...") as status:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CFX/1.0'}
                r = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx_hash}", headers=headers, timeout=10)
                if r.status_code == 200:
                    data = r.json()['Data']
                    status.update(label="SCAN COMPLETE", state="complete")
                    
                    st.markdown("<div class='neon-border'>", unsafe_allow_html=True)
                    col1, col2, col3 = st.columns(3)
                    col1.metric("HOST NAME", data['hostname'][:20])
                    col2.metric("IP ADDR", data['connectEndPoints'][0])
                    col3.metric("PLAYERS", f"{data['clients']}/{data['sv_maxclients']}")
                    
                    st.write("---")
                    st.subheader("📦 INFRASTRUCTURE (RESOURCES)")
                    st.info(", ".join(data['resources']))
                    
                    st.subheader("⚙️ SERVER VARIABLES")
                    st.json(data['vars'])
                    st.markdown("</div>", unsafe_allow_html=True)
                else: st.error("Server info protected or offline.")
            except: st.error("Connection Interrupted.")

# --- B: IP PRECISION TRACKER ---
elif menu == "📍 IP Precision Tracker":
    st.markdown("<h2 style='color:#00FF41;'>📍 IP GEOGRAPHICAL PRECISION</h2>", unsafe_allow_html=True)
    target_ip = st.text_input("TARGET IP:", "8.8.8.8")
    if st.button("START TRACKING"):
        try:
            res = requests.get(f"http://ip-api.com/json/{target_ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query").json()
            if res['status'] == 'success':
                st.markdown("<div class='neon-border'>", unsafe_allow_html=True)
                st.write(f"**ISP:** {res['isp']} | **City:** {res['city']} | **ZIP:** {res['zip']}")
                # الخريطة التفاعلية
                df = pd.DataFrame({'lat': [res['lat']], 'lon': [res['lon']]})
                st.map(df, zoom=12)
                st.markdown("</div>", unsafe_allow_html=True)
            else: st.error("IP Not Found.")
        except: st.error("Geo-Service Offline.")

# --- C: SHADOW FORUM (WITH RANK SYSTEM) ---
elif menu == "🏛️ Shadow Forum":
    st.title("🏛️ SHADOW FORUM")
    
    # نشر موضوع جديد
    with st.expander("➕ NEW LEAK"):
        t_title = st.text_input("Title:")
        t_msg = st.text_area("Content:")
        t_rank = st.selectbox("Required Rank to see:", ["user", "admin", "full_admin"])
        if st.button("POST TO NETWORK"):
            st.session_state.forum_posts.insert(0, {"user": st.session_state.user, "msg": f"[{t_title}] {t_msg}", "rank_req": t_rank})
            st.rerun()
            
    # عرض المواضيع حسب الرتبة
    st.write("---")
    for p in st.session_state.forum_posts:
        # منطق الرتب: هل رتبة المستخدم الحالية تسمح له برؤية البوست؟
        ranks_hierarchy = {"user": 0, "admin": 1, "full_admin": 2}
        user_level = ranks_hierarchy.get(st.session_state.rank, 0)
        req_level = ranks_hierarchy.get(p['rank_req'], 0)
        
        if user_level >= req_level:
            st.markdown(f"""
            <div class='forum-post'>
                <span class='rank-badge'>{p['rank_req'].upper()} REQ</span>
                <b>{p['user']}</b>: {p['msg']}
            </div>
            """, unsafe_allow_html=True)

# --- D: ADMIN PANEL ---
elif menu == "🛠️ ADMIN PANEL":
    if st.session_state.rank == "full_admin":
        st.title("🛠️ MASTER CONTROL PANEL")
        st.write("Current Authorized Entities:")
        st.write(st.session_state.users_db)
        
        new_id = st.text_input("New Entity ID:")
        new_pk = st.text_input("New Auth Key:")
        new_rk = st.selectbox("Assign Rank:", ["user", "admin", "full_admin"])
        if st.button("AUTHORIZE"):
            st.session_state.users_db[new_id] = {"pass": new_pk, "rank": new_rk}
            st.success("Entity Authorized Successfully.")
    else:
        st.error("INSUFFICIENT PRIVILEGES.")