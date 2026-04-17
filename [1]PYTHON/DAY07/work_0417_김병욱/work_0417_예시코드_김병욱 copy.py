# ======================================
# 29장 함수 사용하기
# ======================================
# 함수 만들고 호출
def hello():
    print("Hello, world!")
hello()

# 덧셈 함수
def add(a, b):
    # 독스트링
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    print(a + b)
add(1,2)

# 독스트링 호출
print(add.__doc__)

# 함수의 결과를 반환하기
def add(a, b):
    return a+b
x = add(10, 20)
print("\n",x)

# 값 여러개 반환
def add_sub(a, b):
    return a + b, a - b
x, y = add_sub(10, 20)
print(x,y)

x = add_sub(10, 20)
print(x)

# 값 여러 개를 직접 반환하기
def one_two():
    return [1, 2]
x, y = one_two()
print(x, y)

# 
def mul(a, b):
    c = a * b
    return c
 
def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)
 
x = 10
y = 20
add(x, y)

# ===============================================
# 30장. 함수에서 위치 인수와 키워드 인수 사용하기
# ===============================================
# 언패킹 사용하기
x = [10, 20, 30]
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
print_numbers(*x)
print_numbers(*[10, 20, 30])

# 고정 인수와 가변 인수를 함께 사용하기
def print_numbers(a, *args):
    print(a)
    print(args)
print_numbers(1)
print_numbers(1, 10, 20)
print_numbers(*[10, 20, 30])

# 키워드 인수와 딕셔너리 언패킹 사용하기
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x) # 키/값
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
personal_info(*x) # 키만

# 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
def personal_info(name, **kwargs):
    print(name)
    print(kwargs)
personal_info('홍길동')
personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# 위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args, **kwargs):
    print(*args, **kwargs)
custom_print(1, 2, 3, 4, 5, sep=':', end='')

# 매개변수에 초깃값 지정하기
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info('홍길동', 30,"\n")
personal_info('홍길동', 30, '서울시 용산구 이촌동')
