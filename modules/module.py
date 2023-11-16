import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from fractions import Fraction
import pandas as pd
import math
from collections import Counter
from random import randint


def df(p_object, *args, **kwargs):
    return pd.DataFrame(np.array(p_object), *args, **kwargs)


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


class fraction(Fraction):
    def __new__(cls, numerator, denominator, *args, **kwargs):
        cls = super().__new__(cls, numerator=numerator, denominator=denominator, *args, **kwargs)
        cls.longdouble = np.longdouble(cls)
        cls.float = float(cls)
        return cls

    def __sub__(a, b):
        """a - b"""
        na, da = a.numerator, a.denominator
        nb, db = b.numerator, b.denominator
        g = math.gcd(da, db)
        if g == 1:
            return fraction(na * db - da * nb, da * db, _normalize=False)
        s = da // g
        t = na * (db // g) - nb * s
        g2 = math.gcd(t, g)
        if g2 == 1:
            return fraction(t, s * db, _normalize=False)
        return fraction(t // g2, s * (db // g2), _normalize=False)


def factorial(__x: int) -> int:
    return int(math.factorial(__x))


def find_same(iterable):
    if Counter(iterable).most_common()[0][1] != 1:
        return True
    else:
        return False


def rand0(n: int):
    return randint(0, n)


def rand1(n: int):
    return randint(1, n)
