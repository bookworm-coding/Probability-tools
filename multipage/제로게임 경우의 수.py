import pandas as pd
import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide", initial_sidebar_state="expanded", )

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

df = None

def zero():
    global n, df
    result = []
    for i in range(0, n):
        if i == 0:
            result.append([1, 1, 1])
        else:
            result.append([])
            for j in range(0, i * 2 + 3):
                if j == 0:
                    result[i].append(1)
                elif j == 1:
                    result[i].append(result[i - 1][0] + result[i - 1][1])
                elif j == i * 2 + 1:
                    result[i].append(result[i - 1][-2] + result[i - 1][-1])
                elif j == i * 2 + 2:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 2] + result[i - 1][j - 1] + result[i - 1][j])
    df = pd.DataFrame(result, index=(i for i in range(1, n+1)))


st.subheader("제로게임에서 각 숫자를 불렀을 때의 경우의 수")
n = st.slider("인원수", min_value=1, max_value=50, value=5, step=1, on_change=zero)
zero()
st.dataframe(df)
st.caption("가로축은 부른 숫자, 세로축은 인원수")
