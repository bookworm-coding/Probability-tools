import pandas as pd
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="제로게임 모든 경우 나열", layout="wide", initial_sidebar_state="expanded")
st.title("제로게임 모든 경우 나열")

st.subheader("제로게임에서 각 숫자를 불렀을 때 이를 만족하는 모든 경우를 나열")


class Zero(pd.DataFrame):
	def __init__(self, number: int):
		self.n = number
		for i in range(2 * self.n + 1):
			self.l.append([])
		self.zero([])
		super().__init__(data=self.l, columns=range(1, len(self.l[self.n * -1 - 1]) + 1))

	def zero(self, a: list):
		if len(a) == self.n:
			s = 0
			for i in a:
				s += i
			self.l[s].append(tuple(a))
		else:
			self.zero(a + [0])
			self.zero(a + [1])
			self.zero(a + [2])


n = st.slider("인원수", min_value=1, max_value=10, value=2, step=1)
with st.spinner("로딩 중..."):
	z = Zero(n)
	if n > 5:
		st.info("5보다 큰 경우에는 온라인으로 보는 것이 지원되지 않고, 엑셀 파일 저장만 지원합니다. ")
	else:
		st.dataframe(z, column_config=st.column_config.ListColumn(width="large"), use_container_width=True)
	f = BytesIO()
	z.to_excel(f)
	st.download_button("표 다운로드", f, file_name="제로게임 경우의 수.xlsx",
	                   mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
