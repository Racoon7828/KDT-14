#===========================================
# 시리즈 인스턴스 생성
#===========================================
# pandas에서 1줄 데이터를 저장하는 데이터 타입
# 구성 : 원소 식별 인덱스 + 데이터
# 함수 : Series(data, index, dtype)
#===========================================
# [1] 모듈로딩 
#===========================================
import pandas as pd

# [2] Series 객체 생성
# 데이터 준비
data1 = [11,33,55,77]

# [3] Series 인스턴스 생성
sr1 = pd.Series(data1, index=["a", "b", "c", "d"], dtype='int8', name="data")

# [4] 인스턴스 정보 확인 / 현재 속성값 읽기
# 인스턴스/객체 변수명.속성명
print(f"--[Series 속성들]--")
print(f"index : {sr1.index}")   # 원소 식별 번호
print(f"values : {sr1.values}") # 원소에 저장된 데이터들
print(f"shape : {sr1.shape}")   # 1줄 시리즈의 형태 모양. 튜플로 표기
print(f"ndim : {sr1.ndim}")     # 차원 정보
print(f"dtype : {sr1.dtype}")   # 원소의 데이터 타입 정보
print(f"name : {sr1.name}")     # 메타/부가 정보 이름

print(f"\n--[Series 형태 출력]--")
print(f"sr1 : {sr1}")

# 인스턴스/객체 변수명.속성명 = 새 값
sr1.index = ['1개', '2개', '3개', '4개']
sr1.name = "점수"
print(sr1)

# 데이터 값은 직접 접근으로 변경 불가
# sr1.values = [11,22,33,44]







