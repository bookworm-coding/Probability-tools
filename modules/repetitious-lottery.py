from modules.format import *


class RLottery(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]) -> None:
        super().__init__(header_text, slider_label_text, columns1, columns2)
        self.n = st.slider(label="연속 횟수", min_value=2, max_value=10, value=5, step=1, on_change=self.calc)
        self.x = st.slider(label="당첨 개수", min_value=1, max_value=10, value=5, step=1, on_change=self.calc)
        self.y = st.slider(label="꽝 개수", min_value=1, max_value=10, value=5, step=1, on_change=self.calc)
        self.f = fraction(self.x, self.x + self.y) ** self.n
        return

    def calc(self) -> None:
        super().calc()
        a = 0
        for i in range(1, self.number + 1):
            temp = True
            for j in range(1, self.n + 1):
                if not temp:
                    continue
                else:
                    temp = temp and rand1(self.x + self.y) <= self.x
            if temp:
                a += 1
            self.result.append([fraction(a, i)])
        return

    def write(self) -> None:
        st.write(self.number, "번 추첨을 ", self.n, "번 했을때 당첨이 연속으로 ", self.n, "번 나올 확률은 ", float(self.result[-1][0]), "이다.")
        st.write("이론상 확률은  ", "$(\\frac{%d}{%d})^{%d}$" % (self.x, self.x + self.y, self.n), "=", float(self.f), "이다. ")
        return


RLottery(
    header_text="추첨(뽑기, 돌림판 등)할 때 N번 연속으로 당첨이 나올 확률",
    slider_label_text="N번 추첨하는 횟수",
    columns1=["당첨이 N번 연속으로 나올 확률"],
    columns2=["당첨이 N번 연속으로 나오는 경우의 수"],
).main()
