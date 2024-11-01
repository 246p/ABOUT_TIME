import streamlit as st
import time

## API key가 없을때
def check_page():
    pass

# 입력 페이지 함수
def input_page():
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

    st.title("어바웃 타임")
    st.write("상대방과의 대화 내역과 특별한 정보를 입력하세요.")

    # 대화 내역 파일 업로드
    uploaded_file = st.file_uploader("상대방과의 대화 내역 (txt 파일)", type="txt")

    # 사용자 입력
    special_info = st.text_area("사용자가 알고 있는 특별한 정보")

    if st.button("챗봇 생성"):
        if uploaded_file is not None and special_info:
            # 로딩 타이머 효과
            with st.spinner("챗봇 생성 중..."):
                time.sleep(3)  # 타이머 효과 (3초 대기)

            # 세션 상태에 정보 저장
            st.session_state.uploaded_file = uploaded_file
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

    # 세션 상태에서 정보 가져오기
    uploaded_file = st.session_state.get('uploaded_file')
    special_info = st.session_state.get('special_info')

    if uploaded_file is None or special_info is None:
        st.error("챗봇 페이지로 이동하기 위해서는 입력 페이지에서 정보를 입력해야 합니다.")
        return

    # 챗봇과의 대화창
    chat_input = st.text_input("대화 입력:")

    if st.button("전송"):
        # 대화 로직 구현 (여기서는 간단한 예시)
        st.write(f"챗봇: {generate_response(chat_input, uploaded_file, special_info)}")

    # 상대방 정보 요약
    st.write("상대방 정보 요약:")
    st.write("특별한 정보:", special_info)

    # 연애 팁
    st.write("연애 팁: 여기에 연애 팁을 제공합니다.")

    # 데이트 코스 추천 버튼
    if st.button("데이트 코스 추천"):
        st.write("여기에 데이트 코스 추천 정보를 제공합니다.")

    # 대화 내용 평가 버튼
    if st.button("대화 평가"):
        st.write("여기에 대화 평가 정보를 제공합니다.")

# 챗봇 응답 생성 함수 (예시)
def generate_response(user_input, uploaded_file, special_info):
    # 여기에 챗봇의 응답 생성 로직을 구현
    return "이것은 예시 응답입니다."