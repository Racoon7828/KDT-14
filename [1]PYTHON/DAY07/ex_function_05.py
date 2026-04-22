## =================================================
## 키워드 파라미터 가변인자 매개변수 함수
## -------------------------------------------------
## -> 데이터 정보와 데이터가 가변인 경우 대비
## -> 매개변수 이름 : **변수명
## -> 매개변수 개수 : 0 ~ n개
## -> 매개변수 형식 : 키1=값, 키2=값, ...
## =================================================
## 함수기능 : 학생의 학점을 출력해주는 기능
##           학생마다 과목 개수와 과목이 다름
## 함수이름 : getGrade
## 매개변수 : **jumsu
## 함수결과 : grade
## =================================================
# def getGrade(**jumsu):
#     grade = 0
#     for i in jumsu.values():
#         grade += i
#     avg = grade/len(jumsu) if len(jumsu) else 0
#     # return avg
#     return "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"  
# print(f"getGrade()                               : {getGrade()}")
# print(f"getGrade(kor=90, dance=100)              : {getGrade(kor=90, dance=65)}")
# print(f"getGrade(sci=100,art=99,com=89,life=100) : {getGrade(sci=100,art=99,com=89,life=100)}")

def getGrade(**jumsu):
    grade = [i for i in jumsu.values()]
    avg = sum(grade)/len(jumsu) if len(jumsu) else 0
    # return avg
    return "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"  

# 해당 파일이 다른 파일에 import 될때는 아래 코드가 실행되지 않음
if __name__ == "__main__":
    print(f"getGrade()                               : {getGrade()}")
    print(f"getGrade(kor=90, dance=100)              : {getGrade(kor=90, dance=65)}")
    print(f"getGrade(sci=100,art=99,com=89,life=100) : {getGrade(sci=100,art=99,com=89,life=100)}")

    print(f"매직/스페셜 변수 __name__ : {__name__}")
