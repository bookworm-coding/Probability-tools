import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

add_page_title(page_title="확률 도구",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":house:"
)

show_pages(
    [
        Page("🏠홈.py", "확률 도구", ":house:"),
        Section("단순한 확률 문제", ":file_folder:"),
        Page("multipage/동전 던지기 확률.py", "동전 던지기 확률" ,":coin:"),
        Page("multipage/가위바위보 확률.py", "가위바위보 확률", ":fist:"),
        Page("multipage/주사위 확률.py", "주사위 확률", ":game_die:"),
        Section("복잡한 확률 문제", ":file_folder:"),
        Page("multipage/평년 생일 문제 확률.py", "평년 생일 문제 확률", ":date:"),
        Page("multipage/윤년 생일 문제 확률.py", "윤년 생일 문제 확률", ":date:"),
    ]
)

#st.title("확률 도구")
st.subheader("다양한 확률 그래프 등을 제공합니다.")
st.write("Made by 김강민")
st.write("[소스 코드 Github 주소](https://github.com/bookworm-coding/Probability_test)")
