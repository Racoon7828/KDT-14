# 컴프리헨션(Comprehension])
# 반복문 + 조건문 => 컨테이너 자료형 생성
# Dict 자료형과 컴프리헨션
# [키] {조건부표현식 for 원소 in 반복가능한자료형 필터링}
# [키,값] {조건부표현식 for 원소 in 반복가능한자료형.items() 필터링}
orgDict = {"kor":98,"Eng":100,"Art":78,"Mus":45}

# 과목별 점수를 100으로 나눈 값을 저장
newDict = {key:orgDict[key]/100 for key in orgDict}
# newDict = {i:j/100 for i,j in orgDict.items}
print(newDict)

# 80점 이상만 저장하는 dict
newDict = {key:orgDict[key] for key in orgDict if orgDict[key]>=80}
# newDict = {i:j for i,j in orgDict.items if j>=80}
print(newDict)

# 점수가 80점 이상이면 합격, 아니면 불합격이라고 저장
newDict = {key:"합격" if orgDict[key]>80 else "불합격" for key in orgDict}
# newDict = {i:"합격" if j>80 else "불합격" for i,j in orgDict.items}
print(newDict)

# 점수에따라 학점 A,B,C,D,F로 저장하는 dict
for i,j in orgDict.items():
    if j>90: j="A"
    elif j>80: j="B"
    elif j>70: j="C"
    elif j>60: j="D"
    else: j="F"
    newDict[i]=j
print(newDict)

# 다중 조건문 -> 조건부 표현식
for i,j in orgDict.items():
    j = "A" if j>=90 else "B" if j>=80 else "C" if j>=70 else "D" if j>=60 else "F"
    newDict[i]=j
print(newDict)
# newDict = {i:"A" if j>=90 else "B" if j>=80 else "C" if j>=70 else "D" if j>=60 else "F" for i,j in orgDict.items}
print(newDict)

