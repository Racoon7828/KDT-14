# 챕터 9, 22
# 퀴즈
# 9.2.1 - 문자열 표현 올바른 것
# b. "Hello, world"
# d. 'Hello, world!'

# 9.2.2 - 문자열 여러줄 올바른 것
# a. '''안녕하세요.
# 파이썬입니다.'''
# c. """안녕하세요.
# 파이썬입니다."""

# 9.2.3 - 문자열 표현 올바른 것
# a. 'Hello, \'Python\''
# c. "Hello, 'Python'"
# d. """"Hello", Python"""

# 22.8.1 - a.append(40)과 동작이 같은것 모두 고르기
# a. a.insert(lne(a), 40)
# d. a[len(a):] = [40]

# 22.8. - 리스트 모든 요소 삭제
# e. clear

# 22.8. - 리스트 a의 모든 요소 출력
# a. for i in range(len(a)):
#     print(a[i])
# d. i = 0
# while i < len(a):
#     print(a[i])
#     i += 1
# e. for i in a:
#     print(a)

# 22.8. - 다음 중 튜플 a에 사용할 수 없는 코드는?
# b. a.pop()

# 22.8. - 리스트 [0,1,2,3,17,18,19]를 만드는 방법으로 올바른것?
# d. [i for i in range(20) if i <= 3 or i >= 17]

# 22.8. - [4.7, 3.5, 2.9]를 문자열로 변환하는 방법으로 옳은것?
# c. a = list(map(str, [4.7, 3.5, 2,9]))

# 연습문제
# 9.3
s = """Python is a programming language that lets you work quickly
and
integrate systems more effectively"""
print(s)

# 22.9 길이가 5인 것들만 리스트 형태로 출력
a = ["alpaha", "bravo", "chalie", "delta", "echo", "foxtrot", "golf", "hotel", "india"]
b = [i for i in a if len(i) == 5]
print(b)

# 심사문제
# 9.4
s = """'Phython' is a "programming language"
that lets you work quickly
and
integrate systems more effectively"""
print(s)

# 22.10
def cal_power():
    user_input1 = int(input(""))
    user_input2 = int(input(""))
    power = []
    if user_input1 > 21: print("1~20 까지 입력하세요")
    elif user_input1 >= user_input2: print("두번째 입력이 더 커야합니다.")
    elif user_input2 > 30: print("1~30 까지 입력하세요")
    else:
        for i in range(user_input1, user_input2+1):
            result = 2 ** i
            i += 1
            power.append(result)
    del power[1]
    del power[-2]
    print(power)
cal_power()