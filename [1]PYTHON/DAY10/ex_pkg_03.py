# --------------------------------------------
# 파이썬 표준 모듈 및 패키지
# --------------------------------------------
# OS 모듈: 파일, 폴더 경로 모듈
# --------------------------------------------
import os

# os.mkdir()
# => 1개 폴더 셍성
# => 존재하면 Error 발생
# os.mkdir(r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY10\TEST")

# os.makedirs()
os.makedirs(r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY10\TEST", exist_ok=True)

# os.listdir()
# -> 폴더 내의 목록이름 리스트 반환
items = os.listdir(r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY10")
print(f"폴더 내 항목 : {len(items)}개")
print(items)

# os.join()
# = 경로 만들기
i_path = os.path.join(r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY10", items[0])
print(i_path)

i_path = os.path.join(r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY10", items[0], "image.jpg")
print(i_path)

# [실습] DAY10 폴더 안에 파일만 화면에 출력하세요
# 단, 경로정보까지 출력해주세요.
for item in items:
    item_path = os.path.join(r"C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY10", item)
    if os.path.isfile(item_path):
        print(item, item_path)
