import math
from collections import Counter
from fractions import Fraction
from random import randint
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st

__all__ = ['Probability', 'Fraction', 'rand1', 'factorial', 'find_same', 'st']


def rand1(n: int) -> int:
    return randint(1, n)


def find_same(iterable) -> bool:
    return Counter(iterable).most_common()[0][1] != 1


def factorial(__x: int) -> int:
    return int(math.factorial(__x))


def cut10(data: pd.DataFrame, length: int) -> pd.DataFrame:
    return data.loc[[i for i in range(int(length / 10), length + 1, int(length / 10))]]


def to_numerator(iter1: list[list[Fraction]]) -> list[list[int]]:
    result = map(lambda i: list(map(lambda f: f.numerator, i)), iter1)
    return list(result)


def to_float(iter1: list[list[Fraction]]) -> list[list[float]]:
    result = map(lambda i: list(map(float, i)), iter1)
    return list(result)


def to_fraction(iter1: list[int], i: int) -> list[Fraction]:
    result = map(lambda x: Fraction(x, i), iter1)
    return list(result)


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


def df(p_object, length: int, columns=None) -> pd.DataFrame:
    return pd.DataFrame(np.array(p_object), index=range(1, length + 1), columns=columns)


class Probability:
    def __init__(self, title: str, icon: str, header_text: str, slider_label_text: str, columns1: list[str],
                 columns2: list[str]) -> None:
        self.temp = []
        self.length = len(columns1)
        st.set_page_config(page_title=title, page_icon=icon, layout="wide", initial_sidebar_state="expanded")
        st.title(title)
        st.subheader(header_text)
        self.number = st.slider(label=slider_label_text, min_value=10, max_value=10000, value=100, step=10,
                                on_change=self.calc)
        self.result = []
        self.columns1 = columns1
        self.columns2 = columns2
        self.f = None

    def main(self) -> None:
        self.calc()
        self.chart_and_table()
        self.write()
        return

    def calc(self) -> None:
        self.temp = []
        for i in range(self.length):
            self.temp.append(0)
        for i in range(1, self.number + 1):
            self._calc()
            self.result.append(to_fraction(self.temp, i))
        return

    def _calc(self) -> None:
        return

    def write(self) -> None:
        return

    def chart_and_table(self) -> None:
        chart_data = df(to_float(self.result), self.number, self.columns1)
        st.plotly_chart(line(chart_data, float(self.f)), use_container_width=True)
        return
