import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

add_page_title(layout="wide", initial_sidebar_state="expanded")

show_pages(
    [
        Page("streamlit_app.py", "확률 도구", "🏠"),
        Section("경우의 수 문제", "📁"),
        Page("modules/zerogame-list-all-cases.py", "제로게임 모든 경우 나열", None),
        Page("modules/zerogame-number-of-cases.py", "제로게임 경우의 수", None),
        Section("단순한 확률 문제", "📁"),
        Page("modules/coin.py", "동전 던지기 확률", "🪙"),
        Page("modules/rock-paper-scissors.py", "가위바위보 확률", "✊"),
        Page("modules/dice.py", "주사위 확률", "🎲"),
        Page("modules/lottery.py", "추첨 확률", "🗳️"),
        Section("반복된 확률 문제", "📁"),
        Page("modules/repetitious-coin.py", "반복된 동전 던지기 확률", "🪙"),
        Page("modules/repetitious-rock-paper-scissors.py", "반복된 가위바위보 확률", "✊"),
        Page("modules/repetitious-dice.py", "반복된 주사위 확률", "🎲"),
        Page("modules/repetitious-lottery.py", "반복된 추첨 확률", "🗳️"),
        Section("복잡한 확률 문제", "📁"),
        Page("modules/birthday.py", "생일 문제 확률", "📅"),
    ]
)

st.subheader("다양한 확률 그래프 등을 제공합니다.")
st.write("[데스크탑 버전 다운로드](https://github.com/bookworm-coding/Probability-tools-desktop/releases)")
st.write("[소스 코드 Github 주소](https://github.com/bookworm-coding/Probability-tools)")
st.write("[데스크탑 버전 Github 주소](https://github.com/bookworm-coding/Probability-tools-desktop)")
