import streamlit as st
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("n명이 있을 때 생일이 같은 쌍이 나올 확률(윤년)")


def birthday():
    global l, number, n
    c = 0
    l = []
    for i in range(1, number + 1):
        temp = []
        for j in range(0, n):
            temp.append(rand1(366))
        if find_same(temp):
            c += 1
        l.append([Fraction(c, i)])


mode = m()

if mode:
    number = st.slider(label="그룹의 개수", min_value=10, max_value=10000, value=100, step=10, on_change=birthday)

else:
    number = 1000000

n = st.slider(label="그룹 당 사람 수", min_value=2, max_value=366, value=5, step=1, on_change=birthday)

l = []
birthday()

f = Fraction(1, 1) - Fraction(factorial(366), 366 ** n * factorial(366 - n))
c = ["생일이 같은 쌍이 나올 확률"]
c2 = ["생일이 같은 쌍이 나오는 경우의 수"]

if mode:
    chart_and_table(l, number, c, c2, f)

    st.write(number, "개의 그룹에 그룹당 ", n, "명의 사람들이 있을 때 그룹 안에서 생일이 같은 사람이 생길 확률은 ", float(l[-1][0]), "이다. ")
    st.write("이론상 확률은 ", "$1 - { 366! \\over {366}^{%d} (366-%d)!}$" % (n, n), "≈", float(f), "이다. ")

else:
    with st.spinner("로드 중..."):
        table(l, number, c, c2)
