import streamlit as st

st.title("회원가입")
id = st.text_input("아이디")
pw = st.text_input("비밀번호", type='password')
pw_check = st.text_input("비밀번호 확인", type='password')
gender = st.radio("성별을 선택하세요", ['male','female'])
btn = st.button("회원가입")