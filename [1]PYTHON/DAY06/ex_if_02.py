# # 제어문(조건문/반복문) 연산자 - [1] 
# 조건문 : 조건에 맞는 코드 실행 문법
# 반복문 : 조건에 따라 특정 코드 반복 실행 여부 결정 문법
# -> 조건 1개 이상
# 모든 조건을 만족하는 경우
# 일부 조건을 만족하는 경우
# and, or, not => 결과 True/False

# ex) 조건 1개
# 점수가 60 이상 이면 합격 출력
# grade = 60
# 입력 데이터 좌우공백 제거 후 저장 + int 형변환
grade = input("점수 입력: ").strip()
if grade.isdecimal():
    grade = int(grade)
    if grade >= 60: print("합격")
    else: print("불합격")
else: print("정수 입력")

# 입력된 데이터가 있고, 그 데이터가 숫자인 경우만 출력
# 입력된 내용이 없거나 올바른 데이터가 아닙니다.
# 연산자 : 조건 모두 만족/True => and 
if len(grade) and grade.isdecimal():
    grade = int(grade)
    if grade >= 60: print("합격")
    else: print("불합격")
else: print("정수 입력")

# ex) 조건 여러개
# 점수가 60 이상이면 성적 출력
if grade >= 60: print("D")
elif grade >= 70: print("C")
elif grade >= 80: print("B")
elif grade >= 90: print("A")
else: print("불합격")
