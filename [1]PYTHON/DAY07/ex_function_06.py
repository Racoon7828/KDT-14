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
def getGrade(**jumsu):
    grade = 0
    for i in jumsu.values():
        grade += i
    avg = grade/len(jumsu) if len(jumsu) else 0
    # return avg
    return "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"  
print(f"getGrade()                               : {getGrade()}")
print(f"getGrade(kor=90, dance=100)              : {getGrade(kor=90, dance=65)}")
print(f"getGrade(sci=100,art=99,com=89,life=100) : {getGrade(sci=100,art=99,com=89,life=100)}")

## =================================================
## 가변인자 매개변수 함수
## -------------------------------------------------
## -> 매개변수 이름 : *변수명
## -> 매개변수 개수 : n개
## =================================================
## 함수기능 : 0 ~ n개의 정수를 전달받고 덧셈 후 결과 반환
## 함수이름 : addInt
## 매개변수 : 고정 X,  0개, 1개, .... n개
## 함수결과 : total
## =================================================
def addInt(*nums): return sum(nums)
print(f'addInt() : {addInt(1,2,3,4,5)}')

# 함수 호출 시 전달되는 아규먼드/인수 : *변수명 => 언패킹해서 전달
data =[11,22,33,44,55]
print(f'addInt(11,22,33,44,55) : {addInt(11,22,33,44,55)}')
print(f'addInt(*data) : {addInt(*data)}')

jumsu = {'sci':100,"art":85,"com":80}
print(f"getGrade(sci=100,art=85,com=80) : {getGrade(**jumsu)}")
