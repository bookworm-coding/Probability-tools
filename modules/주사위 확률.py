import streamlit as st
from st_pages import add_page_title
import modules.module as m

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("주사위를 던졌을 때 각 눈이 나올 확률")


def dice():
    global l, number
    a = b = c = d = e = f = 0
    l = []
    for i in range(1, number + 1):
        r = m.rand1(6)
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
        l.append([m.fraction(a, i + 1).float, m.fraction(b, i + 1).float, m.fraction(c, i + 1).float,
                  m.fraction(d, i + 1).float, m.fraction(e, i + 1).float, m.fraction(f, i + 1).float])


number = st.slider(label="주사위 던지기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=dice)

l = []
dice()

f = m.fraction(1, 6)

chart_data = m.df(l, index=(i + 1 for i in range(number)), columns=[1, 2, 3, 4, 5, 6])
st.plotly_chart(m.line(chart_data, f.float), use_container_width=True)
st.dataframe(chart_data.loc[[i for i in range(int(number / 10), number + 1, int(number / 10))]])

st.write(number, "번 주사위를 던졌을 때 ", 1, "이 나올 확률은 ", l[-1][0], "이고 ", 2, "가 나올 확률은 ", l[-1][1], "이고 ", 3, "이 나올 확률은 ",
         l[-1][2], "이고 ", 4, "가 나올 확률은 ", l[-1][3], "이고 ", 5, "가 나올 확률은 ", l[-1][4], "이고 ", 6, "이 나올 확률은 ", l[-1][5],
         "이다.")
st.write("이론상 확률은 모두 ", r"$\frac{1}{6}$", "≈", f.float, "이다. ")
