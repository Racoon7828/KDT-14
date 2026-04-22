# 27장
# 파일에 문자열 쓰기
# 파일객체 = open(파일이름, 파일모드)
# 파일객체.write(문자열)
# 파일객체.close()

# 파일에 문자열 읽기
# 변수 = 파일객체.read()

# 자동으로 파일 객체 닫기
# with open(파일이름, 파일모드) as 파일객체: 코드

# 파일의 내용을 한줄씩 리스트로 가져오기
# 변수 = 파일객체.readlines()

# 파일의 내용을 한줄씩 읽기
# 변수 = 파일객체.readline()

# 28장
# 회문 판별하기
# 회문 : 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장 ex) level

# 반복문으로 문자 검사하기
# word = "level"
word = "hello"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 -i]:
        is_palindrome = False
        break
print(is_palindrome)

# 시퀸스 뒤집기로 문자 검사하기
print(word == word[::-1])

# 리스트와 reversed 사용
word = "level"
print(list(word) == list(reversed(word)))

# 문자열의 join 메서드와 reversed 사용
print(word == ''.join(reversed(word)))

# N-gram 문자열에서 n개의 연속된 요소를 추출하는 방법
# 반복문으로 N-gram 만들기
for i in range(len(word)-1): print(word[i], word[i+1], sep="")

# zip으로 n-gram 만들기
two_gram = zip(word, word[1:])
for i in two_gram: print(i[0], i[1], sep="")

# zip과 리스트 표현식으로 n-gram 만들기
print(list(zip([word[i:] for i in range(3)]))) # [('level',), ('evel',), ('vel',)]

# zip = 반복가능한 객체 여러개를 콤마로 넣어줘야함
# zip리스트 안 각 요소를 콤마로 구분 = 리스트앞 * 붙이기
print(list(zip(*[word[i:] for i in range(3)])))
