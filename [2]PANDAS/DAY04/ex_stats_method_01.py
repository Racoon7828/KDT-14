# ===========================================================
# 통계 관련 메서드들
# ===========================================================
# [1] 모듈 로딩
import pandas as pd, sys
sys.path.append('C:/Users/Win11Pro/Desktop/KDT-14/[2]PANDAS/utils')
import utils

# [2] csv 데이터 준비
DATA_FILE = 'C:/Users/Win11Pro/Desktop/KDT-14/[2]PANDAS/DATA/iris.csv'

# [3] CSV >>> DataFrame 변환 저장
iris_df = pd.read_csv(DATA_FILE)
# print(iris_df,"\n")

# [4] DataFrame 기본 정보 확인
# utils.data_info(iris_df, isall = True)

# --------------------------------------------------------------------
# [5] 통계 관련 메서드들
# --------------------------------------------------------------------
# => DataFrame에 전체 컬럼별 데이터 수 반환 : count()
#    axis=0 : 각각 행 단위 계산 = 결과 열
cnt_sr = iris_df.count()
print(f"axis=0 각 컬럼의 NA가 아닌 데이터 수 === \n{cnt_sr}\n")

#    axis=1 : 각각의 열 단위 계산 = 결과 행
cnt_sr = iris_df.count(axis=1)
print(f"axis=1 각 행의 NA가 아닌 데이터 수=== \n{cnt_sr}\n")

# --------------------------------------------------------------------
# 행의 모든 값이 동일한 개수 반환 => value_counts()
vcnt_sr = iris_df.value_counts()
print(f"vcnt_sr === \n{vcnt_sr}\n")

# --------------------------------------------------------------------
# 특정 컬럼의 데이터별 개수
# => iris_df.컬럼명.value_counts()
# => iris_df['컬럼명'].value_counts()
# --------------------------------------------------------------------
vcnt_sr = iris_df.variety.value_counts()
vcnt_sr = iris_df['variety'].value_counts()
print(f"variety 컬럼의 데이터별 개수 === \n{vcnt_sr}\n")

# --------------------------------------------------------------------
# 컬럼별 데이터/값의 종류 개수 즉,  고유값 반환 : unique()
# => DataFrame에는 없음 Series.unique()
# --------------------------------------------------------------------
# variety 컬럼의 데이터/값의 종류 => 고유값
ret = iris_df['variety'].unique()
print(f"variety 컬럼의 고유값 : {ret}, 원소개수 : {len(iris_df['variety'])}개\n")
print(f"variety 컬럼의 고유값별 원소 개수 \n{iris_df['variety'].value_counts()}\n")

ret = iris_df['petal.width'].unique()
print(f"variety 컬럼의 고유값 : {ret}, 원소개수 : {len(iris_df['petal.width'])}개\n")
print(f"variety 컬럼의 고유값별 원소 개수 \n{iris_df['petal.width'].value_counts()}\n")
