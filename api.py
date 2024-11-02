import streamlit as st
import re

def convert_time_period(period, hour):
    hour = int(hour)
    if period == "오후": 
        if hour != 12: hour += 12
    elif period == "오전":
        if hour == 12:
            hour = 0
    return f"{hour:02d}"

def reformat_line(line):
    pattern = r"(\d{4})년\s+(\d{1,2})월\s+(\d{1,2})일\s+(오전|오후)\s+(\d{1,2}):(\d{2}),\s+(.+?):\s+(.*)"
    match = re.match(pattern, line)
    if match:
        year, month, day, period, hour, minute, user, message = match.groups()
        month = f"{int(month):02d}"
        day = f"{int(day):02d}"
        hour_24 = convert_time_period(period, hour)
        time_24 = f"{hour_24}:{minute}"
        new_date_time = f"{month}/{day}:{time_24}"
        new_line = f"{new_date_time}:{user}:{message}"
        return new_line
    elif line.strip() == "":
        return None
    elif "저장한 날짜" in line:
        return None
    else:
        return line

# return value : string
# 카카오톡 대화 정보 > 글자수 줄이기
def parse(input) :
    transformed_lines = []
    text= input.getvalue().decode("utf-8")
    name = None
    for line in text.split('\n'):
        reformatted = reformat_line(line)
        if reformatted is None: continue
        if "님과 카카오톡 대화" in reformatted:
            name = reformatted.split("님과 카카오톡 대화")[0]
        else:
            transformed_lines.append(reformatted)
    return name, '\n'.join(transformed_lines)

# 상대방 정보를 특정할 수 있는 string 반환
def make_persona(uploaded_file, special_info):
    pass

# return value : string
# state keys() : ['uploaded_file', 'special_info', 'persona', 'name']
# 상대방 정보 요약
def summarey(state):
    pass

# return value : string
# state.keys() : ['uploaded_file', 'special_info', 'persona', 'name']
# Using RAG model
def date_course(state):
    pass

# return value : string
# state.keys() : ['uploaded_file', 'special_info', 'persona', 'name']
# 현재 대화에 대한 평가
def evaluate(state):
    pass

# return value : string
# state.keys() : ['uploaded_file', 'special_info', 'persona', 'name']
# 상대방에 맞춤 연애 팁 제공
def tips(state):
    pass
