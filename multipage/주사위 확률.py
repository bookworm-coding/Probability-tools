import streamlit as st
import pandas as pd
import numpy as np
from random import randint
from fractions import Fraction
from st_pages import add_page_title
import plotly.express as px

add_page_title(layout="wide", initial_sidebar_state="expanded", )

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.subheader("주사위를 던졌을 때 각 눈이 나올 확률")


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

f = Fraction(1, 6)

chart_data = pd.DataFrame(np.array(l), columns=[1, 2, 3, 4, 5, 6])
fig = px.line(chart_data)
fig.update_layout(xaxis_title=None, yaxis_title=None, legend_title=None)
fig.add_hline(y=float(f), line_dash="dot")
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.update_layout(legend=dict(
    yanchor="middle",
    y=0.01,
    xanchor="left",
    x=0.01,
    orientation="h"
))
st.plotly_chart(fig, use_container_width=True)

st.write(number, "번 주사위를 던졌을 때 ", 1, "이 나올 확률은 ", l[-1][0], "이고 ", 2, "가 나올 확률은 ", l[-1][1], "이고 ", 3, "이 나올 확률은 ",
         l[-1][2],
         "이고 ", 4, "가 나올 확률은 ", l[-1][3], "이고 ", 5, "가 나올 확률은 ", l[-1][4], "이고 ", 6, "이 나올 확률은 ", l[-1][5], "이다.")
st.write("이론상 확률은 모두 ", r"$\frac{1}{6}$", "≈", float(f), "이다. ")
