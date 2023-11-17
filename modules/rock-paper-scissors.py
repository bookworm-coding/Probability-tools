from modules.format import *


class RPS(Probability):
    f = fraction(1, 3)

    def calc(self):
        super().calc()
        n1 = n2 = n3 = 0
        for i in range(1, self.number + 1):
            a, b = rand1(3), rand1(3)
            if a == b:
                n2 += 1
            elif a == 3 and b == 1:
                n3 += 1
            elif a == 1 and b == 3:
                n1 += 1
            elif a > b:
                n1 += 1
            else:
                n3 += 1
            self.result.append([fraction(n1, i), fraction(n2, i), fraction(n3, i)])
        return

    def write(self):
        st.write("A와 B가 ", self.number, "번 가위바위보를 했을 때 A가 이기는 확률은 ", float(self.result[-1][0]), "이고 A와 B가 비기는 확률은 ",
                 float(self.result[-1][1]),
                 "이고 A가 지는 확률은 ", float(self.result[-1][2]), "이다. ")
        st.write("이론상 확률은 모두 ", "$\\frac{%d}{%d}$" % (self.f.numerator, self.f.denominator), "≈", float(self.f), "이다. ")


RPS(
    header_text="가위바위보를 2명이 할 때 A가 이길 확률, 비길 확률, 질 확률",
    slider_label_text="가위바위보 횟수",
    columns1=["이길 확률", "비길 확률", "질 확률"],
    columns2=["이기는 경우의 수", "비기는 경우의 수", "지는 경우의 수"]
).main()
