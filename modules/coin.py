from modules.format import *


class Coin(Probability):
    f = fraction(1, 2)

    def calc(self):
        super().calc()
        a = b = 0
        for i in range(1, self.number + 1):
            if rand1(2) == 1:
                a += 1
            else:
                b += 1
            self.result.append([fraction(a, a + b), fraction(b, a + b)])
        return

    def write(self):
        st.write(self.number, "번 동전을 던졌을 때 앞면이 나올 확률은 ", float(self.result[-1][0]), "이고 뒷면이 나올 확률은",
                 float(self.result[-1][1]), "이다.")
        st.write("이론상 확률은 앞면, 뒷면 모두 ", "$\\frac{%d}{%d}$" % (self.f.numerator, self.f.denominator), "=", float(self.f),
                 "이다. ")


Coin(
    header_text="동전을 던졌을 때 각 눈이 나올 확률",
    slider_label_text="동전 던지기 횟수",
    columns1=["앞면이 나올 확률", "뒷면이 나올 확률"],
    columns2=["앞면이 나오는 경우의 수", "뒷면이 나오는 경우의 수"]
).main()
