from modules.format import *


class RLottery(Probability):
	def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]):
		super().__init__("반복된 추첨 확률", ":material/how_to_vote:", header_text, slider_label_text, columns1, columns2)
		self.n = st.slider(label="연속 횟수", min_value=2, max_value=10, value=2, step=1, on_change=self.calc)
		self.x = st.slider(label="당첨 개수", min_value=1, max_value=10, value=5, step=1, on_change=self.calc)
		self.y = st.slider(label="꽝 개수", min_value=1, max_value=10, value=5, step=1, on_change=self.calc)
		self.f = Fraction(self.x, self.x + self.y) ** self.n

	def calc(self):
		self.data = [0] * self.length
		randata: list[list[int]] = rand0(self.x + self.y, (self.number, self.n))
		for i in range(self.number):
			temp = True
			for j in range(self.n):
				if randata[i][j] >= self.x:
					temp = False
					break
			if temp:
				self.data[0] += 1
			self.result.append(to_fraction(self.data, i + 1))

	def write(self):
		st.write(self.number, "번 추첨을 ", self.n, "번 했을때 당첨이 연속으로 ", self.n, "번 나올 확률은 ", float(self.result[-1][0]), "이다.")
		st.write("이론상 확률은  ", "$(\\frac{%d}{%d})^{%d}$" % (self.x, self.x + self.y, self.n), "=", float(self.f), "이다. ")


RLottery(
	header_text="추첨(뽑기, 돌림판 등)할 때 N번 연속으로 당첨이 나올 확률",
	slider_label_text="N번 추첨하는 횟수",
	columns1=["당첨이 N번 연속으로 나올 확률"],
	columns2=["당첨이 N번 연속으로 나오는 경우의 수"],
).main()
