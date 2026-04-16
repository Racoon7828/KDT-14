# 퀴즈
# 13.5.1 올바른것 (c)
# a. if (x==10) 
#   print("10입니다")
# b. if x==10 
#   print("10입니다")
# c. if x==10: 
#   print("10입니다") === O
# d. if x==10: 
# print("10입니다")
# e. if x=10: 
#   print("10입니다")

# 13.5.2 잘못된 부분을 고르세요. (c,j)
# a. x = -20
# c. if x < 0 - X
# d.    print("0 미만입니다")
# f.    if x == -10:
# g.        print("-10입니다")
# i.    if x == -20
# j.    print("-20입니다") - X
# c = 없음, j = 들여쓰기 안함

# 13.5.3 잘못된 if문 고르세요. (a)
# a. if a = b: = X -> a == b
# b. if a > b: 
# c. if a is b: 
# d. if a not b: 
# e. if a != b: 

# 14.5.1 올바른것 (c)
# a. if는 조건식이 만족하지 않을때 실행된다. - X = 만족할때
# b. else의 코드는 조건문이 참일때 실행된다. - X = 거짓
# c. else는 단독으로 사용할 수 없다. - O
# d. else에서 실행되는 코드는 다음 줄에서 들여쓰기를 하지 않아야 한다. - X = 해야한다
# e. if는 항상 else가 있어야한다. - X = 없어도된다

# 14.5.2 잘못된부분 찾기 (b,d)
# a. if x >=10:
# b. print("x에 들어있는 값은") - X = 들여쓰기
# c.    print("10 이상입니다.")
# d. else - X = : 없음
# e.    print("x에 들어있는 값은")
# f.    print("10 미만입니다.")

# 14.5.3 다음 코드의 출력결과를 입력
if not "":
    print(True)
else:
    print(False)
# True

# 14.5.4 if에사 조건식을 여러개 지정하는 방법으로 올바른 것을 모두 고르세요. (b,e)
# a. if x == 10 & y == 20: - X
# b. if x == 10 or y == 20: - O
# c. if x == 10 not y == 20: - X
# d. if x == 10 | y == 20: - X
# e. if x and y: - O

# 14.5.5 출력 결과로 올바른 것
x = 5
if x % 2 ==0:
    print("짝수")
else:    
    print("홀수")
# a. 홀수

# 15.2.1 다음중 설명이 잘못된 것은? (d,e)
# a. elif는 여러번 사용 가능 - O
# b. else는 elif 앞에 올 수 없다. - O
# c. elif는 조건식 지정 가능 - O
# d. elif는 단독 사용 가능 - X = 불가
# e. elif는 항상 else 필요 - X = 안써도 된다

# 15.2.2 출력결과
x = 0
if x == 4:
    print("A")
elif x == 3:
    print("B")
elif x == 2:
    print("C")
elif x == 1:
    print("D")
else:
    print("E")
# e. E

# 연습문제 
# 13.5.2 if 조건문 사용하기
# x의 값이 10이 아닐때 "ok" 출력
x = 8
if x is not 10: print("ok")
if x != 10: print("ok")

# 14.6 필기 시험 점수 80점 이상
# 코딩테스트 통과
# 합격 불합격 출력
written_test = 75
coding_test = True
if written_test >= 80: print('합격')
else:print('불합격')

# 심사문제
# 13.7 온라인 할인 쿠폰 시스템 만들기
# 표준입력 가격(정수), 쿠폰이름
# Cash3000쿠폰 = 3000원 할인
# Cash5000쿠폰 = 5000원 할인
# 쿠폰에 따라 할인된가격
# money, coupon = int(input()), input()
# if coupon == "Cash3000": money -= 3000    
# elif coupon == "Cash5000": money -= 5000
# print(money)

# 14.7 합격여부 판단
# 표준 입력으로 국,영,수,과 점수 입력
# 과목 평균 점수 80점 이상 합격
# 평균점수에 따라 합격 불합격 출력
# 점수 0~100 범위를 벗어나면 "잘못된 점수" 출력
# score = list(map(int, input().split(" ")))
# for i in score:
#     if i > 100 or i < 0:
#         print("잘못된 점수")
#         break
# else:
#     avg = sum(score) / len(score)
#     if avg >= 80:print("합격")
#     else:print("불합격")