import streamlit as st
import pandas as pd
import numpy as np
from random import randint
from fractions import Fraction
from math import factorial
from collections import Counter

st.set_page_config(
    page_title="평년 생일 문제 확률",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":date:"
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("평년 생일 문제 확률")
st.subheader("n명이 있을 때 생일이 같은 쌍이 나올 확률(평년)")


def birthday():
    global li, number, n
    c = 0
    li = []
    for i in range(1, number + 1):
        l = []
        for j in range(0, n):
            l.append(randint(1, 365))
        if Counter(l).most_common()[0][1] != 1:
            c += 1
        li.append([float(Fraction(c, i))])


number = st.slider(label="그룹의 개수", min_value=10, max_value=10000, value=100, step=10, on_change=birthday)
n = st.slider(label="그룹 당 사람 수", min_value=2, max_value=366, value=5, step=1, on_change=birthday)

birthday()

chart_data = pd.DataFrame(np.array(li), columns=["생일이 같은 쌍이 나올 확률"])
st.line_chart(chart_data)

st.write(number, "개의 그룹에 그룹당 ", n, "명의 사람들이 있을 때 그룹 안에서 생일이 같은 사람이 생길 확률은 ", li[-1][0], "이다. ")
f = Fraction(1, 1) - Fraction(int(factorial(365)), 365 ** n * int(factorial(365 - n)))
st.write("이론상 확률은 ", "$1 - { 365! \\over {365}^{%d} (365-%d)!}$" % (n, n),
         # "=", "$%d \\over %d$" % (f.numerator, f.denominator),
         "≈", np.longdouble(f), "이다. ")
