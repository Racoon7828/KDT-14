# 컨테이너 자료형 - [1] list
# List와 연산자

# List 생성
# 1~100 범위에서 7의 배수로만 구성된 데이터
datas = list(range(7,101,7)) # range -> list 형변환
print(datas, len(datas), "\n")

# 산술 연산자 : list + list => new list
new_datas = datas + datas
print("new_datas:", new_datas, len(new_datas), "\n")

# 연산자 : list - list => 지원안함
# TypeError

# 산술 연산자 : list * int => list list list ... (새로운 리스트 반환)
new_datas = datas * 3
print("new_datas:", new_datas, len(new_datas), "\n")

# 멤버 연산자 : 데이터 in list => 데이터가 list에 존재 여부
# 불 타입 결과 값
print(f"8 in datas => {8 in datas}")
print(f"7 in datas => {7 in datas}")

# 멤버 연산자 : 데이터 not in list => 데이터가 list에 존재 여부
# 불 타입 결과 값
print(f"8 not in datas => {8 not in datas}")
print(f"7 not in datas => {7 not in datas}", "\n")

# 