from modules.format import *


class RRPS(Probability):
	def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]):
		super().__init__("반복된 가위바위보 확률", ":material/eda:", header_text, slider_label_text, columns1, columns2)
		self.n = st.slider(label="연속 횟수", min_value=2, max_value=10, value=2, step=1, on_change=self.calc)
		self.f = Fraction(1, 3) ** self.n

	def calc(self):
		self.data = [0] * self.length
		randata: list[list[int]] = rand0(3, (self.number, self.n))
		for i in range(self.number):
			if randata[i].count(0) == self.n:
				self.data[0] += 1
			self.result.append(to_fraction(self.data, i + 1))

	def write(self):
		st.write("A와 B가 ", self.number, "번 가위바위보를 했을 때 A가 ", self.n, "번 연속으로 이기는 확률은 ", float(self.result[-1][0]), "이다. ")
		st.write("이론상 확률은 ", "$(\\frac{1}{3})^{%d}$" % self.n, "≈", float(self.f), "이다. ")


RRPS(
	header_text="가위바위보를 2명이 할 때 A가 N번 연속으로 이길 확률",
	slider_label_text="가위바위보를 N번 하는 횟수",
	columns1=["N번 연속으로 이길 확률"],
	columns2=["N번 연속으로 이기는 경우의 수"]
).main()
