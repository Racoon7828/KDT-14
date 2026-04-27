## ===========================================================
##                  객체지향프로그래밍 언어 -> 파이썬
## -> 모든 데이터 관련 자료형 --- 클래스
## -> 객체지향언어 특징      --- 정보은닉, 다형성, 상속 
## ===========================================================
## -> 정보은닉 특징
##  [기본] 속성과 메서드를 숨기기/감추기
##         공개용 속성과 메서드 따로 존재
## -> 숨겨진 속성을 사용 방법 : getter/setter 메서드
## 
## ===========================================================
class Car:
    # 자동차 인스턴스/객체를 생성 및 초기화 해주는 매직 메서드
    def __init__(self, owner, number, ckey):
        self.owner = owner
        self.number = number
        self.__ckey = ckey ## 비공개 속성 저장 클래스 내에서만 사용가능

    def forward(self):
        print("forward 호출")
        print(f"{self.number}번호 자동차가 앞으로 전진한다")
        print(f"cKey => {self.__ckey}")

    # Getter/Setter 메서드 : 비공개 속성의 외부 접근 가능 메서드
    def get_ckey(self):
        return self.__ckey
    
    def set_ckey(self, nkey):
        self.__ckey = nkey
    
# -----------------------------------------------
# 객체 즉, Car 인스턴스 생성 : 변수명 = 클래스이름()
# -> 생성자 메서드 : 클래스 이름() ==> __init__()
# -----------------------------------------------
myCar = Car("홍길동", "12가 1212", "998877")

# 자동차 인스턴스의 메서드 사용
myCar.forward()

# 자동차 인스턴스/객체의 속성 읽기
print("나의 자동차 번호 : ", myCar.number)
print("나의 자동차 소유자 : ", myCar.owner)
# print("나의 자동차 키 : ", myCar.__ckey) # 비공개 속성으로 클래스 밖에서 사용 X
print("나의 자동차 키 : ", myCar.get_ckey())

# 자동차 인스턴스/객체의 속성 변경
myCar.owner = "김철수철수"
print("나의 자동차 소유자 : ", myCar.owner)

# myCar.__ckey = "111111" # 새로운 __ckey 변수 생성됨
# print("나의 자동차 키 : ", myCar.__ckey)

myCar.set_ckey("775533") # 비공개 속성 변수값 변경됨
print("나의 자동차 키 : ", myCar.get_ckey())
print(myCar.__dict__)




