# 컨테이너 자료형 - [3] string
# 산술 연산자
# str + str => str 연결
# str * int => str 반복
msg = "집에 가고 싶다."
year = "2026!!"

# str과 산술 연산자 : 덧셈
print(msg + " " + year)

# str과 산술 연산자 : 곱셈
print(msg * 5)

# str과 멤버 연산자 : in
print(str("2") in year)
print(str("2026") in year)
