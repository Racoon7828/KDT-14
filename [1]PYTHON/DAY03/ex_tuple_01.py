# 컨테이너 자료형 - [2] tuple
# 읽기 전용 리스트
# 데이터 변경 불가
# Tuple 생성
# 변수명 = (1,2,...)
# 변수명 = 1,2,...
# 변수명 = 1, -> 데이터 하나 일 경우 쉼표(,) 붙이기
datas = "2026-01-01", "홍길동", 10
print(f"데이터 : {datas}, 타입 : {type(datas)}, 원소 수 : {len(datas)}")
datas = ("홍길동")
print(f"데이터 : {datas}, 타입 : {type(datas)}, 원소 수 : {len(datas)}")
datas = ("홍길동",)
print(f"데이터 : {datas}, 타입 : {type(datas)}, 원소 수 : {len(datas)}", "\n")

# Tuple과 연산자
# 산술 연산자 : +, * => 새로운 Tuple 반환
print(datas + datas)
print(datas * 3, "\n")

# 멤버 연산자 : in
print("홍길동" in datas)
print("홍길동" not in datas)