import streamlit as st

st.set_page_config(
    page_title="확률 도구",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': '''이 앱은 김강민에 의해 만들어졌습니다. '''
    }
)

st.title("확률 도구")
st.subheader("다양한 확률 그래프 등을 제공합니다.")
st.write("Made by 김강민")
st.write("[소스 코드 Github 주소](https://github.com/bookworm-coding/Probability_test)")
