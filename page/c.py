import streamlit as st
st.title("먹거리 주문")
st.text('라면')
st.checkbox('너구리  1500')
st.checkbox('짜파게티')
st.checkbox('불닭볶음면')
st.checkbox('신라면')
st.checkbox('비빔면')
st.text('밥')
st.checkbox('볶음밥')
st.checkbox('짜장밥')
st.checkbox('참치마요볶음밥')
st.checkbox('스팸마요볶음밥')
st.checkbox('김치볶음밥')
st.text('간식')
st.checkbox('핫도그')
st.checkbox('치즈스틱')
st.checkbox('감자튀김')
st.checkbox('고기만두')
st.checkbox('김치만두')
st.text('음료')
st.checkbox('커피')
st.checkbox('탄산음료')
st.checkbox('이온음료')
st.checkbox('카페인음료')
st.checkbox('따뜻한음료')

menu = st.selectbox("결제수단", ['카드', '현금','계좌이체','시간차감'])
