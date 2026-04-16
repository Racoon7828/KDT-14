# # 제어문(조건문/반복문) 연산자 - [1] 
# 조건문 : 조건에 맞는 코드 실행 문법
# 반복문 : 조건에 따라 특정 코드 반복 실행 여부 결정 문법
# 멤버 연산자 : in, not in ==> 연산 대체 가능
# ex) 파일 확장자에 따라서 파일 분류
# 이미지 파일 : jpg, png, jpeg, bmp
# 텍스트 파일 : hwp, txt, word
# 기타 파일 : 나머지
# 1. 파일 이름에서 확장자만 찾기
filename = "cat.jpg"
ext = filename.split(".")[1] # 패킹으로 인덱스 접근
_, ext = filename.split(".") # 언패킹으로 접근 / _ = 문법상 필요로 쓰는 의미없는 변수명
print(f"이름:{_}, 확장자:{ext}")

# 2. 확장자에 따른 파일 출력
if ext == "jpg" or ext == "png" or ext == "jpeg" or ext == "bmp":
    print("이미지 파일")
elif ext == ".hwp" or ext == "txt" or ext == "word":
    print("텍스트 파일")
else: print("기타 파일")

# 1. 파일 이름에서 확장자만 찾기
filename = "cat.jpg"
_, ext = filename.split(".") # 언패킹으로 접근 / _ = 문법상 필요로 쓰는 의미없는 변수명

# 2. 확장자에 따른 파일 출력
# 다중 조건문 : 조건 2개이상 - elif
if ext in ['jpg', 'png', 'jpeg', 'bmp']: print("이미지 파일")
elif ext in ['hwp', 'txt', 'word']: print("텍스트 파일")
else: print("기타 파일")
