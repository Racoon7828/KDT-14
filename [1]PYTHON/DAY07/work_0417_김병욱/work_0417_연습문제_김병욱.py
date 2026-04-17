# 퀴즈
# 29.6.1 매개변수가 없는 hello 함수를 호출하는 방법으로 올바른 것을 고르세요. (c)
# a. def hello
# b. hello
# c. hello()
# b. hello[]
# b. def hello:

# 29.6.2 올바른 코드를 고르세요. (d)
# a. def mul(): a*b
# b. def mul(a,b): a*b
# c. mul(a,b): return a*b
# d. def mul(a,b): return a*b
# e. mul(a,b): return a*b

# 29.6.3 올바른 코드를 고르세요. (a,c,d)
# a. def three(): return 1,2,3
# b. def three(): 
#       return 1
#       return 2
#       return 3
# c. def three(): return (1,2,3)
# d. def three(): return [1,2,3]
# e. def three(): return 1, return 2, return 3

# 30.5.1 함수를 def print_numbers(a,b,c):처럼 만들었을때 호출하는 방법으로 잘못된것 (d)
# a. print_numbers(1,3,5)
# b. print_numbers(a=1,b=3,c=5)
# c. a = [5,0,2]
#    print_numbers(*a)
# d. a = [3,7,9]
#    print_numbers(**a)
# e. print_numbers(*[9,1,2])

# 30.5.2 print_numbers(*[10,20,30])으로 호출할 수 있는 함수로 올바른 것 (b,c)
# a. def print_numbers(args):
# b. def print_numbers(a,b,c):
# c. def print_numbers(*args):
# d. def print_numbers(**kwargs):
# e. def print_numbers():

# 30.5.3 personal_info(**{'name':"홍길동", "age":30})으로 호출할 수 있는 함수로 올바른 것 (a,c)
# a. def personal_info(**kwargs)
# a. def personal_info(*args)
# a. def personal_info(name="미공개", age=0)
# a. def personal_info(name, address)
# a. def personal_info(kwargs)

# 연습문제
# 29.7 x / y 몫 출력
x = 10
y = 3
def get_quotient_remainder(x, y):
    return x // y, x % y
quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
# 몫: 3, 나머지: 1

# 30.6 가장 높은 점수를 구하는 함수
kor, eng, math, sci, = 100, 86, 81, 91
def get_max_score(*args):
    return max(*args)
max_score = get_max_score(kor,eng,math,sci)
print(f'높은 점수: {max_score}')

max_score = get_max_score(eng,sci)
print(f'높은 점수: {max_score}')

# 심사문제
# 29.8 사칙 연산 함수 만들기
# 표준 입력 숫자 두개 입력.
# 두 숫자의 덧셈, 뺄셈 곱셈. 나눗셈의 결과가 출력되게 만드세요
# 나눗셈의 결과는 실수
# def calculator():
#     num1,num2 = map(int, input().split())
#     print(f"덧셈: {num1+num2}, 뺄셈: {num1-num2}, 곱셈: {num1*num2}, 나눗셈: {num1/num2}")
# calculator()

def calculator(x,y):
    x, y = map(int, input().split())
    return x+y, x-y, x*y, x/y
a,s,m,d = calculator(x,y)
print("덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}".format(a,s,m,d))

# 30.7 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
# 표준입력 : 국,영,수,과
# 가장 높은 점수,가장 낮은 점수, 평균점수(실수) 출력

kor, eng, math, sci, = map(int, input().split())
def get_min_max_score(*jumsu):
    return min(*jumsu), max(*jumsu)

def get_average(**jumsu):
    total = 0
    for i in jumsu.values():
        total += i
    return total/len(jumsu)

min_score, max_score = get_min_max_score(kor,eng,math,sci)
average_score = get_average(kor=kor,eng=eng,math=math,sci=sci)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score,max_score,average_score))

min_score, max_score = get_min_max_score(eng,sci)
average_score = get_average(eng=eng,sci=sci)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score,max_score,average_score))
    