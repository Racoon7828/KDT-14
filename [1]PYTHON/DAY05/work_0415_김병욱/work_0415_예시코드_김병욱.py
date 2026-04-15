# 25장 딕셔너리 심화
x = {"a":10,"b":20,"c":30,"d":40}
x.setdefault("e")
x.setdefault("f", 100)
print(x)

x.update(a=90, e=60)
print(x)
x.update({"a":"A","g":"G"})
print(x)
x.update(zip(["b","c"],["C","D"]))
print(x)

# 삭제
x.pop("e")
del(x["f"])
print(x)

# 키로 딕셔너리 만들기
keys = range(10,100,10)
values = range(1,10)
x = dict.fromkeys(keys)
print(x)

# 키:값
x = dict(zip(keys,values))
print(x,"\n")

# 반복문 사용해서 출력하기
for i in x:
    print(i, end=" ")

# .keys = 키만
# .values = 값만
# .items = 키,값
for i, j in x.items():
    print(i,j)

# dict 표현식 for문 활용
v = {key: value for key, value in dict.fromkeys(keys).items()}
print(v)

# dict 표현식 if문 활용 - 특정 값 제외
v = {key: value for key, value in x.items() if value != 2}
print(v)

# 딕셔너리 안에 딕셔너리 활용
# 딕셔너리 = {키1:{키A:값A}, 키2:{키B:값B}}
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
# 딕셔너리[키][키] = 값
print(terrestrial_planet['Venus']['mean_radius'])

# 딕셔너리 할당과 복사
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x # 같은 딕셔너리
print(x is y) # True
print(x == y) # True
y['a'] = 100 # x,y 모두 변경됨
print(x)
print(y)

# 딕셔너리 복사 - copy()
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy() # 서로 다른 객체 (별개)
print(x is y) # False
print(x == y) # True (키:값)은 같다
y['a'] = 100 # y 값만 변경
print(x)
print(y)


# 중첩 딕셔너리 복사
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
print(x)
print(y)
y['a']['python'] = '2.7.15' # x,y 모두 변경됨
print(x)
print(y)

# 중첩 딕셔너리 복사 - deepcopy()
import copy
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = copy.deepcopy(x)
print(x)
print(y)
y['a']['python'] = '2.7.15' # y만 변경됨
print(x)
print(y)

# 26장 세트 사용하기
# 중복 X
# []으로 특정 요소 출력 X => 멤버 연산자(in)으로 값 확인
fruits = {'strawberry', 'grape', 'grape', 'grape', 'orange', 'pineapple', 'cherry'}
print("\n",fruits)

# 집합 연산 - 합집합(union) = |
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)
print(set.union(a,b))

# 집합 연산 - 교집합(intersectiom) = &
print(a&b)
print(set.intersection(a,b))

# 집합 연산 - 차집합(difference) = -
print(a-b)
print(set.difference(a,b))


# 집합 연산 - 대칭차집합(symmetric_difference) = ^
print(a^b)
print(set.symmetric_difference(a,b))

# 집합 연산 후 할당
# 세트1 |= 세트2
# 세트1.update(세트2)

# 세트1 &= 세트2
# 세트1.intersection_update(세트2)

# 세트1 -= 세트2
# 세트1.difference_update(세트2)

# 세트1 ^= 세트2
# 세트1.symmetric_difference_update(세트2)


# 부분집합과 상위집합 확인하기 => bool 반환
# 부분집합 확인 - 부분집합(subset) = <=
print(a<=b)
print(set.issubset(a,b))

# 진부분집합 확인 - 진부분집합(proper subset) = <
print(a<b) # 메서드 없음

# 상위집합 확인 - 상위집합(superset) = >=
print(a>=b)
print(set.issuperset(a,b))

# 진상위집합 확인 - 진상위집합(proper superset) = <
print(a<b) # 메서드 없음

# 세트가 같은지 다른지 비교 => bool 반환
# == => 같은지
# != => 다른지
# disjoint => 겹치지 않는지

# 요소 추가 - add()
a = {1,2,3,4}
a.add(5)
print(a)

# 요소 삭제 - remove() - 요소가 없으면 에러
a.remove(3)

# 요소 삭제 - discard() - 요소가 없어도 넘어감
a.discard(2)
print(a)

# 요소 복사 - copy()
a = {1, 2, 3, 4}
b = a.copy() # a,b 는 별개 객체
b.add(5)
print(a)
print(b)

# 반복문으로 세트요소 출력
a = {1, 2, 3, 4}
for i in a:
    print(i,end='')
    
# 세트 표현식 사용하기
# {식 for 변수 in 반복가능한 객체}
# set{식 for 변수 in 반복가능한 객체}
a = {i for i in "apple"}
print(a)

# if문 첨가
a = {i for i in "pineapple" if i not in "apl"}
print(a)