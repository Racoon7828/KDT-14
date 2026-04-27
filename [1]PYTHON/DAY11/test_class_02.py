## ==================================================
# 사용자 정의 클래스
## ==================================================
## --------------------------------------------------
# 사람 클래스 정의 : 세상 모든 사람의 속성과 기능
## --------------------------------------------------
# -> 데이터 : 국적, 성별, 키, 몸무게, 이름, 나이, 혈액형
# -> 기능/역활 : 먹는다, 잔다, 논다, 개인정보출력
## --------------------------------------------------
# 클래스이름 : Human
# 클래스속성 : 
# 클래스기능 : 
## --------------------------------------------------
class Human:
    nationality = "Korean"
    def __init__(self, gender, height, weight, name, age, blood):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.blood = blood
        
    def eat(food):
       pass 

    def sleep(where):
        pass

    def play(item):
        pass

    def show_info():
        pass
    
    def show_health(self):
        bmi = self.weight / (self.height/100)**2
        "비만" if bmi >= 25 else "정상" if bmi >= 16 else "저체중"
        print(bmi)

import random
class Gatekeeper:
    def __init__(self, gender, height, weight, name, age, blood, nationality):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.blood = blood
        self.nationality = nationality

    def mission():
        # 랜덤 미션 출력
        pass
        
    def gatekeeping():
        # 여권받고
        pass

    def menu():
        # 터미널 출력
        pass
