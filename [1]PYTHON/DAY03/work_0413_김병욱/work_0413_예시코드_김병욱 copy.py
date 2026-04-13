# 문자열
hello = "hello, world"

# 여러줄
hello = """hello, world
안녕하세요.
Python입니다."""
print(hello)

# 문자열 따옴표 포함
s = "He said 'Python is easy'"
print(s)

single_quote = '''"안녕하세요."
'파이썬'입니다'''
double_quote1 = """"Hello"
'Pythhon'"""
double_quote2 = """Hello, 'Pythhon'"""
print(single_quote)
print(double_quote1)
print(double_quote2)

# 리스트 요소 추가
a = [10,20,30]
a.append([500,600])
print(a, len(a))

a = [10,20,30]
a.extend([500,600])
print(a, len(a))

a = [10,20,30]
a.insert(2, 500)
print(a, len(a))

# 리스트 요소 삭제
a = [10,20,30]
a.pop(1)
print(a)

# 특정값 삭제
a = [10,20,30,20]
a.remove(20) # 맨 처음 값 삭제
print(a)

# 인덱스
a = [10,20,30,15,20,40]
print(a.index(20))
# 요소 개수
print(a.count(20))
# 요소 정렬
a.sort(reverse=True)
print(a)
# 요소 전체 삭제
a.clear()
print(a)

# 리스트 슬라이스 조작
a = [10,20,30]
a[len(a):] = [50]
a[len(a):] = [40]
print(a)