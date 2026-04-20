# 32장
# 람다 표현식
print(lambda x:x+10)
x = lambda x:x+10
print(x(1))
print((lambda x:x+10)(1))
# 람다 표현식 안에선 변수 생성 불가
# 외부 변수는 사용가능
y=10
print((lambda x:x+y)(1))

# 조건부 표현식 사용
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:str(x) if x % 3 == 0 else x, a)))

# map() 반복 가능한 객체(Iterable)의 모든 요소에 특정 함수를 일괄적으로 적용
# map(함수, 반복가능개체)
# map에 여러 객체 넣기
a = [1,2,3,4,5]
b = [2,4,6,8,10]
# 두 리스트 요소를 곱해서 새 리스트로 만들기
print(list(map(lambda x,y: x * y, a, b)))

# filter() 사용하기
# filter() = 지정한 함수의 반환값이 True일 때만 해당 요소 가져온다
# filter(함수, 반복가능개체)
a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(lambda x: x > 5 and x < 10, a)))

# reduce() 사용하기
# reduce() = 반복 가능한 객체의 각 요소를 지정된 함수로 처리한후 이전 결과와 누적해서 반환
# 파이썬 3부터 functools 모듈에서 reduce함수를 가져와야 한다.
# reduce(함수, 반복가능개체)
from functools import reduce
a = [1,2,3,4,5]
print(reduce(lambda x, y: x + y, a))

# 33장 - 33.1만
# 변수의 사용 범위
x = 10          # 전역변수
def foo():
    print(x)    # 전역변수 출력
foo()
print(x)        # 전역변수 출력

# 함수안에 전역변수 변경하기
# 일반
x = 10          # 전역변수
def foo():
    x = 20      # x는 foo의 지역변수
    print(x)    # foo의 지역변수 x 출력
foo()
print(x)        # 전역변수 출력

# 함수안에 전역변수 변경
x = 10          # 전역변수
def foo():
    global x    # 전역변수 x 사용 선언
    x = 20      # x는 전역변수
    print(x)    # 전역변수 x 출력
foo()
print(x)        # 전역변수 출력

# 전역변수 X
def foo():
    global a    # a를 전역변수로 선언
    a = 20      # a는 전역변수
    print(a)    # 전역변수 a 출력
foo()
print(a)        # 전역변수 a 출력

