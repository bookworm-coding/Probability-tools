import streamlit as st
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("동전을 던졌을 때 각 눈이 나올 확률")


def coin():
    global number, l
    a = b = 0
    l = []
    for i in range(1, number + 1):
        if rand1(2) == 1:
            a += 1
        else:
            b += 1
        l.append([Fraction(a, a + b), Fraction(b, a + b)])


mode = m()

if mode:
    number = st.slider(label="동전 던지기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=coin)

else:
    number = 1000000

l = []
coin()

f = Fraction(1, 2)
c = ["앞면이 나올 확률", "뒷면이 나올 확률"]
c2 = ["앞면이 나오는 경우의 수", "뒷면이 나오는 경우의 수"]

if mode:
    chart_and_table(l, number, c, c2, f)

    st.write(number, "번 동전을 던졌을 때 앞면이 나올 확률은 ", float(l[-1][0]), "이고 뒷면이 나올 확률은", float(l[-1][1]), "이다.")
    st.write("이론상 확률은 앞면, 뒷면 모두 ", "$\\frac{%d}{%d}$" % (f.numerator, f.denominator), "=", float(f), "이다. ")

else:
    with st.spinner("로드 중..."):
        table(l, number, c, c2)
