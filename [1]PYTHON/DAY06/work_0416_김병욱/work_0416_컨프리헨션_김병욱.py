# ================================================================
#  Python 컨프리헨션 실습 문제집
#  List / Set / Dictionary Comprehension
# ================================================================

# ----------------------------------------------------------------
#  1. 리스트 컨프리헨션 (List Comprehension)
# ----------------------------------------------------------------
# ★ 초급 (Beginner)
# [문제 1-1]
# 1부터 20까지의 정수 중에서 짝수만 골라 리스트를 만드세요.
# 예상 출력: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print([i for i in range(1,20) if i%2==0])

# [문제 1-2]
# 문자열 리스트 ["hello", "world", "python", "list"]에서
# 각 단어를 대문자로 변환한 새 리스트를 만드세요.
# 예상 출력: ['HELLO', 'WORLD', 'PYTHON', 'LIST']
a = ["hello", "world", "python", "list"]
print([i.upper() for i in a])

# [문제 1-3]
# numbers = [1, 2, 3, 4, 5]일 때,
# 각 숫자의 제곱값을 담은 리스트를 만드세요.
# 예상 출력: [1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5]
print([i ** 2 for i in numbers])

# [문제 1-4]
# 문자열 "Hello, World!"에서 알파벳 소문자만 추출하여 리스트를 만드세요.
# 예상 출력: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
a = "Hello, World!"
print([i for i in a if i.islower()])

# [문제 1-5]
# 0부터 9까지의 숫자 중 3의 배수(0 포함)를 담은 리스트를 만드세요.
# 예상 출력: [0, 3, 6, 9]
print([i for i in range(0,10,3)])
# ---

# ★★ 중급 (Intermediate)

# [문제 1-6]
# numbers = [3, -1, 4, -1, 5, -9, 2, -6, 5]에서
# 양수는 그대로, 음수는 0으로 바꾼 리스트를 만드세요.
# 예상 출력: [3, 0, 4, 0, 5, 0, 2, 0, 5]
numbers = [3, -1, 4, -1, 5, -9, 2, -6, 5]
print([0 if i<0 else i for i in numbers])

# [문제 1-7]
# matrix = [[1,2,3],[4,5,6],[7,8,9]] 인 2차원 리스트를
# 1차원 리스트로 평탄화(flatten)하세요.
# 예상 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([i for row in matrix for i in row])

# print([i for i in matrix])

# [문제 1-8]
# words = ["apple", "banana", "cherry", "date", "elderberry"]에서
# 글자 수가 5 이상인 단어들만 대문자로 변환하여 리스트를 만드세요.
# 예상 출력: ['APPLE', 'BANANA', 'CHERRY', 'ELDERBERRY']
words = ["apple", "banana", "cherry", "date", "elderberry"]
print([i.upper() if len(i) >=5 else i for i in words])

# [문제 1-9]
# 두 리스트 a = [1,2,3]과 b = [4,5,6]에서
# a의 원소 * b의 원소 조합 중 곱이 10 이상인 경우만 모아
# (a원소, b원소, 곱) 튜플 리스트를 만드세요.
# 예상 출력: [(2, 5, 10), (2, 6, 12), (3, 4, 12), (3, 5, 15), (3, 6, 18)]
a, b = [1,2,3], [4,5,6]
print([(i,j,i*j) for i in a for j in b if i*j >= 10])

# [문제 1-10]
# sentences = ["I love Python", "Python is fun", "I am learning"]에서
# 각 문장을 단어 단위로 분리하되, "Python"이 포함된 문장의 단어만 모아
# 하나의 리스트로 만드세요.
# 예상 출력: ['I', 'love', 'Python', 'Python', 'is', 'fun']
sentences = ["I love Python", "Python is fun", "I am learning"]
print([word for sentence in sentences for word in sentence.split() if "Python" in sentence])
# ---


