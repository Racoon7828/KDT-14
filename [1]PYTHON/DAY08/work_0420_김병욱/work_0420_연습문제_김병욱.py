# 퀴즈
# 32.3.1 값 세 개를 매개변수로 받은 뒤 매개변수를 모두 곱해서 반환하는 람다표현식 올바른 것 (d)
# a. lambda a,b: a*b
# b. lambda a,b,c: return a*b*c
# c. lambda a,b,c -> a*b*c
# d. lambda a,b,c: a*b*c
# e. lambda (a,b,c): a*b*c

# 32.3.1 람다표현식 호출하는 올바른 것 (b)
# a. lambda a: a+1(10)
# b. (lambda a: a+1)(10)
# c. lambda a: a+1: 10
# d. lambda a: a+1, 10
# e. lambda a: a+1 <- 10

# 32.3.1 람다표현식 올바른 것 (c)
# a. list(lambda x: x % 10 == 7,a)
# b. list(map(lambda x: x % 10 == 7,a))
# c. list(filter(lambda x: x % 10 == 7,a))
# d. list(reduce(lambda x: x % 10 == 7,a))
# e. list(filter(lambda x: x % 7 == 0,a))

# 연습문제
# 32.4 이미지 파일만 가져오기
# .jpg, .png
# 람다 표현식 사용 문자열 메서드 활용
files = ['font', '1.jpg', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print([i for i in files if i.endswith((".jpg", ".png"))])
print(list(filter(lambda x: x.endswith((".jpg", ".png")),files)))
print(list(filter(lambda x: x.find(".jpg") != -1 or x.find(".png") != -1,files)))

# 심사문제
# 32.5 파일 이름 한꺼번에 바꾸기
# 표준 입력 숫자.확장자 파일 여러개
# 파일 이름이 숫자 3개이면서 앞에 0이 들어가는 형식으로 출력 1.png => 001.png
# 람다 표현식 사용, 리스트 형태로 출력, 문자열 포매팅,메서드 사용
# 1.jpg 10.png 11.png 2.jpg 3.png 97.xslx
files = input().split()
print(list(map(lambda x: f"{x:0>7}" if len(x.split(".")[1]) == 3 else f"{x:0>8}" if len(x.split(".")[1]) == 4 else f"{x:0>9}", files)))

# 묘수풀이
print(list(map(lambda x: f"{int(x.split('.')[0]):03}.{x.split('.')[1]}", files)))
