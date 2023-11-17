import streamlit as st
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("추첨(뽑기, 돌림판 등)할 때 당첨이 나올 확률")


def lottery():
    global number, l
    a = 0
    l = []
    for i in range(1, number + 1):
        if rand1(x + y) <= x:
            a += 1
        l.append([fraction(a, i)])


mode = m()

if mode:
    number = st.slider(label="뽑기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=lottery)

else:
    number = 1000000

x = st.slider(label="당첨 개수", min_value=1, max_value=10, value=5, step=1, on_change=lottery)
y = st.slider(label="꽝 개수", min_value=1, max_value=10, value=5, step=1, on_change=lottery)

l = []
lottery()

f = fraction(x, x + y)
c = ["당첨이 나올 확률"]
c2 = ["당첨이 나오는 경우의 수"]

if mode:
    chart_and_table(l, number, c, c2, f)

    st.write(number, "번 추첨했을 때 당첨이 나올 확률은 ", float(l[-1][0]), "이다.")
    st.write("이론상 확률은  ", "$\\frac{%d}{%d}$" % (f.numerator, f.denominator), "=", float(f), "이다. ")

else:
    with st.spinner("로드 중..."):
        table(l, number, c, c2)
