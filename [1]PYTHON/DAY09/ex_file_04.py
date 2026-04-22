## ---------------------------------------------------------------------
## 파일 입출력 - 파일 쓰기
## ---------------------------------------------------------------------
## 동작 프로세스
## (1) 파일 열기 --- 쓰기 모드, 인코딩 방식 설정 체크
## (2) 내용 쓰기 ---
## (3) 파일 닫기 ---
## ---------------------------------------------------------------------
# 전역 변수
# file_path = 'tmp_in.txt'
file_path = r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY09\mydata.txt"

# 파일 쓰기 - 1: a 모드(append)
# 존재하지 않는 파일이면 생성
# 존재하는 파일이면 끝 부분에 내용추가
# 1. 열기 - open()
f = open(file_path, "at", encoding="UTF-8")

# 2. 쓰기 - .write()
w_data = f.write("잠 존나 온다. 뒤지겠다""\n")
print(f"쓰기한 개수 : {w_data}개")

w_data = f.write("1234567890""\n")
print(f"쓰기한 개수 : {w_data}개")

# 파일 속성들 확인
print(f'closed : {f.closed}')
print(f'name : {f.name}')
print(f'mode : {f.mode}')

# 3. 닫기 - .close()
f.close()
print(f'mode : {f.mode}')


