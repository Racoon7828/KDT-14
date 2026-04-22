# --------------------------------------------
# 파이썬 표준 모듈 및 패키지
# --------------------------------------------
# random 모듈 : 무작위 값 생성 모듈
# --------------------------------------------
import random

# random.random()
# => 0 이상 1 미만의 실수를 무작위로 반환
print(random.random(),random.random(),random.random())

# random.randint(a,b)
# => a 이상 b 이하의 정수를 무작위로 반환
print(random.randint(2, 15),random.randint(2, 15),random.randint(2, 15))

# random.randrange(start, stop, step)
# => range()처럼 범위 지정해 무작위로 반환
print(random.randrange(1,10,2),random.randrange(1,10,2),random.randrange(1,10,2))

# random.uniform(start, stop)
# => a부터 b 사이의 실수를 무작위로 반환
print(f'{random.uniform(1,10):.2f} {random.uniform(1,10):.2f} {random.uniform(1,10):.2f}')

# random.choice(순서있는 데이터 타입)
# => 1개 무작위로 반환
print(random.choice([1,2,3,4,5,6,7,8,9]), random.choice([1,2,3,4,5,6,7,8,9]))
print(random.choice("hello"), random.choice("hello"))

# random.choices(순서있는 데이터 타입, k=n)
# => n개 무작위로 선택 반환, 중복 가능
print(random.choices([1,2,3,4,5,6,7,8,9],k=5), random.choices([1,2,3,4,5,6,7,8,9],k=5))

# random.sample(순서있는 데이터 타입, k=n)
# => n개 무작위로 선택 반환, 중복 불가
print(random.sample([1,2,3,4,5,6,7,8,9], k=5), random.sample([1,2,3,4,5,6,7,8,9], k=5))

# random.seed()
# => 매번 동일한 랜덤값 추출하도록 고정
random.seed(1)
print("seed 고정")
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))

random.seed(2)
print("seed 고정")
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
print(random.sample([1,2,3,4,5,6,7,8,9], k=5))
