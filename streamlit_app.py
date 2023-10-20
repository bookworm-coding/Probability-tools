import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

add_page_title(layout="wide", initial_sidebar_state="expanded")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

show_pages(
    [
        Page("streamlit_app.py", "확률 도구", "🏠"),
        Section("경우의 수 문제", "📁"),
        Page("multipage/제로게임 모든 경우들 열거.py", "제로게임 모든 경우 나열", ""),
        Page("multipage/제로게임 경우의 수.py", "제로게임 경우의 수", ""),
        Section("단순한 확률 문제", "📁"),
        Page("multipage/동전 던지기 확률.py", "동전 던지기 확률" ,"🪙"),
        Page("multipage/가위바위보 확률.py", "가위바위보 확률", "✊"),
        Page("multipage/주사위 확률.py", "주사위 확률", "🎲"),
        Section("복잡한 확률 문제", "📁"),
        Page("multipage/평년 생일 문제 확률.py", "평년 생일 문제 확률", "📅"),
        Page("multipage/윤년 생일 문제 확률.py", "윤년 생일 문제 확률", "📅"),
    ]
)
st.subheader("다양한 확률 그래프 등을 제공합니다.")
st.write("Made by 김강민")
st.write("[소스 코드 Github 주소](https://github.com/bookworm-coding/Probability_test)")
