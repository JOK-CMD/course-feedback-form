import streamlit as st

st.set_page_config(page_title="課程回饋表單", page_icon="📋")
st.title("📋 課程回饋表單")
st.write("請填寫以下資料，完成後按下送出。")
st.caption("本練習僅顯示填寫結果，資料不會保存到資料庫。")

st.sidebar.header("基本資料")
department = st.sidebar.selectbox("科系", ["資訊工程系", "電子工程系", "其他"])

with st.form("course_feedback"):
    name = st.text_input("姓名（必填）", max_chars=100)
    satisfaction = st.slider("課程滿意度", 1, 5, 3)
    feedback = st.text_area("意見回饋", placeholder="歡迎分享你的學習心得或建議。")
    submitted = st.form_submit_button("送出")

if submitted:
    if not name.strip():
        st.warning("請先輸入姓名")
    else:
        st.success("感謝您的回饋！")
        st.subheader("填寫結果")
        st.write("姓名：", name.strip())
        st.write("科系：", department)
        st.write("課程滿意度：", f"{satisfaction} / 5")
        st.write("意見回饋：", feedback.strip() or "未填寫")
