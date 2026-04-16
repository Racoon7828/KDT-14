# # 제어문(조건문/반복문) 연산자 - 조건부 표현식
# 여러 라인의 if ~ else 구문을 간단하게 처리해주는 문법
# True조건 실행코드 if 조건식 else False조건 실행코드
# ex) 짝수 & 홀수 판별 조건문
num = 8
if num % 2 : print(f"{num}은 짝수")
else: print(f"{num}은 홀수")

print(f'{num}은 짝수') if num % 2 == 0 else print(f'{num}은 홀수')

result = "홀수" if num%2 else "짝수"
print(f"{num}은 {result}")

print(f"{num}은 {"홀수" if num%2 else "짝수"}")

# 음수, 0, 양수 판별 조건문
# 양수 : 데이터 > 0
# 음수 : 데이터 < 0
# 0 : 데이터 == 0
# => 다중조건문
num = 5
result = ""

# 기본 다중조건문
if num>0:print("양수")
elif num<0:print("음수")
else:print("영")

# 기본 다중조건문 : 중복 코드 제거
if num>0:result="양수"
elif num<0:result="음수"
else:result="영"
print(result)

# 다중 조건부 표현식
result = "양수" if num>0 else "음수" if num<0 else "영"
print(result)
