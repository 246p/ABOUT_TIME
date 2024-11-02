import streamlit as st
import time
import base64
from api import *

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return encoded

## API key가 없을때
def check_page():
    pass

# 입력 페이지 함수
def input_page():
    image_path = "main.png"
    encoded_image = get_base64_image(image_path)
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-attachment: fixed;
        background-size: cover;
    }}
    h1 {{
        font-size: 5em;  /* 제목 크기 조정 */
        color: white;    /* 제목 색상 조정 */
        text-align: center;  /* 제목 정렬 */
        margin-top: 20px; /* 제목 상단 여백 */
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

    st.title("어바웃 타임")
    st.write("상대방과의 대화 내역과 특별한 정보를 입력하세요.")

    # 대화 내역 파일 업로드
    uploaded_file = st.file_uploader("상대방과의 대화 내역 (txt 파일)", type="txt")

    # 사용자 입력
    special_info = st.text_area("사용자가 알고 있는 특별한 정보")

    if st.button("챗봇 생성"):
        if uploaded_file is not None and special_info:
            # 세션 상태에 정보 저장
            chat_log= parse(uploaded_file)
            st.session_state.persona=make_persona(chat_log, special_info)
            st.session_state.uploaded_file = chat_log
            st.session_state.special_info = special_info
            # 챗봇 페이지로 전환
            st.session_state.page = "chatbot"
            st.rerun()  # 페이지 리로드
        else:
            st.error("모든 정보를 입력해 주세요.")

# 챗봇 페이지 함수
def chatbot_page():
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://cdn.pixabay.com/photo/2017/08/06/23/22/people-2597454_1280.jpg");
        background-attachment: fixed;
        background-size: cover;
    }}
    h1 {{
        font-size: 5em;  /* 제목 크기 조정 */
        color: white;    /* 제목 색상 조정 */
        text-align: center;  /* 제목 정렬 */
        margin-top: 20px; /* 제목 상단 여백 */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

    st.title("챗봇과의 대화")

    # 챗봇과의 대화창
    chat_input = st.text_input("대화 입력:")

    # 다음 내가 보내는 메시지에 대한 평가
    if st.button("대화 평가"):
        st.write(evaluate(st.session_state))

    # 상대방 정보 요약
    st.write("상대방 정보 요약:")
    st.write(summarey(st.session_state))

    # 연애 팁
    st.write(tips(st.session_state))

    # 데이트 코스 추천 버튼
    if st.button("데이트 코스 추천"):
        st.write(date_course(st.session_state))


# 챗봇 응답 생성 함수 (예시)
def generate_response(user_input, uploaded_file, special_info):
    # 여기에 챗봇의 응답 생성 로직을 구현
    return "이것은 예시 응답입니다."