import streamlit as st

st.title("파이콘 튜토리얼")
st.info("안녕하세요, 파이콘 튜토리얼 앱입니다.")

st.subheader("첫 번째 앱")
st.image("https://static.streamlit.io/examples/cat.jpg", caption="귀여운 고양이", use_container_width=True)
st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")




