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
DATA_FILE1 = r"C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\DATA\iris.csv"
DATA_FILE2 = r"C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\DATA\iris_no_columns.csv"
DATA_FILE3 = r"C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\DATA\iris_space.csv"

# --------------------------------------------------------------------
# [2] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
iris_df = pd.read_csv(DATA_FILE1)

utils.print_df('첫번째 줄 컬럼명 있는 CSV',iris_df)
print("컬럼이름 인덱스 ->", iris_df.columns)

# --------------------------------------------------------------------
# [3] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
# 첫번째 줄이 데이터 ==> 컬럼명 없는 CSV 파일 : header 매개변수 설정
iris_df = pd.read_csv(DATA_FILE2, header=None)
iris_df.columns = ['꽃받침_길이', '꽃받침_넓이', '꽃_길이', '꽃_너비', '품종']

utils.print_df('첫번째줄 데이터 미존재 CSV',iris_df)
print("컬럼이름 인덱스 ->", iris_df.columns)

# --------------------------------------------------------------------
# [4] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
# 첫번째 줄이 데이터 ==> 컬럼명 없는 CSV 파일 : header 매개변수 설정
# 데이터 구분 문자 ===> 공백 1개 => sep 매개변수 설정 
iris_df = pd.read_csv(DATA_FILE3, header=None, sep=' ')
iris_df.columns = ['p_h', 'p_W', 's_l', 's_w', 'var']

utils.print_df('첫번째줄 데이터 + 구분자 공백 1개 CSV', iris_df)
print("컬럼이름 인덱스 ->", iris_df.columns)

# --------------------------------------------------------------------
# [5] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
# 첫번째 줄이 데이터 ==> 컬럼명 없는 CSV 파일 => header 매개변수 설정
# 데이터 구분 문자 ===> 공백 1개 => sep 매개변수 설정
# 특정 컬럼을 행인덱스로 설정 로딩 => index_col 매개변수 설정
iris_df = pd.read_csv(DATA_FILE3, header=None, sep=' ', index_col=4)
# iris_df.columns = ['p_h', 'p_W', 's_l', 's_w', 'var']

utils.print_df('첫번째줄 데이터 + 구분자 공백 1개 CSV + 컬럼 행인덱스 설정', iris_df)
# print("컬럼이름 인덱스 ->", iris_df.columns)
print("행 인덱스 ->", iris_df.columns)

# --------------------------------------------------------------------
# [6] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
# DataFrame으로 로딩
iris_df = pd.read_csv(DATA_FILE1, usecols=[0,1,4])

utils.print_df('0,1,4 컬럼만 추출 CSV',iris_df)
print("컬럼이름 인덱스 ->", iris_df.columns)
print("DF 형태 정보 ->", iris_df.shape)

# --------------------------------------------------------------------
# [7] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
# DataFrame으로 로딩
# skipfooter 매개변수 : 아래쪽 지정된 개수 데이터 로딩 X
# skiprows 매개변수 : 앞쪽 지정된 개수 데이터 로딩 X
iris_df = pd.read_csv(DATA_FILE1, skipfooter=30, skiprows=30, header=None)

utils.print_df('일부 행 제외한 데이터 로딩',iris_df)
print("컬럼이름 인덱스 ->", iris_df.columns)
print("DF 형태 정보 ->", iris_df.shape)

# --------------------------------------------------------------------
# [8] CSV >>> DataFrame 로딩 및 기본 형태 확인
# --------------------------------------------------------------------
# 날짜 시간 컬럼 존재하는 데이터 파일
DATA_FILE1 = r'C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\DATA\sample_data.csv'

# DataFrame으로 로딩
# 첫번째줄 -> 컬럼이름 데이터 ok
# 구분자 -> 쉼표/콤마 ok

# 날짜/시간 컬럼 ===> datetime64[ns] 형변환 후 로딩 : parse_dates=[컬럼명] 매개변수 
csv_df = pd.read_csv(DATA_FILE1, parse_dates=['date'])

utils.print_df('일부 행 제외한 데이터 로딩',csv_df)
print("DF 컬럼이름 인덱스 ->", csv_df.columns)
print("DF 형태 정보 ->", iris_df.shape)
print("DF 컬럼 타입 ->", csv_df.dtypes.to_dict())
