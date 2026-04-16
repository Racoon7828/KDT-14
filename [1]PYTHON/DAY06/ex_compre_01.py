# 컴프리헨션(Comprehension])
# 반복문 + 조건문 => 컨테이너 자료형 생성
# [형식1] 반복문으로 컨테이너 자료형 생성
# [ 원소 for 원소 in 반복가능한자료형]
# oreList의 원소에 3을 곱한 값으로 새로운 리스트 생성
orgList = [1,2,3]
newList = []
for num in orgList:
    newList.append(num*3)

# 컴프리헨션
newList = [i*3 for i in orgList]
print(newList)