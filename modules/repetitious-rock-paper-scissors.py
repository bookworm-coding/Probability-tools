from modules.format import *


class RRPS(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]):
        super().__init__(header_text, slider_label_text, columns1, columns2)
        self.n = st.slider(label="연속 횟수", min_value=2, max_value=10, value=5, step=1, on_change=self.calc)
        self.f = fraction(1, 3) ** self.n

    def calc(self):
        super().calc()
        n1 = 0
        for i in range(1, self.number + 1):
            temp = True
            for j in range(1, self.n + 1):
                if not temp:
                    continue
                else:
                    a, b = rand1(3), rand1(3)
                    if a == 1 and b == 3:
                        pass
                    elif a > b:
                        pass
                    else:
                        temp = False
                        continue
            if temp:
                n1 += 1
            self.result.append([fraction(n1, i)])
        return

    def write(self):
        st.write("A와 B가 ", self.number, "번 가위바위보를 했을 때 A가 ", self.n, "번 연속으로 이기는 확률은 ", float(self.result[-1][0]), "이다. ")
        st.write("이론상 확률은 ", "$(\\frac{1}{3})^{%d}$" % self.n, "≈", float(self.f), "이다. ")


RRPS(
    header_text="가위바위보를 2명이 할 때 A가 N번 연속으로 이길 확률",
    slider_label_text="가위바위보를 N번 하는 횟수",
    columns1=["N번 연속으로 이길 확률"],
    columns2=["N번 연속으로 이기는 경우의 수"]
).main()
