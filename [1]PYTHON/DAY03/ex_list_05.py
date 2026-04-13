# 컨테이너 자료형 - [1] list
# List 전용 메서드 : List 자료형에서만 사용 가능한 함수
# List객체 변수명.메서드명()

datas = list(range(1,11)) # range -> list 형변환
print(datas, len(datas), "\n")

# List 전용 함수 (메서드 사용)
# 원소/요소 추가 -> 마지막 : 변수명.append()
datas.append(100)
print(f"datas 원소 개수 : {len(datas)}개, {datas}")
datas.append(-5)
datas.append(100)

# 원소/요소 추가 -> 위치설정 : 변수명.insert()
datas.insert(0,55)
print(f"datas 원소 개수 : {len(datas)}개, {datas}")
datas.insert(-1,85)
print(f"datas 원소 개수 : {len(datas)}개, {datas}")

# 원소/요소 개수 확장 -> 마지막 : 변수명.extend()
# 반복가능타입/Iterable : for ~ in 가능한 타입 (인덱스 있는 타입들 해당됨)
datas.extend([15,25,35])
# a = [20,30]
# datas.extend(a)
print(f"datas 원소 개수 : {len(datas)}개, {datas}")

# 원소/요소 뒤집기 -> 변수명.reverse() 정렬 X
datas.reverse()
print(f"datas 원소 개수 : {len(datas)}개, {datas}")

# 원소/요소 정렬 -> 변수명.sort() 원소값 비교 후 위치 다시 설정
datas.sort() # 오름차순
print(f"datas 원소 개수 : {len(datas)}개, {datas}")
datas.sort(reverse=True) # 내림차순
print(f"datas 원소 개수 : {len(datas)}개, {datas}")

# 원소/요소 삭제 -> 변수명.remove() 
# 첫번째 발견된 데이터값 삭제 (모두 삭제 X)
# 없을 경우 Error
if 100 in datas:
    datas.remove(100)
elif 13 in datas:
    datas.remove(13)
print(f"datas 원소 개수 : {len(datas)}개, {datas}")

# 원소/요소 삭제 -> 변수명.pop()
# 마지막 또는 특정 인덱스 꺼내기
# 꺼낸 요소 데이터 반환
datas.pop()
datas.pop(0)
print(f"datas 원소 개수 : {len(datas)}개, {datas}")

# 원소/요소 삭제 -> 변수명.clear()
# 빈 리스트 반환
del datas[10:]
print(f"datas 원소 개수 : {len(datas)}개, {datas}")
datas.clear()
print(f"datas 원소 개수 : {len(datas)}개, {datas}")
