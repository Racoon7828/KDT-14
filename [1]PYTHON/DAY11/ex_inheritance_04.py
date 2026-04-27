## ==========================================================
## 상속(Inheritance)
## -> 다중 상속
## * 파이썬은 다중 상속 허용
## * 형식 : 자식클래스이름(부모클래스1, 부모클래스2, ..., 부모클래스N)
## * 규칙
## - 메서드/속성 사용시 실행규칙
## - (1) 자신의 클래스에서 메서드/속성 찾기
## - (2) 부모클래스1에 존재 X --> 부모클래스1
## - (3) 부모클래스2에 존재 X --> 부모클래스2
## - (3) 부모클래스N에 존재 X --> Error
## ==========================================================
class Animal:
    def hello(self):
        print("안녕 나는 짐승이야")

class Dog(Animal):
    def hello(self):
        print("안녕 나는 개자식이야")

class Cat(Animal):
    def hello(self):
        print("안녕 나는 냥아치야")

## ----------------------------------------------------------
# 인스턴스 생성 및 사용
## ----------------------------------------------------------
# -> 인스턴스 생성
dog = Dog()
cat = Cat()

# -> 부모 - 자식 관계 검사 issubclass(자식,부모)
print(f"issubclass(Dog, Animal) : {issubclass(Dog, Animal)}")
print(f"issubclass(Cat, Animal) : {issubclass(Cat, Animal)}")

print(f"issubclass(Cat, Animal) : {issubclass(Cat, Dog)}")

# 특정 클래스로 생선된 인스턴스 즉, 객체 여부 검사 isinstance(변수명, 클래스이름)
print(f"isinstance(cat, Cat) : {isinstance(cat, Cat)}")
print(f"isinstance(dog, Cat) : {isinstance(dog, Cat)}")

cat.hello()
dog.hello()

class Bear(Dog,Cat):
    pass
    
bear = Bear()
bear.hello()

# __dict__ : 속성, 메서드 추출
print(cat.__dict__)
print(Cat.__dict__)
print(Bear.__dict__)

# 메서드 호출 순서
print(Cat.mro())
print(Bear.mro())





