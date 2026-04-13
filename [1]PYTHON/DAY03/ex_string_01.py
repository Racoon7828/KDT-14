# 컨테이너 자료형 - [3] string
# "문자", "문자"
# 변수명 = """문자,
# 문자"""
msg = """
니얼굴
(0v0)
"""
print(msg)

# 이스케이프 문자와 raw string
# \n = 줄바꿈
# \t = tap간격
# \\ = \
# \" = "
# \a = 소리 출력 문자
# \U = 유니코드 의미 문자
# raw string : 문자열 내에 이스케이프 문자를 사용하지 않음 설정
# r"문자열" or R"문자열"
# 1. raw string 이해
data1 = "Good\nLuck\t!!"
data2 = r"Good\nLuck\t!!"
print(data1)
print(data2)

# 1. raw string 활용 및 적욕 => 경로(path) 관련
data_path = (r"C:\Users\Win11Pro\Desktop\명령어.txt")
# data_path = ("C:\\Users\Win11Pro\Desktop\명령어.txt")
print(f"txt 파일 경로 : {data_path}")

