# 컨테이너 자료형 - [2] tuple
# 읽기 전용 리스트
# 데이터 변경 불가
# 튜플 전용 메서드
datas = "2026-01-01", "홍길동", "홍길동", 10

# 1. 데이터의 인덱스 반환 함수 : .index(데이터값)
print(datas.index("홍길동"))

# 2. 데이터의 존재 개수 반환 함수 : .count(데이터값)
print(datas.count("홍길동"))
print(datas.count("홍"))