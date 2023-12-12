import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()


c1 = st.sidebar.radio('선의 색을 선택하시오',['red', 'green', 'blue'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오',['-', ':', '-.'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오',['o','^','s'])

a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)


x=[]
y=[]
y2=[]
for i in range(-29,30,3):
    x.append(i)
    y.append(ax** + b*x + c)
    y2.append(d/x)



plt.plot(x, y, y2, color = c1, linestyle = s1, maker = m1)

st.pyplot(fig)


import sys
sys.exit()