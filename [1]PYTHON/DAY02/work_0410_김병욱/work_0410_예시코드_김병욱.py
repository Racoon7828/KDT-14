# 리스트 사용
# 리스트 = list(range(시작, 끝, 증가폭))
a = list(range(10))
print(a)

b = list(range(5, 12))
print(b)

c = list(range(-4, 10, 2))
print(c)

d = list(range(10, 0 , -1))
print(d)

# 튜플 (요소값이 변경 불가능한 자료형)
a = (38,21,53,62,19)
print(a)

a = 38,21,53,62,19
print(a)

# 리스트 처럼 여러 자료형 섞기 가능
a = ('james', 17, 175.3, True)
print(a)

# 요소값이 한개인 튜플
# 튜플 = (값,)
a = (38,)
print(a)

# range
a = tuple(range(-4,10,2))
print(a)

# 튜플 -> 리스트
a = [1,2,3]
print(tuple(a))

# 리스트 -> 튜플
b = (4,5,6)
print(list(b))

a = ['hello', (1,2,3)]
print(a)
b = tuple(a)
print(b)

# 자료형 안 튜플 -> 리스트 변경
c = (a[0], list(a[1]))
print(c)

# 시퀸스(값이 연속적인) 자료형
# list, tuple, str, range

# 특정 값 확인 - in
a = [10,20,30,40,50]
print(30 in a)
print('P' not in ('Hello', 'Python'))

# 객체 연결 + (range는 사용 불가)
a = [10,20,30]
b = [5,4,3,2,1]
print(a+b)

# 문자열 + 숫자
a = 'Hello, '
b = str(10) # 문자열 변환
print(a+b)

# 반복 *
print(a*3)

# 요소 갯수,길이 - len()
print(len('Hello World'))

# 인덱스
a = [38,24,13,51]
print(a[0])
print(a[-1])

# 요소값 할당
a[3]= 15
a[1]= 27
print(a)

# 요소 삭제 - del
del a[2]
print(a, '\n')
# range() 객체는 사용 불가

# 요소 추가 = append(하나만)
a.append(67)
print(a)

# 요소 추가 = insert(원하는 위치
a.insert(3,45)
print(a)

# 요소 추가 = extend([여러개])
a.extend([99,64,31])
print(a)

# 슬라이스 a[시작:끝:증가폭]
print(a[0:4])

del (a[:len(a):2])
print(a)