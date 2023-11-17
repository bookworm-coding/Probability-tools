import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from fractions import Fraction
import pandas as pd
from pandas._typing import Axes
import math
from collections import Counter
from random import randint
import streamlit as st


def df(p_object, length: int, columns: Axes = None) -> pd.DataFrame:
    return pd.DataFrame(np.array(p_object), index=range(1, length + 1), columns=columns)


def line(chart_data: pd.DataFrame, y: float = None) -> go.Figure:
    fig = px.line(chart_data)
    fig.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        legend_title=None,
        margin=dict(l=0, r=0, b=0, t=0),
        legend=dict(
            yanchor="middle",
            y=0.01,
            xanchor="left",
            x=0.01,
            orientation="h"
        )
    )
    if y is not None:
        fig.add_hline(y=y, line_dash="dot")
    return fig


def to_float(iter1: list[list[Fraction]]) -> list[list[float]]:
    result = map(lambda i: list(map(float, i)), iter1)
    return list(result)


def to_numerator(iter1: list[list[Fraction]]) -> list[list[int]]:
    result = map(lambda i: list(map(lambda f: f.numerator, i)), iter1)
    return list(result)


def cut10(data: pd.DataFrame, length: int) -> pd.DataFrame:
    return data.loc[[i for i in range(int(length / 10), length + 1, int(length / 10))]]


def factorial(__x: int) -> int:
    return int(math.factorial(__x))


def find_same(iterable) -> bool:
    return Counter(iterable).most_common()[0][1] != 1


def rand0(n: int) -> int:
    return randint(0, n)


def rand1(n: int) -> int:
    return randint(1, n)


def chart_and_table(l: list[list[Fraction]], length: int, columns1: Axes, columns2: Axes, f: Fraction) -> None:
    chart(l, length, columns1, f)
    table(l, length, columns1, columns2)


def table(l: list[list[Fraction]], length: int, columns1: Axes, columns2: Axes) -> None:
    data = cut10(df(to_numerator(l), length, columns2), length)
    st.dataframe(pd.concat([data, cut10(df(to_float(l), length, columns1), length)], axis=1))
    return


def chart(l: list[list[Fraction]], length: int, columns: Axes, f: Fraction) -> None:
    chart_data = df(to_float(l), length, columns)
    st.plotly_chart(line(chart_data, float(f)), use_container_width=True)
    return


def m() -> bool:
    return st.sidebar.radio("모드를 선택하세요", ["일반모드", "특수모드"],
                            captions=["10부터 10,000번 중 선택한 만큼 테스트하여 그래프와 확률 표로 나타냅니다. 일반적인 상황에서 이용합니다.",
                                      "1,000,000번 테스트하여 경우의 수와 확률 표로 나타냅니다. 대규모 테스트가 필요한 상황에 사용합니다. "]
                            ) == "일반모드"


def fraction(numerator=0, denominator=None):
    return Fraction(numerator, denominator, _normalize=False)