# 컴프리헨션(Comprehension])
# 반복문 + 조건문 => 컨테이너 자료형 생성
# set 자료형과 컴프리헨션
# {조건부 표현식 원소 for 원소 in 반복가능한자료형 필터링}
org = {1,2,3,4,5,1,1,2,3,4,5}
new_data = set()
new_data = {num for num in orgList}
print(new_data, type(new_data))

# 짝수만 저장
new_data = {num for num in orgList if num%2==0}
print(new_data)

# 짝수면 *2 홀수면 *3
new_data = { num*2 if num%2==0 else num*3 for num in orgList}
print(new_data)

# 리스트의 원소값이 짝수인 원소만 추가하고
# 그 값이 6미만이면 "작은수"로 저장
# 그 값이 6이상이면 "큰수"로 저장
# 집합자료형 저장
new_data = {"큰수" if num>=6 else "작은수" for num in orgList if num%2==0}
print(new_data)

