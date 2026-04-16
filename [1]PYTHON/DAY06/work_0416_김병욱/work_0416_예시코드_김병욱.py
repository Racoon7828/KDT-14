# if 조건문 사용 주의할 점
# 비교값은 ==
x = 10
if x == 10:
    pass # 코드 생략

# 들려쓰기 잘하기 - tap

# 중첩 if문
x = 15
if x >= 10: 
    print("10 이상")
    if x >= 15: print("15 이상")
    if x >= 20: print("20 이상")

# else 사용
x = 5
if x == 10: print('10입니다.')
else: print('10이 아닙니다.')

# 조건부 표현식
x = 10
y = x if x == 10 else 0
print(y)

