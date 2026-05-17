import streamlit as st

st.title('st.session_state')

import streamlit as st

# 1. 초기값 설정 (Key 에러 방지)
if "geun" not in st.session_state:
    st.session_state["geun"] = 0.0
if "kg" not in st.session_state:
    st.session_state["kg"] = 0.0

# 2. 변환 로직 함수들
def geun_to_kg():
    # 근 -> kg (1근 = 0.6kg 가정)
    st.session_state["kg"] = st.session_state["geun"] * 0.6

def kg_to_geun():
    # kg -> 근
    st.session_state["geun"] = st.session_state["kg"] / 0.6

def sb_to_all():
    # 슬라이더(sb_kg) 값을 kg와 근에 동기화
    val = st.session_state["sb_kg"]
    st.session_state["kg"] = float(val)
    st.session_state["geun"] = val / 0.6

# 3. UI 구성
# 근 입력
st.number_input("근 (Geun):", key='geun', on_change=geun_to_kg)

# kg 입력
st.number_input("kg:", key='kg', on_change=kg_to_geun)

# 슬라이더 (kg 기준)
st.slider('kg 조절 슬라이더', 0.0, 100.0, key='sb_kg', on_change=sb_to_all)

# 결과 출력
st.write(f"현재 설정된 무게: **{st.session_state['kg']:.2f} kg** / **{st.session_state['geun']:.2f} 근**")
