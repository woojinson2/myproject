import streamlit as st
from PIL import Image
st.title("게임")
img=Image.open('dd.jpg')
st.image(img)
diablo_link=st.link_button('디아블로4',url="https://diablo4.blizzard.com/ko-kr/")