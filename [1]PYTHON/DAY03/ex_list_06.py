# 컨테이너 자료형 - [1] list
# List 전용 메서드 : List 자료형에서만 사용 가능한 함수
# List객체 변수명.메서드명()

datas = list(range(1,11)) # range -> list 형변환
datas.extend([11,12,13,12,12])
print(datas, len(datas), "\n")

# List 전용 함수 (메서드 사용)
# 원소/요소 인덱스 찾기 -> 변수명.index()
# 첫번째 발견되는 데이터의 인덱스 반환
# 존재하지 않는 데이터의 인덱스 = Error 반환
if 100 in datas:
    datas.index(100)
    print(f"datas의 인덱스 : {datas.index}, {datas}")
else:
    print("100은 존재하는 원소가 아닙니다.")

# 1개만 존재하는 데이터의 인덱스
idx = datas.index(7)
print(f"datas 7의 인덱스 : {idx}, {datas}")

# 여러개 존재하는 데이터의 인덱스
idx = datas.index(12)
print(f"첫번째 datas 12의 인덱스 : {idx}, {datas}")

idx = datas.index(12, idx+1)
print(f"두번째 datas 12의 인덱스 : {idx}, {datas}")

idx = datas.index(12, idx+1)
print(f"세번째 datas 12의 인덱스 : {idx}, {datas}")

# 원소/요소 인덱스 찾기 -> 변수명.count(데이터값)
# 없으면 0 반환
cnt = datas.count(12)
print(f"datas 12의 개수 : {cnt}개, {datas}")

# 매직코드/매직메서드 : 파이썬에서 특수한 기능을 부여햐 놓은 것들
# __ 메서드이름__(), __변수이름__
item = datas.__getitem__(12)
print(f"datas 개수 : {item}개, {datas}")