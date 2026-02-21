import streamlit as st
import requests
import pandas as pd
import time
import socket
import hashlib
import random

# --- إعدادات النظام ---
st.set_page_config(page_title="ERORR_ULTIMATE_CORE", page_icon="☣️", layout="wide")

# --- قاعدة البيانات والنظام ---
if 'valid_keys' not in st.session_state:
    st.session_state.valid_keys = ["ERORR_ADMIN", "GUEST_2026"]
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- CSS المجنون ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00FF41 !important; }
    .prank-red { color: #FF0000 !important; text-shadow: 0 0 10px #FF0000; font-weight: bold; font-size: 30px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- بوابة الدخول ---
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align:center; margin-top:10%; color:#00FF41;'>☣️ ERORR GATEWAY</h1>", unsafe_allow_html=True)
    cols = st.columns([1, 2, 1])
    with cols[1]:
        input_key = st.text_input("AUTHORIZATION KEY:", type="password")
        if st.button("BYPASS"):
            if input_key in st.session_state.valid_keys:
                st.session_state.authenticated = True
                st.rerun()
    st.stop()

# --- القائمة الجانبية ---
with st.sidebar:
    st.markdown("<h1 style='color:#00FF41;'>! 𝕰𝕽𝕽𝕺𝕽</h1>", unsafe_allow_html=True)
    category = st.selectbox("📁 CATEGORY:", [
        "🌐 Recon & OSINT", 
        "⚡ Network Warfare", 
        "🔐 Exploitation Lab", 
        "🤡 Cyber Pranks (NEW)",
        "🛠️ Admin Control"
    ])

# --- قسم الضحك والمقالب (Cyber Pranks) ---
if category == "🤡 Cyber Pranks (NEW)":
    st.title("🤡 CYBER PRANK TERMINAL")
    st.write("أدوات لإيهام الأصدقاء بأنك هكر أسطوري.")
    
    p1, p2, p3, p4 = st.tabs(["Ransomware Simulation", "Ghost Chat", "Data Leaker", "Satellite Uplink"])
    
    with p1:
        st.subheader("Fake Ransomware Attack")
        target_name = st.text_input("Enter Victim Name:")
        if st.button("ACTIVATE VIRUS"):
            container = st.empty()
            for i in range(3, 0, -1):
                container.warning(f"SYSTEM OVERRIDE IN {i}...")
                time.sleep(1)
            container.markdown("<div class='prank-red'>⚠️ YOUR SYSTEM IS INFECTED BY ERORR ⚠️<br>All files encrypted. Pay 5.0 BTC to recover.</div>", unsafe_allow_html=True)
            st.audio("https://www.soundjay.com/buttons/sounds/beep-01a.mp3") # صوت تنبيه بسيط

    with p2:
        st.subheader("Ghost Communication")
        if st.button("START GHOST PROTOCOL"):
            messages = [
                "I see you...", 
                "Nice shirt you're wearing today.", 
                "Why are you looking at the screen?", 
                "ERORR is everywhere."
            ]
            for msg in messages:
                st.write(f"**[STRANGER]:** {msg}")
                time.sleep(1.5)

    with p3:
        st.subheader("Fake Gallery Leaker")
        if st.button("LEAK IMAGES"):
            with st.status("Accessing Mobile Storage..."):
                time.sleep(1)
                st.write("Bypassing iCloud/Google Photos...")
                time.sleep(1)
                st.write("Extracting DCIM Folder...")
            
            st.warning("1,452 Images Found. Uploading to ERORR Cloud...")
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.05)
                progress.progress(i + 1)
            st.error("DATABASE LEAKED SUCCESSFULLY 💀")

    with p4:
        st.subheader("Satellite Uplink Simulation")
        if st.button("ESTABLISH UPLINK"):
            st.code("""
            Connecting to SpaceX Starlink Node #4412...
            [OK] Handshake established.
            [OK] Signal Strength: 98%
            [OK] Adjusting Orbital Position...
            Targeting Latitude: 24.7136 | Longitude: 46.6753
            Satellite Camera Live Feed Initialized.
            """, language="bash")
            st.info("Searching for visual signal...")

# --- الأقسام الأخرى (نفس الأكواد السابقة لضمان عمل الـ 20 أداة) ---
elif category == "🌐 Recon & OSINT":
    st.title("📡 GLOBAL RECON UNIT")
    # ... (تضع هنا الـ 5 أدوات الخاصة بالـ Recon)

elif category == "🛠️ Admin Control":
    st.title("🛠️ MASTER CONTROL")
    st.write(f"Current Access Keys: {st.session_state.valid_keys}")
    new_k = st.text_input("New Key:")
    if st.button("Add Key"):
        st.session_state.valid_keys.append(new_k)
        st.success("Key Added.")

st.sidebar.markdown("---")
st.sidebar.write("Total Tools: **24**")