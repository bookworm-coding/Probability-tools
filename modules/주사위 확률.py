import streamlit as st
from st_pages import add_page_title
from modules.module import *

add_page_title(layout="wide", initial_sidebar_state="expanded")

st.subheader("주사위를 던졌을 때 각 눈이 나올 확률")


def dice():
    global l, number
    a = b = c = d = e = f = 0
    l = []
    for i in range(1, number + 1):
        r = rand1(6)
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
        l.append([Fraction(a, i), Fraction(b, i), Fraction(c, i),
                  Fraction(d, i), Fraction(e, i), Fraction(f, i)])


mode: bool = (st.sidebar.radio(
    "모드를 선택하세요",
    ["일반모드", "특수모드"],
    captions=["10부터 10,000번 중 선택한 만큼 테스트하여 그래프와 확률 표로 나타냅니다. 일반적인 상황에서 이용합니다.",
              "1,000,000번 테스트하여 경우의 수와 확률 표로 나타냅니다. 대규모 테스트가 필요한 상황에 사용합니다. "]
) == "일반모드")

if mode:
    number = st.slider(label="주사위 던지기 횟수", min_value=10, max_value=10000, value=100, step=10, on_change=dice)

else:
    number = 1000000

l = []
dice()

f = Fraction(1, 6)
c = ["1이 나올 확률", "2가 나올 확률", "3이 나올 확률", "4가 나올 확률", "5가 나올 확률", "6이 나올 확률"]
c2 = ["1이 나오는 경우의 수", "2가 나오는 경우의 수", "3이 나오는 경우의 수", "4가 나오는 경우의 수", "5가 나오는 경우의 수", "6이 나오는 경우의 수"]

if mode:
    chart_data = df(to_float(l), number, c)
    st.plotly_chart(line(chart_data, float(f)), use_container_width=True)
    data = cut10(df(to_numerator(l), number, c2), number)
    st.dataframe(pd.concat([data, cut10(df(to_float(l), number, c), number)], axis=1))

    st.write(number, "번 주사위를 던졌을 때 ", 1, "이 나올 확률은 ", float(l[-1][0]), "이고 ", 2, "가 나올 확률은 ", float(l[-1][1]), "이고 ",
             3, "이 나올 확률은 ", float(l[-1][2]), "이고 ", 4, "가 나올 확률은 ", float(l[-1][3]), "이고 ",
             5, "가 나올 확률은 ", float(l[-1][4]), "이고 ", 6, "이 나올 확률은 ", float(l[-1][5]), "이다.")
    st.write("이론상 확률은 모두 ", "$\\frac{%d}{%d}$" % (f.numerator, f.denominator), "≈", float(f), "이다. ")

else:
    with st.spinner("로드 중..."):
        data = cut10(df(to_numerator(l), number, c2), number)
        st.dataframe(pd.concat([data, cut10(df(to_float(l), number, c), number)], axis=1))
