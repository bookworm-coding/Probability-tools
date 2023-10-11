import streamlit as st
import pandas as pd
import numpy as np
from random import randint
from fractions import Fraction

st.set_page_config(
    page_title="동전 던지기 확률",
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

st.title("동전 던지기 확률")
st.subheader("동전을 n번 던졌을 때 각 눈이 나올 확률")


def coin():
    global number, l
    a = b = 0
    l = []
    for i in range(0, number):
        if randint(0, 1) == 0:
            a += 1
        else:
            b += 1
        l.append([float(Fraction(a, a + b)), float(Fraction(b, a + b))])


number = st.slider(label="동전 던지기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=coin)

l = []
coin()

chart_data = pd.DataFrame(np.array(l), columns=["앞면", "뒷면"])
st.line_chart(chart_data)

st.write(number, "번 동전을 던졌을 때 앞면이 나올 확률은 ", l[-1][0], "이고 뒷면이 나올 확률은", l[-1][1], "이다.")
st.write("이론상 확률은 앞면, 뒷면 모두 ", r"$\frac{1}{2}$", "=", float(Fraction(1, 2)), "이다. ")
