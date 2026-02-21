import streamlit as st
import requests
import json

# إعداد واجهة الموقع (Theme)
st.set_page_config(page_title="FiveM Info Tool", page_icon="🔍", layout="wide")

# تخصيص المظهر بـ CSS بسيط ليظهر بشكل "سبراني"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ff00; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

def fetch_fivem_data(cfx_code):
    url = f"https://servers-frontend.fivem.net/api/servers/single/{cfx_code}"
    # التظاهر بأننا مستخدم آيفون لتخطي حماية FiveM
    headers = {'user-agent': 'ios:2.65.0:488:14:iPhone13,3'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get("Data", {})
    except:
        return None
    return None

# الواجهة الرسومية
st.title("🌐 FiveM Server Intelligence Tool")
st.write("أداة استعلام عن سيرفرات فايف إم عبر الكود المختصر")

# منطقة الإدخال
cfx_input = st.text_input("أدخل كود السيرفر (مثل qx6e89):", placeholder="qx6e89")

if st.button("تحليل البيانات Fetch Data"):
    if cfx_input:
        with st.spinner('جاري جلب المعلومات من Cfx.re...'):
            server_data = fetch_fivem_data(cfx_input)
            
            if server_data:
                st.success("تم العثور على السيرفر بنجاح!")
                
                # عرض المعلومات الأساسية في كروت
                col1, col2, col3 = st.columns(3)
                col1.metric("IP Address", server_data.get("connectEndPoints", ["غير معروف"])[0])
                col2.metric("اللاعبين", f"{server_data.get('clients', 0)} / {server_data.get('sv_maxclients', 0)}")
                col3.metric("التقييم (Upvotes)", server_data.get("upvotePower", 0))

                st.markdown("---")
                
                # تفاصيل السيرفر
                with st.container():
                    st.subheader("📋 تفاصيل النظام")
                    st.write(f"**اسم السيرفر:** {server_data.get('hostname', 'N/A')}")
                    st.write(f"**صاحب السيرفر:** {server_data.get('ownerName', 'N/A')}")
                    st.write(f"**نظام التشغيل:** {server_data.get('vars', {}).get('os', 'N/A')}")
                
                # فحص الحماية (Anti-Cheat)
                st.subheader("🛡️ تحليل أمني")
                resources = str(server_data.get('resources', []))
                ac_list = ['shield', 'anticheat', 'eac', 'easy-anticheat', 'wave', 'phoenix']
                detected = [ac for ac in ac_list if ac in resources.lower()]
                
                if detected:
                    st.error(f"⚠️ تم كشف ملفات حماية محتملة: {', '.join(detected)}")
                else:
                    st.info("✅ لم يتم العثور على كلمات دلالية لبرامج حماية مشهورة.")

                # عرض البيانات الخام (لأغراض البحث العلمي)
                with st.expander("عرض البيانات الخام (JSON)"):
                    st.json(server_data)
            else:
                st.error("خطأ: الكود غير صحيح أو السيرفر مخفي.")
    else:
        st.warning("الرجاء إدخال الكود أولاً.")

st.sidebar.info("هذا الموقع صُمم كجزء من بحث في الأمن السيبراني لتحليل استغلال الـ APIs.")