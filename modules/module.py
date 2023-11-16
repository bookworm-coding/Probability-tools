import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from fractions import Fraction
import pandas as pd
import math
from collections import Counter
from random import randint


def df(p_object, length: int, columns=None) -> pd.DataFrame:
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


def fraction(numerator: int, denominator: int):
    return Fraction(numerator, denominator, _normalize=False)


def to_float(iter1: list[list[Fraction]]) -> list[list[float]]:
    result = map(lambda i: list(map(float, i)), iter1)
    return list(result)


def to_longdouble(iter1: list[list[Fraction]]) -> list[list[np.longdouble]]:
    result = map(lambda i: list(map(np.longdouble, i)), iter1)
    return list(result)


def to_numerator(iter1: list[list[Fraction]]) -> list[list[int]]:
    result = map(lambda i: list(map(lambda f: f.numerator, i)), iter1)
    return list(result)


def cut10(data: pd.DataFrame, length: int):
    return data.loc[[i for i in range(int(length / 10), length + 1, int(length / 10))]]


def factorial(__x: int) -> int:
    return int(math.factorial(__x))


def find_same(iterable) -> bool:
    if Counter(iterable).most_common()[0][1] != 1:
        return True
    else:
        return False


def rand0(n: int) -> int:
    return randint(0, n)


def rand1(n: int) -> int:
    return randint(1, n)
