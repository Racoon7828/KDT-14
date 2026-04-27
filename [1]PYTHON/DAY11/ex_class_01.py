# ===============================================
# 클래스 / 객체 / 인스턴스
# ===============================================
# -> 클래스 : 특정 데이터에 대한 속성과 기능을 묶어서 정의한 것
#            새로운 사용자 정의한 데이터 타입 
# -> 객  체 : 클래스를 기반으로 메모리 힙영역에 저장된 데이터들
# -> 인스턴스 : 힙영역에 있는 객체들 하나하나를 의미
# ===============================================
# 클래스 목적 : 자동차 관련 데이터를 저장하는 타입
# 클래스 이름 : Car
# 클래스 속성 : width, height, length, color, kind, number, owner
# 클래스 기능 : forward() 
#           : backward()
#           : stop()
# ===============================================
class Car:
    ## 자동차 인스턴스/객체를 생성 위한 메모리 힙 영역 스캔 후 메모리 할당 메서드
    ## 메모리 힙 영역 생성된 자동차 인스턴스/객체 주소 반환
    # - cls : 클래스 정보
    # - owner, number : 인스턴스 생성 시 전달 데이터
    # def __new__(cls, owner, number):
    #     print("(1) __new__ Method create an instance!!")
    #     new_instance = super().__new__(cls)
    #     # new_instance = int(str(new_instance).split()[-1][:-1], base=16)
    #     print("new_instance =>" , new_instance)
    #     return new_instance

    # 자동차 인스턴스/객체를 생성 및 초기화 해주는 매직 메서드
    # 파이썬 시스템에서 자동 호출 실행됨!!
    def __init__(self, owner, number):
        self_value =  int(str(self).split()[-1][:-1], base=16)
        print("(2) __init__() => self : ", self_value) 
        self.owner = owner
        self.number = number

    # 자동차만이 가진 기능 함수 즉, 메서드
    # 메모리 힙영역에 자동차 인스턴스/객체 생성이 되어야만 사용할 수 있는 메서드
    def forward(self):
        print("forward 호출")
        print(f"{self.number}번호 자동차가 앞으로 전진한다")

    def backward(self):
        print("backward 호출")
        print(f"{self.number}번호 자동차가 뒤로 후진한다")
    
    def stop(self, where):
        print("stop 호출")
        print(f"{self.owner}의 자동차가 {where}에서 정지한다")
    
# -----------------------------------------------
# 객체 즉, Car 인스턴스 생성 : 변수명 = 클래스이름()
# -> 생성자 메서드 : 클래스 이름() ==> __init__()
# -----------------------------------------------
myCar = Car("홍길동", "12가 1212")
yourCar = Car("마징가", "70아 9900")
print(f"myCar id => {id(myCar)}, yourCar id => {id(yourCar)}")

# 자동차 인스턴스의 메서드 사용
myCar.forward()
yourCar.backward()
myCar.stop("운동장")

# 자동차 인스턴스/객체의 속성 읽기
print("나의 자동차 번호 : ", myCar.number)
print("나의 자동차 소유자 : ", myCar.owner)

# 자동차 인스턴스/객체의 속성 변경
myCar.owner = "김철수철수"
print("나의 자동차 소유자 : ", myCar.owner)
