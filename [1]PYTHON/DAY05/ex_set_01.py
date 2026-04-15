# 컨테이너 자료형 - [5] set
# 중복 데이터는 저장되지 않음
# 원소/요소 식별용 인덱스 없음
# 표현방식 : {원소1,원소2,...}
dataSet=set({1,1,1,1,1,1,1,1})
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")

dataSet={1,1,1,1,1,1,1,1,2,3,4}
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")

# 빈 집합 : set()
dataSet = set()
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")

# 산술 연산자 덧셈 + = 미지원
# new_data = dataSet + {11,33,9,7}
# print(f"new_data: {len(new_data)}개, {type(new_data)}, {new_data}")

# 멤버 연산자 - in
dataSet={1,1,1,1,1,1,1,1,2,3,4}
print(f"3 in dataSet: {3 in dataSet}")

# 원소/요소 1개 추가 메서드 : add(데이터)
# 중복 추가 X
dataSet.add(5)
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")

# 원소/요소 여러개 추가 메서드 : update(데이터)
# 중복 추가 X
dataSet.update([9,8,7,6,5,4,3,2,1])
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")
dataSet.update("Gooooood")
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")
dataSet.update(["Gooooood"])
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")


# 원소/요소 삭제 메서드 : remove()
dataSet.remove("Gooooood")
print(f"dataSet: {len(dataSet)}개, {type(dataSet)}, {dataSet}")

# 원소/요소 삭제 메서드 : pop()
dataSet.pop("G")
