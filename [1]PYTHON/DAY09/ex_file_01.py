## ---------------------------------------------------------------------
## 파일 입출력 - 파일 읽기
## ---------------------------------------------------------------------
## 동작 프로세스
## (1) 파일 열기 --- 읽기모드, 인코딩 방식 설정 체크
## (2) 내용 읽기 ---
## (3) 파일 닫기 ---
## ---------------------------------------------------------------------
# 전역 변수
# file_path = 'tmp_in.txt'
file_path = r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY09\tmp_in.txt"

# 파일 내용 읽어서 출력
# 1. 열기 - open()
f = open(file_path, "rt", encoding="UTF-8")

# 2. 읽기 - .read()
# 모든 내용 읽어오기
all_data = f.read()
print(f"all_data\n{all_data}\n{len(all_data)}개")

# 원하는 만큼 읽어오기
data = f.read(30)
print(f"data\n{data}\n{len(data)}개")

# 한줄만 읽어오기 ('\n')
# one_line = f.readline()
# print(f"data\n{one_line}")

# 줄 단위로 모든 읽어오기 ('\n')
# all_lines = f.readlines()
# print(f"data\n{all_lines}")

# 3. 닫기 - .close()
f.close()





