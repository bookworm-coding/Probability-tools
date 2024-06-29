import streamlit as st

def homepage():
    st.set_page_config(page_title="홈", page_icon=":material/home:")
    st.header("확률 도구")
    st.subheader("다양한 확률 그래프 등을 제공합니다.")
    st.write("[데스크탑 버전 다운로드](https://github.com/bookworm-coding/Probability-tools-desktop/releases)")
    st.write("[소스 코드 Github 주소](https://github.com/bookworm-coding/Probability-tools)")
    st.write("[데스크탑 버전 Github 주소](https://github.com/bookworm-coding/Probability-tools-desktop)")


home = st.Page(homepage, title="홈", icon=":material/home:", default=True)

zlac = st.Page("modules/zerogame-list-all-cases.py", title="제로게임 모든 경우 나열")
znoc = st.Page("modules/zerogame-number-of-cases.py", title="제로게임 경우의 수")

coin = st.Page("modules/coin.py", title="동전 던지기 확률", icon=":material/paid:")
rps = st.Page("modules/rock-paper-scissors.py", title="가위바위보 확률", icon=":material/eda:")
dice = st.Page("modules/dice.py", title="주사위 던지기 확률", icon=":material/ifl:")
lottery = st.Page("modules/lottery.py", title="추첨 확률", icon=":material/how_to_vote:")

rcoin = st.Page("modules/repetitious-coin.py", title="반복된 동전 던지기 확률", icon=":material/paid:")
rrps = st.Page("modules/repetitious-rock-paper-scissors.py", title="반복된 가위바위보 확률", icon=":material/eda:")
rdice = st.Page("modules/repetitious-dice.py", title="반복된 주사위 던지기 확률", icon=":material/ifl:")
rlottery = st.Page("modules/repetitious-lottery.py", title="반복된 추첨 확률", icon=":material/how_to_vote:")

b = st.Page("modules/birthday.py", title="생일 문제 확률", icon=":material/calendar_month:")

st.navigation(
    {
        "홈": [home],
        "경우의 수 문제": [zlac, znoc],
        "단순한 확률 문제": [coin, rps, dice, lottery],
        "반복된 확률 문제": [rcoin, rrps, rdice, rlottery],
        "복잡한 확률 문제": [b],
    }
).run()