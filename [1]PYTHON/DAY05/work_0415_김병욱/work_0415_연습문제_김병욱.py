# 12, 24
# 퀴즈
# 12.3.1 딕셔너리 만드는법 아닌거
# b. x={'a'=10, 'b'=20}

# 12.3.2 x={10:'Hello', 'world':30}에서 키10의 값을 출력하는 법 옳은것
# e.print(x[10])

# 12.3.3 출력 결과 올바른 것
fruits = {'apple': 1500, 'pear':3000, 'grape': 1400}
fruits['orange']=2000
print(fruits['apple'], fruits['orange'])
# c. 1500 2000

# 12.3.4 
print(len({10:0, 20:1, 30:2, 40:2, 50:4, 60:7}))
# d. 6

# 24.3.1 문자열 메서드에 설명이 잘못된 것은?
# a. count는 문자열의 전체 문자 개수를 구한다. => 특정 문자열의 개수 구한다.
# e. index는 문자열의 오른쪽에서부터 문자열을 찾아서 인덱스를 반환한다. => 왼쪽부터

# 24.3.2
print('Python'.lower().replace("on", "ON").ljust(10))
# d.'pythON    '

# 24.3.3 "Hello, Python 3.6"을 만드는 법
# b. "%s, %s 3.6" % ("Hello", "Python")
# d. "{hello}, {language} 3.6".format(hello="Hello", language="Python")

# 25.3.4 문자열 "   1675.3000"을 만드는 법
# 문자열 길이 12, 소수점 이하 4자리
# 오른쪽 정렬, 빈칸 공백
a = "{:>12.4f}".format(1675.3)
print(a)
# c. "{0:>12.4f}".format(1675.3)
# d. "{: >12.4f}".format(1675.3)

# 연습문제
# 12.4 
camille = {
    'health': 575.6,
    'health_regen':1.7,
    'mana':338.8,    
    'mana_regen':1.63,
    'melee': 125,
    'attack_damage':60,
    'attack_speed':0.625,
    'armor':26,
    'magic_resistance':32.1,
    'movemont_speed':340,
}
print(camille['health'])
print(camille['movemont_speed'])

# 24.4
path = r"C:\User\dojang\Appdata\Local\Progrmas\Python\Python36-32\python.exe"
# filename = path[-10:]
a = path.split("\\")
filename = a[-1]
print(filename)

# 심화 문제
# 12.5
user_input1, user_input2 = input(""), input("")
a, b = user_input1.split(" "), user_input2.split(" ")
new_dict = {}
for i,j in zip(a,b): new_dict[i] = j
print(new_dict)  

# 24.5
user_input = input("")
cnt = user_input.split().count("the")
print(cnt)

# 24.6
user_input = input("")
a = [int(i) for i in user_input.split(";")]
a.sort(reverse=True)
for i in a:
    print("{:,}".format(i)) # 책 302 참고 : 파이썬에서 천단위 자동으로 찍어준다.
