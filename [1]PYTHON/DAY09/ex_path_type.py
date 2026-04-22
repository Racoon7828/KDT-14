## ---------------------------------------------------------------------
## 경로
## - 절대경로 : Window OS관점에서 드라이브 기준(C.:\) 
##             [예] C:\Users\kwon\Desktop\PYTORCH_IMAGE\data\flower.jpg
##             Linux OS관점에서 루트(/)
## - 상대경로 : 현재 파일이 있는 위치를 기준으로 경로/파일위치 설정
## -           특별한 의미를 가진 ., .. 기호 사용
## -           [예] ../data/flower.jpg
## ---------------------------------------------------------------------
## 파일의 경로
## (1) temp_in.txt  : 현재 파이썬 코드 파일과 동일한 폴더에 존재
## (2) temp_out.txt : [1]PYTHON 폴더에 존재
##                    현재 파이썬 코드 파일과 다른 위치에 존재
## ---------------------------------------------------------------------
# 파일 및 경로 관련 함수, 클래스 존재하는 파일 : 모듈
# 모듈을 코드에 포함하기 문법 => import 모듈파일명
import os

# 전역변수 파일경로 저장
# file_path_abs1 = "C:/Users/Win11Pro/Desktop/KDT-14/[1]PYTHON\DAY09/tmp_in.txt"
file_path_abs1 = r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY09\tmp_in.txt"

# 코드 파일과 같은 위치에 존재 즉, 현재 위치를 의미 => 기호 ./
# file_path_re1 = r"./tmp_in.txt"
file_path_re1 = 'tmp_in.txt'

# 현재 코드 파일 보다 상위 폴더에 존재한다는 의미 => ../
file_path_abs2 = r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\tmp_out.txt"
file_path_re2 = r"../tmp_out.txt"
## ---------------------------------------------------------------------
# 파일 존재 여부 검사
# os 모듈의 함수 사용
print(f"절대경로 : {os.path.exists(file_path_abs1)}")
print(f'상대경로 : {os.path.exists(file_path_re1)}')
print(f"절대경로 : {os.path.exists(file_path_abs2)}")
print(f'상대경로 : {os.path.exists(file_path_re2)}')
## ---------------------------------------------------------------------

# [실습] check.py 파일의 절대경로, 상대 경로 출력하기
## ---------------------------------------------------------------------
file_abs = r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY01\check.py"
file_re = "../DAY01/check.py"
print(os.path.exists(file_abs))
print(os.path.exists(file_re))
