import streamlit as st
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("동전을 던졌을 때 각 눈이 나올 확률")


def coin():
    global number, l
    a = b = 0
    l = []
    for i in range(0, number):
        if randint(0, 1) == 0:
            a += 1
        else:
            b += 1
        l.append([fraction(a, a + b).float, fraction(b, a + b).float])


number = st.slider(label="동전 던지기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=coin)

l = []
coin()

f = fraction(1, 2)

chart_data = df(l, columns=["앞면", "뒷면"])
st.plotly_chart(line(chart_data, f.float), use_container_width=True)

st.write(number, "번 동전을 던졌을 때 앞면이 나올 확률은 ", l[-1][0], "이고 뒷면이 나올 확률은", l[-1][1], "이다.")
st.write("이론상 확률은 앞면, 뒷면 모두 ", r"$\frac{1}{2}$", "=", f.float, "이다. ")
