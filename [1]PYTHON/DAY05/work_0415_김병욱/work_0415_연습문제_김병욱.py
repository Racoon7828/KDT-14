# 25.3, 26.6 제외
# 과제 25,26

# 퀴즈
# 25.6.1 키 'Python'과 해당 값을 삭제하는 방법
# c. x.pop('Python',100) - O
# e. del x[Python] - O

# 25.6.2 딕셔너리 메서드에 대한 설명으로 올바르지 않는 것을 모두 고르세요 (b,c)
# a. setdafault는 딕셔너리에 키-값 쌍을 추가한다. - O
# b. setdafault는 키만 지정하면 값은 0으로 지정한다. - X = 값은 None 
# c. key는 딕셔너리의 키-값 쌍을 모두 가져온다. - X = key만
# d. clear는 딕셔너리의 모든 키-값 쌍을 삭제한다. - O
# e. update는 딕셔너리에서 키의 값을 수정한다. - O

# 25.6.3 반복문으로 딕셔너리 x의 모든 키를 출력하는 방법으로 올바른 것을 고르시오. (a,d)
# a. for key, value in x: print(key) - X = Error
# b. for key in x: print(key) - O
# c. for key in x.keys(): print(key) - O
# d. for value in x.values(): print(value) - X = 값만 출력
# e. for key, value in x.items(): print(key) - O 

# 25.6.4 다음 중 딕셔너리 x={"a":10,"b":20,"c":30,"d":40}에서 값이 40인 키-값 쌍을 삭제하는 방법 (d)
# a. for key value in x.items(): if value == 40: del x[key]
# b. del x[40]
# c. x = {key: value for key, value in x.items()}
# d. x = {key: value for key, value in x.items() if value != 40} - O
# e. x = {key: value for key, value in x.items() if value == 40}

# 25.6.5딕셔너리 terrestrial_planet의 키 "satellites"에 접근하는 방법 (d)
terrestrial_planet = {
    "Earth": {
        "physical_characteristics":{
            "mean_radius":6271.0,
            "mass": 5.97279E+24
        },
        "orbital_characteristics":{
            "orbital_period": 365.25641,
            "satellites": 1
        }
    },
    "Mars": {
        "physical_characteristics":{
            "mean_radius":3389.5,
            "mass": 6.4185E+23
        },
        "orbital_characteristics":{
            "orbital_period": 686.9600,
            "satellites":2
        }
    }
}

# a. terrestrial_planet("Earth")("orbital_characteristics")("satellites")
# b. terrestrial_planet["satellites"]
# c. terrestrial_planet["Earth"]["satellites"]
# d. terrestrial_planet["Earth"]["orbital_characteristics"]["satellites"] - O
# e. terrestrial_planet["Mars"]["physical_characteristics"]["mass"]

# 25.6.6 실행결과
import copy
x = {"python": {"version": "2.7"}, "scripts":{"name":"hello.py"}}
a = x
b = x.copy()
c = copy.deepcopy(x)
x["python"]["version"]="3.6"
print(a["python"]["version"], b["python"]["version"], c["python"]["version"])
# c. 3.6 3.6 2.7

# 26.7.1 다음 중 세트를 만드는 법으로 올바르지 않는 것 (b)
# a. a = {1,2,3,4,5} - O
# b. a = {} - X => 딕셔너리
# c. a = set("hello") - O
# d. a = set(range(10)) - O
# e. a = set() - O

# 26.7.2 a = {1,2,3}, b ={3,4,5}가 있을 때 집합 연산의 결과로 잘못된 것 (b,e)
# a. set.union(a,b)는 {1,2,3,4,5} - O
# b. a ^ b = {1,3,5} - X => {1,2,4,5}
# c. a - b = {1,2} - O
# d. a & b = {3} - O
# e. set.difference(b,a) = {4} - X => {4,5}

# 26.7.3 부분집합, 상위 집합에 대한 설명으로 잘못된 것 (c,d)
# a. 부분집합은 <=와 issubset로 구할 수 있고, 두세트가 같을때 참이다. - O
# b. 진부분집합은 <와 issubset로 구할 수 있고, 두세트가 다를때 참이다. - X => 진부분집합을 구하는 메서드는 없다 
# c. 상위집합은 >=와 issuperset로 구할 수 있고, 두세트가 같을때 참이다. - O
# d. 진상위집합은 > 두세트가 같을때 참이다. - X => 두세트가 다를때 참
# e. 진부분집합과 진상위집합을 구하는 메서드는 없다

# 26.7.4 세트 메서드에 대한 설명으로 올바른 것 (a,b,c)
# a. intersection_update는 현재 세트와 다른 세트중에서 겹치는 요소만 현재 세트에 저장 - O
# b. set.symmetric_difference는 두 세트의 대칭차집합을 구한다. - O
# c. isdisjoint는 햔재 세트가 다른 세트와 겹치지 않는지 확인한다. - O
# d. discard는 현재 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생시킨다. - X => 에러 발생 X
# e. pop은 현재 세트에서 지정된 요소를 삭제하고 요소가 없으면 에러를 발생시킨다. - X => remove()

# 26.7.5 메서드와 연산자의 기능이 잘못 짝지어진 것 (c,d)
# a. set.intersection = & - O
# b. set.update = |= - O
# c. symmetric_difference_update = -= - X => ^=
# d. issuperset = > - X => >=
# e. ste.union = | - O

# 26.7.6 세트 {0,1,3,4,5,6,8,9}을 만드는 방법 (a)
# a. {i for i in range(10) if i !=2 and i != 7} - O
# b. {i for i in range(10) if i !=2 or i != 7} - X
# c. {i for i in range(10) if i is not 2 and i is not 7} - X
# d. {i for i in range(10) if i is not 2 or i is not 7} - X
# e. {i for i in range(10) if i is 2 and i is 7} - X

# 연습문제
# 25.7 평균점수 구하기
maria = {"kor":94,"eng":91,"math":89,"sci":83}
avg = sum(maria.values())/ len(maria)
print(avg)

# 26.8 공배수 구하기
# 1~100 까지 숫자중 3과 5의 공배수 구하기
a,b = set(range(3,101,3)), set(range(5,101,5))
print(a&b)

# a = {i for i in range(1,101) if i % 3 == 0}
# b = {i for i in range(1,101) if i % 5 == 0}
# print(a&b)

# 심사문제
# 25.8 딕셔너리 특정 값 삭제하기
# 표준 입력으로 문자열 여러개와 숫자 여러 개가 두 줄로 입력되고 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성
# 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.
# alpha bravo charlie delta
# 10 20 30 40
keys = input().split()
values = map(int, input().split())
x = dict(zip(keys, values))
x = {key:value for key,value in x.items() if key != "delta" and value != 30}
print(x)

# 26.9 공약수 구하기
# 표준 입력 양의 정수
# 두 숫자의 공약수를 세트 형태로 구하기
# 최종 결과 = 공약수의 합
user_input1, user_input2 = int(input()), int(input())
a = {i for i in range(1,user_input1+1) if user_input1 % i == 0}
b = {i for i in range(1,user_input1+1) if user_input1 % i == 0}
divisor = a & b
result = 0
if type(divisor) == set: result = sum(divisor)
print(result)