# ----------------------------------------------------------------
#  2. 셋 컨프리헨션 (Set Comprehension)
# ----------------------------------------------------------------

# ★ 초급 (Beginner)

# [문제 2-1]
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]에서
# 중복을 제거한 값들의 집합을 셋 컨프리헨션으로 만드세요.
# 예상 출력: {1, 2, 3, 4}
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print({i for i in numbers})

# [문제 2-2]
# 1부터 10까지의 숫자에서 2의 배수 집합을 만드세요.
# 예상 출력: {2, 4, 6, 8, 10}
print({i for i in range(1,11) if i%2==0})

# [문제 2-3]
# 문자열 "mississippi"에서 등장하는 고유 문자들의 집합을 만드세요.
# 예상 출력: {'m', 'i', 's', 'p'}
print({i for i in "mississippi"})

# [문제 2-4]
# words = ["apple","banana","cherry","apricot","blueberry"]에서
# 첫 글자만 모은 집합을 만드세요. (중복 없음)
# 예상 출력: {'a', 'b', 'c'}
words = ["apple","banana","cherry","apricot","blueberry"]
print({i[0] for i in words})

# [문제 2-5]
# numbers = [1,2,3,4,5,6,7,8,9,10]에서
# 각 숫자를 제곱한 값들의 집합을 만드세요.
# 예상 출력: {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
numbers = [1,2,3,4,5,6,7,8,9,10]
print({i ** 2 for i in numbers})
# ---

# ★★ 중급 (Intermediate)

# [문제 2-6]
# 문자열 리스트 words = ["Python","python","PYTHON","Java","java","JAVA"]에서
# 모두 소문자로 변환한 뒤 중복을 제거한 집합을 만드세요.
# 예상 출력: {'python', 'java'}
words = ["Python","python","PYTHON","Java","java","JAVA"]
print({i.lower() for i in words})

# [문제 2-7]
# a = {1,2,3,4,5}, b = {3,4,5,6,7} 일 때,
# 셋 컨프리헨션으로 두 집합 중 하나에만 속하는 원소들의 집합(대칭 차집합)을 만드세요.
# 예상 출력: {1, 2, 6, 7}
a, b = {1,2,3,4,5}, {3,4,5,6,7}
print({i for i in a.symmetric_difference(b)})

# [문제 2-8]
# sentences = ["I love Python", "Python is great", "I enjoy coding"]에서
# 모든 문장에 등장하는 단어들을 소문자 변환 후 중복 없이 모은 집합을 만드세요.
# 예상 출력: {'i', 'love', 'python', 'is', 'great', 'enjoy', 'coding'}
sentences = ["I love Python", "Python is great", "I enjoy coding"]
print({word.lower() for sentence in sentences for word in sentence.split() if word != "Python"})

# [문제 2-9]
# numbers = list(range(1, 21))에서
# 3의 배수이거나 7의 배수인 숫자들의 집합을 만드세요.
# 예상 출력: {3, 6, 7, 9, 12, 14, 15, 18}
numbers = list(range(1, 21))
print({i for i in numbers if i%3==0 or i%7==0})

# [문제 2-10]
# pairs = [(1,2),(2,3),(3,4),(1,3),(2,4)]에서
# 각 쌍의 합이 짝수인 경우, 그 합 값들로 집합을 만드세요.
# 예상 출력: {4, 6}
pairs = [(1,2),(2,3),(3,4),(1,3),(2,4)]
print({sum(i) for i in pairs if sum(i)%2==0})
# ---


# ----------------------------------------------------------------
#  3. 딕셔너리 컨프리헨션 (Dictionary Comprehension)
# ----------------------------------------------------------------

# ★ 초급 (Beginner)

# [문제 3-1]
# 1부터 5까지의 숫자를 키로, 그 제곱을 값으로 하는 딕셔너리를 만드세요.
# 예상 출력: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print({i: i**2 for i in range(1,6)})

