# 딕셔너리 생성
lux1 = dict(health=190, mana=334, melee=550, armor=18.72)
print(lux1)

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490,334,550,18.72]))
print(lux2)

lux3 = dict([('health', 190) , ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

lux4 = dict({'health':190, 'mana':334, 'melee':550, 'armor':18.72})
print(lux4)

lux = {'health':190, 'mana':334, 'melee':550, 'armor':18.72}
print(lux["health"])
print(lux["armor"])

lux['health'] = 2037
lux['mana'] = 1184
lux['mana_regen'] = 3.28
print(lux)

# 문자 바꾸기
table = str.maketrans("aeiou", "12345")
print("apple".translate(table))

# 문자 분리하기
a = "apple pear grape pineapple orange".split()
print(a)

# 문자열 왼쪽에 0 채우기
a = "35".zfill(5)
print(a)

# 매서드 체이닝
a = "python".rjust(10).upper().zfill(20)
print(a)

# 문자열 개수 세기
a = 'apple pineapple'.count('pl')
print(a)

a = """an elongated hand-held movable body carrying a light emitting cell array including a plurality of light emitting cells arranged in alignment for reciprocally swinging on a desired surface by manual swing motion at an arbitrary speed to scan said light emitting cell array thereon and form a visual image utilizing an effect of residual image;
display data storage means for storing display data in the form of a bit map;
display data reading out control means for reading out display data from said display data storage means in a given order at a given speed, said display data including a plurality of sets of display data for respective light emitting cells associated with an elapsed time factor representative of angular positions of said hand-held movable body;
driver means adapted to said light emitting cell array, for receiving given bits of said display data read out by said display data reading out control means and for driving each of said light emitting cell arrays ON and OFF;
swing detecting means for producing a detection signal on the basis of the acceleration of the swinging motion of said movable body, said swing detecting means including,
an acceleration sensor for generating an output corresponding to the acceleration of the swinging motion of said movable body, and signal processing means for detecting a specific operational point in said swinging motion of said movable body by processing the output from said acceleration sensor, 
and timing control means responsive to said detection signal for deriving a trigger signal so as to control said display data reading control means such that respective sets of display data for respective light emitting cells are read out at the substantially same angular positions of said hand-held movable body for arbitrary swing speeds."""
print("data의 개수:", a.count("data"))
print("the의 개수:", a.count("the"))
b = list(a.split(" "))
print("the의 개수:", b.count("the"))

# 서식 지정자 &s 문자열
name = "maria"
print("I am %s." % "james")
print("I am %s." % name)
print("We are %s %s." % (name, "james"))

# %s 문자열
# %d 정수
# %f 소수
# %.자릿수f % 숫자
print('%.2f' % 2.3)

# 채우기와 정렬을 조합헤사 사용하기
# "{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}"
print("{0:0<10.2f}".format(15))
print("{:,>10.2f}".format(15))