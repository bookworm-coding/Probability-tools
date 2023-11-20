from modules.format import *


class RCoin(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]) -> None:
        super().__init__(header_text, slider_label_text, columns1, columns2)
        self.n = st.slider(label="연속 횟수", min_value=2, max_value=10, value=5, step=1, on_change=self.calc)
        self.f = fraction(1, 2) ** self.n
        return

    def _calc(self) -> None:
        temp = True
        for j in range(1, self.n + 1):
            if not temp:
                continue
            else:
                temp = temp and rand1(2) == 1
        if temp:
            self.temp[0] += 1
        return

    def write(self) -> None:
        st.write(self.number, "번 동전을 ", self.n, "번 던졌을 때 앞면이 ", self.n, "번 연속 나올 확률은 ", float(self.result[-1][0]),
                 "이다.")
        st.write("이론상 확률은 ", "$(\\frac{1}{2})^{%d}$" % self.n, "=",
                 float(self.f), "이다. ")
        return


RCoin(
    header_text="동전을 던졌을 때 앞면이 N번 연속으로 나올 확률",
    slider_label_text="동전을 N번 던지는 횟수",
    columns1=["N번 연속 앞면이 나올 확률"],
    columns2=["N번 연속 앞면이 나오는 경우의 수"]
).main()
