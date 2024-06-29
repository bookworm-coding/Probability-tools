from modules.format import *


class Birthday(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]) -> None:
        super().__init__("생일 문제 확률", ":material/calendar_month:", header_text, slider_label_text, columns1, columns2)
        if st.sidebar.toggle("윤년 모드"):
            self.year = 366
        else:
            self.year = 365
        self.n = st.slider(label="그룹 당 사람 수", min_value=2, max_value=self.year, value=5, step=1, on_change=self.calc)
        self.f = Fraction(1, 1) - Fraction(factorial(self.year), self.year ** self.n * factorial(self.year - self.n))
        return

    def _calc(self) -> None:
        temp = []
        for j in range(0, self.n):
            temp.append(rand1(self.year))
        if find_same(temp):
            self.temp[0] += 1
        return

    def write(self) -> None:
        st.write(self.number, "개의 그룹에 그룹당 ", self.n, "명의 사람들이 있을 때 그룹 안에서 생일이 같은 사람이 생길 확률은 ",
                 float(self.result[-1][0]), "이다. ")
        st.write("이론상 확률은 ", "$1 - { %d! \\over {%d}^{%d} (%d-%d)!}$" % (self.year, self.year, self.n, self.year,self.n), "≈",
                 float(self.f), "이다. ")
        return


Birthday(
    header_text="n명이 있을 때 생일이 같은 쌍이 나올 확률",
    slider_label_text="그룹의 개수",
    columns1=["생일이 같은 쌍이 나올 확률"],
    columns2=["생일이 같은 쌍이 나오는 경우의 수"]
).main()
