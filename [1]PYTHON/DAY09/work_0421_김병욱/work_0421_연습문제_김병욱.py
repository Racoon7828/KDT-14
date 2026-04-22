# 27,28 27.3안해도됨
# 퀴즈
# 27.4.1 다음 중 문자열을 쓸때 파일 열기 방법으로 올바른 것 (d)
# a. file = open('hello.txt', 'r')
# b. file = open('hello.txt', 'b')
# c. file = open('hello.txt', 'rb')
# d. file = open('hello.txt', 'w')
# e. file = open('hello.txt', 'wb')

# 27.4.2 다음 중 파일에서 문자열을 한 줄씩 읽어서 리스트 형태로 가져오는 메서드로 올바른 것을 고르세요. (c)
# a. read
# b. readline
# c. readlines
# d. writelines
# e. write

# 27.4.3 다음 중 pickle 모듈로 파일에 저장된 파이썬의 객체를 읽어올 때 파일 열기 방법으로 올바른 것 (b)
# a. file = open("maria.p", 'r')
# b. file = open("maria.p", 'rb')
# c. file = open("maria.p", 'w')
# d. file = open("maria.p", 'wb')
# e. file = open("maria.p", 'rt')

# 연습문제
# 27.5 파일에서 10자 이하인 단어 개수 세기
file = r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY09\work_0421_김병욱\words.txt"
with open(file, "w", encoding="utf8")as f:
    f.write("anonymously\ncompatiblity\ndashboard\nexperience\nphotography\nspotlight\nwarehouse\n")

with open(file, 'r', encoding="utf8") as f:
    a = f.readlines()
    b = 0
    for i in a:
        if len(i.strip("\n"))<=10:
            print(i)
            b += 1
print(b)
# 28.3 단어 단위 N-gram 만들기
# 표준 입력 정수와 문자열 각줄에 입력
# 입력된 숫자에 해당하는 단어 단위 N-gram을 튜플로 출력
# 입력된 정수 미만이면 "wrong" 출력
n = int(input())
text = input()
words = text.split()
if len(words) < n:
    print("wrong")
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)

# 심사문제
# 27.6 특정 문자가 들어있는 단어 찾기
# 문자열(한줄)이 저장된 words.txt 파일이 주어집니다. 
# 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 등장한 순서대로 출력/, . 출력 X
file = r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY09\work_0421_김병욱\words.txt"
with open(file, "w", encoding="utf8")as f:
    f.write("Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.")
with open(file, "r") as f:
    a = f.read()
    words = a.split()
    for i in words:
        c_word = i.strip(".,")
        if "c" in c_word: print(c_word)

# 28.4 파일에서 회문인 단어 출력하기
# 단어가 줄 단위로 저장된 word.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력
# 파일에서 읽은 단어는 \n 판단 후 제외한 후 출력
with open(file, "w", encoding="utf-8") as f:
    f.write("apache\n")
    f.write("decal\n")
    f.write("did\n")
    f.write("neep\n")
    f.write("noon\n")
    f.write("refer\n")

with open(file, "r", encoding="utf-8") as f:
    for line in f:
        word = line.strip()
        if word == word[::-1]: print(word)