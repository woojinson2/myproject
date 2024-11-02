import streamlit as st
from PIL import Image

st.title("먹거리 주문")
st.text('라면')
st.checkbox('너구리  1500')
img=Image.open('ngr.png')
st.image(img)

st.checkbox('짜파게티')
img2=Image.open('Jpgt.png')
st.image(img2)

st.checkbox('불닭볶음면')
img3=Image.open('buldak.png')
st.image(img3)

st.checkbox('신라면')
img4=Image.open('srm.png')
st.image(img4)

st.checkbox('비빔면')
img5=Image.open('bbm.png')
st.image(img5)


st.text('밥')


st.checkbox('야채볶음밥')
img6=Image.open('bap.png')
st.image(img6)

st.checkbox('새우볶음밥')
img7=Image.open('sbap.png')
st.image(img7)

st.checkbox('참치마요덮밥')
img8=Image.open('ccbap.png')
st.image(img8)

st.checkbox('스팸마요덮밥')
img9=Image.open('spbap.png')
st.image(img9)

st.checkbox('김치볶음밥')
img10=Image.open('gcbap.png')
st.image(img10)


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
