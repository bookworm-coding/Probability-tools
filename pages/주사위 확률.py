import streamlit as st
import pandas as pd
import numpy as np
from random import randint
from fractions import Fraction

st.set_page_config(
    page_title="주사위 확률",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': '''이 앱은 김강민에 의해 만들어졌습니다. '''
    }
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("주사위 확률")
st.subheader("주사위를 n번 던졌을 때 각 눈이 나올 확률")


def dice():
    global l, number
    a = b = c = d = e = f = 0
    l = []
    for i in range(0, number):
        r = randint(1, 6)
        if r == 1:
            a += 1
        elif r == 2:
            b += 1
        elif r == 3:
            c += 1
        elif r == 4:
            d += 1
        elif r == 5:
            e += 1
        elif r == 6:
            f += 1
        l.append([float(Fraction(a, i + 1)), float(Fraction(b, i + 1)), float(Fraction(c, i + 1)),
                  float(Fraction(d, i + 1)), float(Fraction(e, i + 1)), float(Fraction(f, i + 1))])


number = st.slider(label="주사위 던지기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=dice)

l = []
dice()

chart_data = pd.DataFrame(np.array(l), columns=[1, 2, 3, 4, 5, 6])
st.line_chart(chart_data)

st.write(number, "번 주사위를 던졌을 때 ", 1, "이 나올 확률은 ", l[-1][0], "이고 ", 2, "가 나올 확률은 ", l[-1][1], "이고 ", 3, "이 나올 확률은 ",
         l[-1][2],
         "이고 ", 4, "가 나올 확률은 ", l[-1][3], "이고 ", 5, "가 나올 확률은 ", l[-1][4], "이고 ", 6, "이 나올 확률은 ", l[-1][5], "이다.")
st.write("이론상 확률은 모두 ", r"$\frac{1}{6}$", "≈", float(Fraction(1, 6)), "이다. ")
