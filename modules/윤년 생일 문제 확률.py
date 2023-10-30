import streamlit as st
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("n명이 있을 때 생일이 같은 쌍이 나올 확률(윤년)")


def birthday():
    global li, number, n
    c = 0
    li = []
    for i in range(1, number + 1):
        l = []
        for j in range(0, n):
            l.append(randint(1, 366))
        if find_same(l):
            c += 1
        li.append([fraction(c, i).float])


number = st.slider(label="그룹의 개수", min_value=10, max_value=10000, value=100, step=10, on_change=birthday)
n = st.slider(label="그룹 당 사람 수", min_value=2, max_value=366, value=5, step=1, on_change=birthday)

birthday()

f = fraction(1, 1) - fraction(factorial(366), 366 ** n * factorial(366 - n))

chart_data = df(li, columns=["생일이 같은 쌍이 나올 확률"])
st.plotly_chart(line(chart_data), use_container_width=True)

st.write(number, "개의 그룹에 그룹당 ", n, "명의 사람들이 있을 때 그룹 안에서 생일이 같은 사람이 생길 확률은 ", li[-1][0], "이다. ")
st.write("이론상 확률은 ", "$1 - { 366! \\over {366}^{%d} (366-%d)!}$" % (n, n),
         "≈", f.longdouble, "이다. ")
