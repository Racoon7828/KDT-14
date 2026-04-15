# 컨테이너 자료형 - [4] Dictionary
# 다양한 dict 데이터 생성 방식
# 유용한 내장 함수 zip() : 같은 위치에 있는 데이터를 하나로 묶어주는 기능
names = ["홍", "박", "김"]
jumsu = [98,100,77]

# 반복 가능한 데이터들을 묶음 처리
result = zip(names, jumsu, range(3))
print(f"result: {result}, {type(result)}")

# 보기 방식으로 형변한 필요
result = list(result)
print(f"result: {result}, {type(result)}")

result = tuple(result)
print(f"result: {result}, {type(result)}")

# dict는 2개 까지
result = zip(names, jumsu)
result = dict(result) 
print(f"result: {result}, {type(result)}")
