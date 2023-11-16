import streamlit as st
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("가위바위보를 2명이 할 때 A가 이길 확률, 비길 확률, 질 확률")


def rcp():
    global number, l
    n1 = n2 = n3 = 0
    for i in range(1, number + 1):
        a, b = rand1(3), rand1(3)
        if a == b:
            n2 += 1
        elif a == 3 and b == 1:
            n3 += 1
        elif a == 1 and b == 3:
            n1 += 1
        elif a > b:
            n1 += 1
        else:
            n3 += 1
        l.append([fraction(n1, i), fraction(n2, i), fraction(n3, i)])


mode: bool = (st.sidebar.radio(
    "모드를 선택하세요",
    ["일반모드", "특수모드"],
    captions=["10부터 10,000번 중 선택한 만큼 테스트하여 그래프와 확률 표로 나타냅니다. 일반적인 상황에서 이용합니다.",
              "1,000,000번 테스트하여 경우의 수와 확률 표로 나타냅니다. 대규모 테스트가 필요한 상황에 사용합니다. "]
) == "일반모드")

if mode:
    number = st.slider(label="가위바위보 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=rcp)

else:
    number = 1000000

l = []
rcp()

f = fraction(1, 3)
c = ["이길 확률", "비길 확률", "질 확률"]
c2 = ["이기는 경우의 수", "비기는 경우의 수", "지는 경우의 수"]

if mode:
    chart_data = df(to_float(l), number, c)
    st.plotly_chart(line(chart_data, float(f)), use_container_width=True)
    data = cut10(df(to_numerator(l), number, c2), number)
    st.dataframe(pd.concat([data, cut10(df(to_float(l), number, c), number)], axis=1))

    st.write("A와 B가 ", number, "번 가위바위보를 했을 때 A가 이긴 확률은 ", float(l[-1][0]), "이고 A와 B가 비긴 확률은 ", float(l[-1][1]), "이고 A가 진 확률은 ",
             float(l[-1][2]), "이다. ")
    st.write("이론상 확률은 모두 ", "$\\frac{%d}{%d}$" % (f.numerator, f.denominator), "≈", float(f), "이다. ")

else:
    with st.spinner("로드 중..."):
        data = cut10(df(to_numerator(l), number, c2), number)
        st.dataframe(pd.concat([data, cut10(df(to_float(l), number, c), number)], axis=1))
