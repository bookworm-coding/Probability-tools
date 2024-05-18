from modules.format import *


class Dice(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]):
        super().__init__(header_text, slider_label_text, columns1, columns2)
        self.f = Fraction(1, 6)
        
    def _calc(self) -> None:
        r = rand1(6)
        if r == 1:
            self.temp[0] += 1
        elif r == 2:
            self.temp[1] += 1
        elif r == 3:
            self.temp[2] += 1
        elif r == 4:
            self.temp[3] += 1
        elif r == 5:
            self.temp[4] += 1
        elif r == 6:
            self.temp[5] += 1
        return
    
    def write(self) -> None:
        st.write(self.number, "번 주사위를 던졌을 때 ", 1, "이 나올 확률은 ", float(self.result[-1][0]), "이고 ", 2, "가 나올 확률은 ",
                 float(self.result[-1][1]), "이고 ", 3, "이 나올 확률은 ", float(self.result[-1][2]), "이고 ", 4, "가 나올 확률은 ",
                 float(self.result[-1][3]), "이고 ", 5, "가 나올 확률은 ", float(self.result[-1][4]), "이고 ", 6, "이 나올 확률은 ",
                 float(self.result[-1][5]), "이다.")
        st.write("이론상 확률은 모두 ", "$\\frac{%d}{%d}$" % (self.f.numerator, self.f.denominator), "≈", float(self.f), "이다. ")
        return
        
    
Dice(
    header_text="주사위를 던졌을 때 각 눈이 나올 확률",
    slider_label_text="주사위 던지기 횟수",
    columns1=["1이 나올 확률", "2가 나올 확률", "3이 나올 확률", "4가 나올 확률", "5가 나올 확률", "6이 나올 확률"],
    columns2=["1이 나오는 경우의 수", "2가 나오는 경우의 수", "3이 나오는 경우의 수", "4가 나오는 경우의 수", "5가 나오는 경우의 수", "6이 나오는 경우의 수"]
).main()
