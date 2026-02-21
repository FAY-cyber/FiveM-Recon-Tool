import streamlit as st
import requests
import pandas as pd
import socket
import folium
from streamlit_folium import st_folium

# إعداد الصفحة لتعمل بثبات
st.set_page_config(page_title="FiveM Cyber Recon", page_icon="🛡️", layout="wide")

# دالة فحص المنافذ بطريقة آمنة لا تسبب انهيار الكود
def safe_check_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5) # وقت قصير لعدم تعليق الموقع
            return s.connect_ex((ip, port)) == 0
    except:
        return False

st.title("🛡️ FiveM Server Security Dashboard")
st.sidebar.header("Control Panel")
cfx_code = st.sidebar.text_input("Target CFX Code:", "qx6e89")

if st.sidebar.button("Execute Deep Scan"):
    with st.spinner('Accessing Cfx.re API...'):
        headers = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
        try:
            r = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{cfx_code}", headers=headers)
            if r.status_code == 200:
                data = r.json().get("Data")
                full_ip = data['connectEndPoints'][0]
                pure_ip = full_ip.split(':')[0]

                # عرض المعلومات الأساسية
                st.success(f"Target Acquired: {data['hostname'][:50]}")
                
                tab1, tab2 = st.tabs(["🗺️ Geo-Location", "🔍 Vulnerabilities"])

                with tab1:
                    # جلب الموقع الجغرافي
                    geo = requests.get(f"http://ip-api.com/json/{pure_ip}").json()
                    if geo.get('status') == 'success':
                        m = folium.Map(location=[geo['lat'], geo['lon']], zoom_start=8)
                        folium.Marker([geo['lat'], geo['lon']], popup=geo['isp']).add_to(m)
                        st_folium(m, height=400, width=1000)
                    else:
                        st.warning("Could not resolve Geo-location (Proxy detected)")

                with tab2:
                    st.subheader("Critical Security Checks")
                    # فحص RCON
                    if safe_check_port(pure_ip, 30120):
                        st.error("🚨 CRITICAL: RCON port 30120 is EXPOSED!")
                    else:
                        st.info("✅ RCON port is secure (closed).")
                    
                    # فحص الملفات المسربة
                    with st.expander("Information Disclosure Check"):
                        for endpoint in ["/players.json", "/info.json"]:
                            check_url = f"http://{full_ip}{endpoint}"
                            try:
                                res = requests.get(check_url, timeout=2)
                                if res.status_code == 200:
                                    st.warning(f"⚠️ Leak Found: {endpoint} is public.")
                            except: pass

            else:
                st.error("Invalid CFX Code or API Rate Limit exceeded.")
        except Exception as e:
            st.error(f"Error during scan: {str(e)}")

st.sidebar.markdown("---")
st.sidebar.write("Developed for Cybersecurity Academic Research")