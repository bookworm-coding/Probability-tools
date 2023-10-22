import streamlit as st
import pandas as pd
import numpy as np
from random import randint
from fractions import Fraction
from st_pages import add_page_title
import plotly.express as px

add_page_title(layout="wide", initial_sidebar_state="expanded",)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
        l.append([float(Fraction(a, a + b)), float(Fraction(b, a + b))])


number = st.slider(label="동전 던지기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=coin)

l = []
coin()

f = Fraction(1,2)

chart_data = pd.DataFrame(np.array(l), columns=["앞면", "뒷면"])
fig = px.line(chart_data)
fig.update_layout(xaxis_title="", yaxis_title="", legend_title="")
fig.add_hline(y=float(f), line_dash="dot")
fig.update_layout(margin=dict(l=0,r=0,b=0,t=0))
st.plotly_chart(fig, use_container_width=True)

st.write(number, "번 동전을 던졌을 때 앞면이 나올 확률은 ", l[-1][0], "이고 뒷면이 나올 확률은", l[-1][1], "이다.")
st.write("이론상 확률은 앞면, 뒷면 모두 ", r"$\frac{1}{2}$", "=", np.longdouble(f), "이다. ")