# [문제 3-2]
# words = ["apple","banana","cherry"]에서
# 단어를 키로, 단어의 길이를 값으로 하는 딕셔너리를 만드세요.
# 예상 출력: {'apple': 5, 'banana': 6, 'cherry': 6}
words = ["apple","banana","cherry"]
print({i: len(i) for i in words})

# [문제 3-3]
# 기존 딕셔너리 d = {'a':1, 'b':2, 'c':3}의 키와 값을 서로 뒤집은 딕셔너리를 만드세요.
# 예상 출력: {1: 'a', 2: 'b', 3: 'c'}
d = {'a':1, 'b':2, 'c':3}
print({j: i for i, j in d.items()})

# [문제 3-4]
# keys = ['name','age','city'], values = ['Alice', 30, 'Seoul']을
# zip으로 묶어 딕셔너리를 만드세요.
# 예상 출력: {'name': 'Alice', 'age': 30, 'city': 'Seoul'}
keys,values = ['name','age','city'], ['Alice', 30, 'Seoul']
print({i: j for i, j in zip(keys, values)})

# [문제 3-5]
# 알파벳 'a'부터 'e'까지를 키로, 해당 알파벳의 ASCII 코드를 값으로 하는
# 딕셔너리를 만드세요.
# 예상 출력: {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}
print({i:j for i, j in zip("abcde", range(97, 102))})

# ord() -> 문자 -> 숫자
# char() -> 숫자 -> 문자
# print({i:ord(i) for i in "abcde"})
# ---

# ★★ 중급 (Intermediate)

# [문제 3-6]
# scores = {'Alice':85, 'Bob':42, 'Carol':91, 'Dave':58, 'Eve':76}에서
# 점수가 60 이상인 학생만 포함하고, 점수에 5점을 더한 딕셔너리를 만드세요.
# 예상 출력: {'Alice': 90, 'Carol': 96, 'Eve': 81}
scores = {'Alice':85, 'Bob':42, 'Carol':91, 'Dave':58, 'Eve':76}
print({i: j+5 for i, j in scores.items() if j >= 60})

# [문제 3-7]
# text = "hello world"에서 각 문자를 키로, 등장 횟수를 값으로 하는
# 딕셔너리를 컨프리헨션으로 만드세요. (공백 제외)
# 예상 출력: {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}
text = "hello world"
print({i: text.count(i) for i in text if i != " "})

# [문제 3-8]
# items = [("apple",3),("banana",5),("cherry",2),("date",8)]에서
# 수량이 4 이상인 항목만 골라 {품목: 수량} 딕셔너리를 만드세요.
# 예상 출력: {'banana': 5, 'date': 8}
items = [("apple",3),("banana",5),("cherry",2),("date",8)]
print({i: j for i, j in items if j >= 4})

# [문제 3-9]
# numbers = [1,2,3,4,5,6,7,8,9,10]에서
# 홀수는 키로 "odd", 짝수는 키로 "even"으로 분류하되,
# {숫자: "odd"/"even"} 형태의 딕셔너리를 만드세요.
# 예상 출력: {1:'odd',2:'even',3:'odd',4:'even',5:'odd',
#             6:'even',7:'odd',8:'even',9:'odd',10:'even'}
numbers = [1,2,3,4,5,6,7,8,9,10]
print({i: "odd" if i % 2 == 1 else "even" for i in numbers})

# [문제 3-10]
# two = {1:'one',2:'two',3:'three'}, three = {2:'TWO',3:'THREE',4:'FOUR'}
# 두 딕셔너리에서 공통 키만 골라 {키: (값1, 값2)} 형태의 딕셔너리를 만드세요.
# 예상 출력: {2: ('two', 'TWO'), 3: ('three', 'THREE')}
two, three = {1:'one',2:'two',3:'three'}, {2:'TWO',3:'THREE',4:'FOUR'}
print({i: (j, three[i]) for i, j in two.items() if i in three})
# ---
