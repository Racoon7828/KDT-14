# 컨테이너 자료형 - [4] Dictionary
# 다양한 dict 추가 메서드 살펴보기
# dict에 원소/요소 추가 메서드 => 형태: 키와 값 쌍으로 추가
# setdefault()
# update()
# ex)
stdDict = {"홍":3.9,"마":4.1,"권":2.7}

# 1. 원소 추가하기
stdDict.setdefault("박")
print(f"{len(stdDict)}개, {stdDict}")
stdDict.setdefault("베", 3.3)
print(f"{len(stdDict)}개, {stdDict}")

# 존재하는 키 추가시 추가되지 않음
stdDict.setdefault("베", 4.3)
print(f"{len(stdDict)}개, {stdDict}")

# 2. 원소 추가하기
# 존재하지 않는 키 추가, 여러개 가능
# * 키가 str 타입만 가능. str 타입이지만 "", '' 감싸지 않음 => 함수 문법 규칙에 맞춤
stdDict.update(K=2.9, P=3.1, C=4.0)
print(f"{len(stdDict)}개, {stdDict}")

# dict 형식으로 추가
stdDict.update({"A":1.3, "Z":3.9})
print(f"{len(stdDict)}개, {stdDict}")

# 키와값 형식으로 추가
stdDict.update([["김",3.2],["이",4.4]])
print(f"{len(stdDict)}개, {stdDict}")

# zip 형식으로 추가
stdDict.update(zip(["최","제갈","남궁"],[3.0,2.9,2.8]))
print(f"{len(stdDict)}개, {stdDict}")

# 값 변경 update()
stdDict.update(홍=2.9)
stdDict.update(zip(["최","제갈","사공"],[2.0,3.9,3.8]))
print(f"{len(stdDict)}개, {stdDict}")

# dict 원소 삭제
# 키 원소 값 반환 pop()
# 삭제 del x[]
value = stdDict.pop('홍')
del stdDict["박"]
print(f"{len(stdDict)}개, {stdDict}\n꺼낸 원소값: {value}")

# 마지막 원소 (키,값) 반환 popitem() - 파이썬3.5 이하 임의값
value = stdDict.popitem()
print(f"{len(stdDict)}개, {stdDict}\n꺼낸 원소값: {value}")

# 모두 삭제
# stdDict.clear()
