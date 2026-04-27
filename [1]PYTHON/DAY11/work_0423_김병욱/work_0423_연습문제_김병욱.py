# 34장, 35장

# 퀴즈
# 34.4.1 다음 클래스의 greeting 메서드를 호출하기 위한 방법으로 올바른 것을 고르세요. (d)
class Person:
    def greeting(self):
        print("Hello")
# a. Person.greeting()
# b. greeting()
# c. maria = Person 
#    maria.greeting()
# d. maria = Person()
#    maria.greeting()
# e. Person(greeting)

# 34.4.2 클래스로 인스턴스를 만들 때 호출되는 메서드는 무었인가요? (메서드 뒤의 괄호는 생략하고 메서드 이름만 입력) __init__

# 34.4.3 다음과 같이 Person 클래스가 있습니다. 클래스에서 다른 메서드를 만들었을 때 인스턴스 속성 name에 접근하기 위한 방법으로 올바른 것을 고르세요. (e)
class Person:
    def __init__(self, name):
        self.name = name
# a. name
# b. self
# c. Person.name
# d. self[name]
# f. self.name

# 34.4.4 클래스의 메서드 def __init__(self):에서 속성을 만들려고 합니다. 다음 중 비공개 속성을 고르세요. (c)
# a. self.name
# b. self._name
# c. self.__name
# d. self.__name__
# e. self.name__

# 34.4.1 다음 중 클래스 바깥에서 클래스 속성x에 접근하는 방법으로 올바른 것을 고르세요. (a)
class Person:
    x = {}
# a. Person.x

# 34.4.2 정적메서드로 올바른 것을 고르세요 (c)
# c. @staticmethod
#    def div(a,b): print(a/b)

# 34.4.3 다음 중 클래스 메서드에 대한 설명으로 잘못된 것을 고르세요. (c,e)
# c. 클래스 메서드의 첫번째 매개변수는 self이면 현재 인스턴스가 들어온다. => cls 현재 클래스가 들어온다.
# e. 클래스 메서드는 인스턴스 없이 호출할 수 있다. => 없다

# 연습문제
# 34.5 게임 캐릭터 클래스 만들기
# 게임 캐릭터의 능력치와 베기가 출력되게 만드세요.
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print("베기")

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

# 35.5 연습문제: 날짜 클래스 만들기
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31
if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다')
else:
    print('잘못된 날짜 형식입니다')

# 34.6 심사문제 게임 캐릭터 클래스 만들기
class Annie:
    def __init__(self, health, mana, ability_power):
        self.hp = health
        self.mp = mana
        self.ap = ability_power

    def tibbers(self):
        print(self.ap * 0.65 + 400)

# health, mana, ability_power = map(float, input().split())
# x = Annie(health=health, mana=mana, ability_power=ability_power)
# x.tibbers()

# 35.6 시간 클래스 만들기
# 표준 입력 시:분:초
# 시, 분, 초가 출력되도록
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        # 문자열로 인스턴스 만들기
        h, m, s = map(int, time_string.split(':'))
        return cls(h, m, s)
    
    @staticmethod
    def is_time_valid(time_string):
        #문자열이 올바른 시간인지 검사
        h, m, s = map(int, time_string.split(':'))
        return 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 60
    
# time_string = input()
# if Time.is_time_valid(time_string):
#     t = Time.from_string(time_string)
#     print(t.hour, t.minute, t.second)
# else:
#     print("X")

