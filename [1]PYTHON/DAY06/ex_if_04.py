# # 제어문(조건문/반복문) 연산자 - [1] 
# 조건문 : 조건에 맞는 코드 실행 문법
# 반복문 : 조건에 따라 특정 코드 반복 실행 여부 결정 문법
# -> 조건 1개 이상
# 모든 조건을 만족하는 경우
# 일부 조건을 만족하는 경우
# and, or, not => 결과 True/False

# 점수가 60 이상 이면 합격 출력
grade = 60
if grade >= 60: print("합격")
else: print("불합격")

# ex) 짝수 & 홀수 판별 출력
# 숫자 %2 나머지 ==> 2의 배수 0, 2의 배수가 아닌경우 1
num = 4
if num % 2 == 0: print(f"{num} = 짝수")
else: print(f"{num} = 홀수")
if not num % 2 == 1: print(f"{num} = 짝수")
else: print(f"{num} = 홀수")