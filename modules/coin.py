from modules.format import *


class Coin(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]):
        super().__init__(header_text, slider_label_text, columns1, columns2)
        self.f = fraction(1, 2)

    def _calc(self) -> None:
        if rand1(2) == 1:
            self.temp[0] += 1
        else:
            self.temp[1] += 1
        return

    def write(self) -> None:
        st.write(self.number, "번 동전을 던졌을 때 앞면이 나올 확률은 ", float(self.result[-1][0]), "이고 뒷면이 나올 확률은",
                 float(self.result[-1][1]), "이다.")
        st.write("이론상 확률은 앞면, 뒷면 모두 ", "$\\frac{%d}{%d}$" % (self.f.numerator, self.f.denominator), "=", float(self.f),
                 "이다. ")
        return


Coin(
    header_text="동전을 던졌을 때 앞면, 뒷면이 나올 확률",
    slider_label_text="동전 던지기 횟수",
    columns1=["앞면이 나올 확률", "뒷면이 나올 확률"],
    columns2=["앞면이 나오는 경우의 수", "뒷면이 나오는 경우의 수"]
).main()
