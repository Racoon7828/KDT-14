# 컴프리헨션(Comprehension])
# 반복문 + 조건문 => 컨테이너 자료형 생성
# [형식1] 반복문으로 컨테이너 자료형 생성
# [ 원소 for 원소 in 반복가능한자료형 if 조건식]
# oreList의 짝수 값으로 새로운 리스트 생성
orgList = [1,2,3,4,5,6,7,8]

newList = []
for num in orgList:
    if not num % 2:
        newList.append(num)
print(newList)

# 컴프리헨션
newList = [num for num in orgList if not num%2]
print(newList)

# [ 원소 if 조건 else 원소 for 원소 in 반복가능한자료형]
# oreList의 짝수 값 * 3, 홀수 값은 그대로 새로운 리스트 생성
for num in orgList:
    if not num % 2:
        newList.append(num*3)
    else: newList.append(num)
print(newList)

# 컴프리헨션
newList = [num*3 if not num%2 else num for num in orgList]
print(newList)

# [원소 if 조건 else 원소 for 원소 in 반복가능한자료형 if 조건식]
orgList = range(1,20)
new_list = ["큰수" if num>=10 else num for num in orgList if not num%2]
print(new_list)
