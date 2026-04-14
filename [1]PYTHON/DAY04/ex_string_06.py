# 컨테이너 자료형 - [3] string
# str 메서드

# 10. 특정 문자열/문자로 시작하는지 또는 끝나는지 검사하는 메서드
# -> startwith(문자/열) : 시작 검사 => True/False
# -> endswich(문자/열) : 끝 검사 => True/False

# Unpacking 언팩킹 : 원소 개수만큼 변수명을 선언해서 저장하는 것
#                   한개의 변수명으로 관리하던 데이터를 여러개의 변수명으로 나누어서 저장
filename1, filename2, filename3 = "data.csv", "image.jpg", "image.png"

# 특정 문자/열로 시작하는지 검사 : startswith()
ret = filename1.startswith("d")
print(f"{filename1} : start d? => {ret}")

# 특정 문자/열로 끝나는지 검사 : endswith()
ret = filename2.endswith(".jpg")
print(f"{filename2} : jpg? => {ret}")

ret = filename3.endswith((".jpg", ".png", "gif"))
print(f"{filename3} : image? => {ret}")