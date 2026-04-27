# 클래스 = 객체를 표현하는 문법
# 인스턴스 = 객체
# 보통 객체만을 지칭할때는 객체라고 부른다.
# 클래스와 연관지어 말할때는 인스턴스라고 부른다

# 속성 만들기
# def __init__(self): self.속성 = 값

#  __init__ = 인스턴스(객체)를 초기화

# 비공개 클래스
class Knight:
    __item_limit = 10 # 비공개 클래스
    def __init__(self):
        self.__item = 50 # 비공개 클래스
    
    def print_item_limit(self):
        print(Knight.__item_limit) # 클래스 안에서만 접근가능
    def a(self):
        return self.__item
    def b(self):
        return self.__item_limit

x = Knight()
x.print_item_limit()
# print(Knight.__item_limit) #
# print(Knight.__item) #
print(x.a()) # 비공개도 함수로 리턴해주면 얻을 수 있다
print(x.b())

# @property = 사용자가 메서드인지 모르게 변수처럼 쓸 수 있게 해줌
# 코드 유지보수 및 가독성 축면에서 우수
class Car:
    def __init__(self, ckey):
        self.__ckey = ckey       ## 비공개 속성 저장. 클래스 내에서만 사용 가능
    @property
    def get_ckey(self):       return self.__ckey
    
    @get_ckey.setter
    def set_ckey(self, nkey): self.__ckey = nkey

# @ 없을시
# obj.set_ckey(100)      # 값을 넣을 때
# print(obj.get_ckey())  # 값을 읽을 때 (항상 괄호 필요)

# obj = Car(10) 
# obj.ckey = 20    # 메서드 호출이 아니라 변수 대입처럼 보안다
# print(obj.ckey)  # 괄호 없이 변수처럼 읽을 수 있음

# 정적 메서드 
# 인스턴스 사용하지않고 바로 호출가능
# @staticmethod
# def 메서드(매개변수1,매개변수2):코드

# *메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수를 만들때 사용
class Calc:
    @staticmethod
    def add(a,b): print(a+b)
    @staticmethod
    def mul(a,b): print(a*b)
# 클래스에서 바로 메서드 호출
Calc.add(10,20)
Calc.mul(10,20)

# 클래스 메서드
# @classmethod
# def 메서드(매개변수1,매개변수2):코드
# 인스턴스 사용하지않고 바로 호출가능
# 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용
# cls() = Person() / 클래스
class Person:
    count = 0
    def __init__(self,c):
        Person.count += 1
        self.c = c
    
    @classmethod
    def print_count(cls):
        print(f'{cls.count}명 생성되었습니다')
    
    @classmethod
    def create(cls):
        p = cls(1)
        return p
    
    def add(a,b): print(a+b)
    def mul(self, b): print(self.c + b)

james = Person(1)
maria = Person(1)
john = Person(3)

Person.print_count()
print(Person.count)

a = Person.create()
Person.print_count()
Person.add(3,5) # __init__ 안거침
john.mul(5) # __init__ 거침
print(Person.count)
print(a)