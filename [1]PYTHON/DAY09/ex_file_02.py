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

# 2. 읽기
# 한줄씩 읽어서 모든 내용 저장하기 
# 몇줄이 존재하는지 모름
# -> readline() 반환값 : 파일 끝에 도달하면 empty str(')
all_data = []
while True:
    line = f.readline()
    if not line:
        break
    all_data.append(line.rstrip('\n'))
print(all_data)

# 3. 닫기 - .close()
f.close()
