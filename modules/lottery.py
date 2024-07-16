from modules.format import *


class Lottery(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]) -> None:
        super().__init__("추첨 확률", ":material/how_to_vote:", header_text, slider_label_text, columns1, columns2)
        self.x = st.slider(label="당첨 개수", min_value=1, max_value=10, value=5, step=1, on_change=self.calc)
        self.y = st.slider(label="꽝 개수", min_value=1, max_value=10, value=5, step=1, on_change=self.calc)
        self.f = Fraction(self.x, self.x + self.y)
        return

    def calc(self):
        self.data = [0] * self.length
        randata: list[int] = rand0(self.x + self.y, self.number)
        for i in range(self.number):
            if randata[i] < self.x:
                self.data[0] += 1
            self.result.append(to_fraction(self.data, i + 1))
        return

    def write(self):
        st.write(self.number, "번 추첨했을 때 당첨이 나올 확률은 ", float(self.result[-1][0]), "이다.")
        st.write("이론상 확률은  ", "$\\frac{%d}{%d}$" % (self.f.numerator, self.f.denominator), "=", float(self.f), "이다. ")
        return


Lottery(
    header_text="추첨(뽑기, 돌림판 등)할 때 당첨이 나올 확률",
    slider_label_text="추첨 횟수",
    columns1=["당첨이 나올 확률"],
    columns2=["당첨이 나오는 경우의 수"],
).main()
