# =======================================================
# File ===> DataFrame으로 변환 로딩
# 관련 함수들 : pandas.read_파일포멧()
# pandas.read_csv() / .read_excel() / .read_json()
# =======================================================
# [기억] DataFrame = 행인덱스 + 열이름인덱스 + 데이터
# [규칙] 파일의 첫번째 줄에 데이터 ===> 열이름/컬럼이름으로 설정
# =======================================================
## [1] 모듈 로딩 및 데이터 선정
import pandas as pd, sys
sys.path.append(r'C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\utils')
import utils

# 데이터 파일
# DATA_FILE1 = r"C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\DATA\학생관리부.xlsx"
DATA_FILE1 = "../DATA/학생관리부.xlsx"
# --------------------------------------------------------------------
# [2] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
excel_df = pd.read_excel(DATA_FILE1, header=2, index_col='이름') # 0,1번행 자동 버려짐

# 기본 정보 확인
utils.print_df('excel',excel_df)
print("컬럼이름 인덱스 ->", excel_df.columns)

# --------------------------------------------------------------------
# [3] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
# DataFrame으로 로딩
# 엑셀파일에서 로딩할 시트 설정 : sheet_name = 정수/문자열
excel_df = pd.read_excel(DATA_FILE1, header=2, sheet_name=1, usecols=range(1,7))

# 기본 정보 확인
utils.print_df('두번째 시트 설정',excel_df)
print("컬럼이름 인덱스 ->", excel_df.columns)
print("행 ->", excel_df.index)
