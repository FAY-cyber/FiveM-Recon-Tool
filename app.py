import streamlit as st
import pandas as pd
import time
import hashlib
import random

# --- 1. إعدادات النظام ---
st.set_page_config(page_title="ERORR_SHADOW_NET", page_icon="☣️", layout="wide")

# --- 2. إدارة قواعد البيانات المؤقتة (DB Simulation) ---
if 'valid_keys' not in st.session_state:
    st.session_state.valid_keys = {"ERORR": "ERORR_2026", "MEMBER1": "123"}
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = [{"user": "ERORR", "msg": "Welcome to the shadow network.", "time": "00:00"}]
if 'chat_msg' not in st.session_state:
    st.session_state.chat_msg = []
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- 3. تصميم الواجهة (Quantum Dark UI) ---
st.markdown("""
    <style>
    .stApp { background-color: #020202; color: #00FF41 !important; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 2px solid #00FF41; }
    .neon-card { border: 1px solid #00FF41; padding: 15px; border-radius: 10px; background: rgba(0, 255, 65, 0.05); margin-bottom: 10px; }
    .admin-zone { border: 2px dashed #ff0000; padding: 20px; border-radius: 10px; background: rgba(255, 0, 0, 0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- 4. نظام الدخول ---
if 'authenticated' not in st.session_state or not st.session_state.authenticated:
    st.markdown("<h1 style='text-align:center; color:#00FF41;'>☣️ ERORR GATEWAY ☣️</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        u_name = st.text_input("ENTITY ID:")
        u_key = st.text_input("AUTH KEY:", type="password")
        if st.button("BYPASS"):
            if u_name in st.session_state.valid_keys and st.session_state.valid_keys[u_name] == u_key:
                st.session_state.authenticated = True
                st.session_state.current_user = u_name
                st.session_state.logs.append(f"Login: {u_name} - SUCCESS")
                st.rerun()
            else:
                st.error("ACCESS DENIED.")
    st.stop()

# --- 5. القائمة الجانبية المتقدمة ---
with st.sidebar:
    st.markdown(f"<h1 style='color:#00FF41; text-align:center;'>! 𝕰𝕽𝕽𝕺𝕽</h1>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.selectbox("📁 NAVIGATE:", [
        "🔥 FiveM Recon Tools",
        "🕵️ OSINT & Mapping",
        "💬 Covert Chat",
        "🏛️ Shadow Forum",
        "🛠️ ADMIN PANEL"
    ])
    st.markdown("---")
    if st.button("🔴 LOGOUT"):
        st.session_state.authenticated = False
        st.rerun()

# --- 6. الأقسام الجديدة ---

# --- أ: الشات المخفي ---
if menu == "💬 Covert Chat":
    st.title("💬 COVERT ENCRYPTED CHAT")
    st.markdown("<p style='color:red;'>[Messages are session-only and never stored on disk]</p>", unsafe_allow_html=True)
    
    chat_box = st.container(height=400)
    for m in st.session_state.chat_msg:
        chat_box.markdown(f"**[{m['user']}]:** {m['msg']}")
    
    with st.container():
        msg_input = st.text_input("Type message...", key="chat_input")
        if st.button("SEND"):
            if msg_input:
                st.session_state.chat_msg.append({"user": st.session_state.current_user, "msg": msg_input})
                st.rerun()

# --- ب: المنتدى السري ---
elif menu == "🏛️ Shadow Forum":
    st.title("🏛️ SHADOW FORUM")
    with st.expander("➕ Create New Post"):
        post_title = st.text_input("Topic:")
        post_content = st.text_area("Content:")
        if st.button("POST"):
            st.session_state.forum_posts.insert(0, {"user": st.session_state.current_user, "msg": f"{post_title}: {post_content}", "time": time.strftime("%H:%M")})
            st.rerun()
    
    for p in st.session_state.forum_posts:
        st.markdown(f"""
        <div class='neon-card'>
            <small style='color:grey;'>By {p['user']} at {p['time']}</small><br>
            {p['msg']}
        </div>
        """, unsafe_allow_html=True)

# --- ج: لوحة الإدمن المتطورة (لـ ERORR فقط) ---
elif menu == "🛠️ ADMIN PANEL":
    if st.session_state.current_user == "ERORR":
        st.markdown("<div class='admin-zone'>", unsafe_allow_html=True)
        st.title("🛠️ SYSTEM COMMANDER")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("User Management")
            target_user = st.selectbox("Select User:", list(st.session_state.valid_keys.keys()))
            if st.button("DELETE USER") and target_user != "ERORR":
                del st.session_state.valid_keys[target_user]
                st.warning(f"User {target_user} purged.")
                st.rerun()
            
            new_u = st.text_input("New User ID:")
            new_p = st.text_input("New Pass:")
            if st.button("ADD ACCESS KEY"):
                st.session_state.valid_keys[new_u] = new_p
                st.success("Key Activated.")
        
        with col2:
            st.subheader("System Logs")
            st.code("\n".join(st.session_state.logs[-10:]))
            if st.button("CLEAR ALL CHATS"):
                st.session_state.chat_msg = []
                st.success("Chat history wiped.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("INSUFFICIENT PRIVILEGES.")

# --- الأقسام القديمة (FiveM & OSINT) ---
elif menu == "🔥 FiveM Recon Tools":
    st.title("🔥 FiveM Infiltrator")
    # كود الـ Recon السابق يوضع هنا ليعمل 100%
    st.info("System Ready for Scanning.")

elif menu == "🕵️ OSINT & Mapping":
    st.title("🕵️ Geo-Intelligence")
    # كود الخرائط والـ IP يوضع هنا