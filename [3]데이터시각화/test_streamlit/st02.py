# 소스코드가 입력된 순서대로 문서가 만들어진다
import streamlit as st, pandas as pd

st.header('버튼 누르면 갱신')

# 페이지 로딩과 상관없이 변수를 유지시키고 싶으면 sessin_state.변수명 => 저장
if 'count' not in st.session_state:
    st.session_state.count = 0

# 버튼을 누를 때마다 출력 숫자 증가
if st.button('버튼'):
    st.session_state['count'] += 1

st.write(st.session_state.count)























