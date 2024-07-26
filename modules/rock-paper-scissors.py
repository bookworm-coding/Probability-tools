from modules.format import *


class RPS(Probability):
	def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]):
		super().__init__("가위바위보 확률", ":material/eda:", header_text, slider_label_text, columns1, columns2)
		self.f = Fraction(1, 3)

	def _calc(self) -> list[int]:
		return rand0(3, self.number)

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
