# ===========================================================
# CSV 데이터 파일 >>> DataFrame 변환 로딩
# ===========================================================
# [1] 모듈 로딩
import pandas as pd, sys
# sys.path.append('C:/Users/Win11Pro/Desktop/KDT-14/[2]PANDAS/utils')
sys.path.append(r'C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\utils')
import utils

# [2] csv 데이터 준비
DATA_FILE = '../KDT-14/[2]PANDAS/DATA/iris.csv'

# [3] CSV >>> DataFrame 변환 저장
iris_df = pd.read_csv(DATA_FILE)
# print(iris_df,"\n")

# [4] DataFrame 기본 정보 확인
# 요약 정보
print("요약정보\n")
iris_df.info()

# 실제 데이터 확인 = 기본값 상위 5개 출력
print(f'\n상위 정보\n{iris_df.head(3)}\n{iris_df.tail(2)}')

# 컬럼별 통계 정보 확인
print(f'\n수치 컬럼별 정보\n{iris_df.describe()}')
print(f'\n모든 컬럼별 정보\n{iris_df.describe(include="all")}')

# => describe()/head()/ tail() 메서드는 결과는 저장 후 활용 가능
desc_df = iris_df.describe()
print(f'\ndesc_df 정보\n{desc_df.columns}\n{desc_df.index}')
