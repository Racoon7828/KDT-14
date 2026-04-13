# 표준 입/출력
# 입력합수 : input()
# 출력함수 : print()

# print() 출력함수
# 1. 데이터 1개 출력 : print(data) / 데이터+"\n"
print("Good Luck", end="")

# 2. 여러개 출력 : print(데이터1, 데이터2, ...)
#                       데이터1+""+데이터2+""+"\n"
print("Good Luck", 2026, "Happy")
print("Good Luck", 2026, "Happy", sep="|")

# 3. 데이터 원소가 10게
data=range(10)
print(data, len(data), " 개", sep="")

# 4. 출력형태 data : 10개
print("data : ", len(data), "개", sep="")
print(f"data : {len(data)}개", "\n")

# input("입력조건 문자열 프롬프트") 입력함수
# 반환값 = str . 반드시 저장 필요
# 엔터기를 입력시 모든 입력값 전달
# 1. 문자열 입력 받고 저장
# name = (input("이름: "))
# print(f"당신의 이름은 {name}이군요!")

# 2. 숫자 입력 받고 저장
age = int(input("나이: "))
# print(f"당신의 나이는 {age}세이군요.")
print(f"{age+age}")
