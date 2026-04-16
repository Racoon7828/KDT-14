# # 제어문(조건문/반복문) 연산자 - [1] 
# 조건문 : 조건에 맞는 코드 실행 문법
# 반복문 : 조건에 따라 특정 코드 반복 실행 여부 결정 문법
# -> 조건 1개 이상
# 모든 조건을 만족하는 경우
# 일부 조건을 만족하는 경우
# and, or, not => 결과 True/False

# ex) 나이가 20살 이상이거나 또는 성별이 여자인 경우
# => 왼쪽으로 이동하세요.
# else => 오른쪽으로 이동하세요.
info = input("나이/성별 입력: ").strip()

# 입력 데이터 존재 여부 체크 : len()
if len(info):
    # 나이 성별 분리
    age, gender = info.split()

    # 나이 성별 조건 검사에 따른 출력
    if age.isdigit() and gender.isalpha():
        # 나이와 성별 조건에 따른 출력
        if int(age) >= 20 or gender == "여자": print("왼쪽으로 가쇼")
        else: print("꺼지슈")
    else:print("나이 / 남자or여자 입력")
else:print("재입력")

# 나이와 성별 조건에 따른 출력
if len(info) and age.isdigit() and gender.isalpha():
    # 나이 성별 분리
    age, gender = info.split()
    # 나이 성별 조건 검사에 따른 출력
    if int(age) >= 20 or gender == "여": print("왼쪽으로 가쇼")
    else: print("꺼지슈")
else:print("재입력")