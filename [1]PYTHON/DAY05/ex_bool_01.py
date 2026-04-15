# 기본 자료형 - bool
# 참 / 거짓
# True / False
data1 = False
data2 = True
data3 = bool(False)

print(data1,type(data1))
print(data2,type(data2))
print(data3,type(data3))

# bool자료형과 다른 자료형 사이의 변환
# 형식 : bool(데이터) : 헤딩 데이터를 bool타입으로 변환
# int, float = 0만 False, 나머지 True
# 1. int <-> bool
data1,data2 = -9, 0
print(bool(data1),bool(data2))
print(int(True),int(False))

# 2. str <-> bool : 원소 개수 0개 False, 1개이상 True
data1,data2 = "", " "
print(bool(data1),bool(data2))
print(str(True),str(False))

data1,data2 = "집에 가고 싶다", "언제 끝나노"
