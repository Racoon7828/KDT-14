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
# utils.data_info(iris_df)

# --------------------------------------------------------------------
# [5] 통계 관련 메서드들
# --------------------------------------------------------------------
# => 평균, 중앙값, 최빈값, 최소, 최대, 표준편차 계산 메서드
#    axis=0 : 각각 행 단위 계산 = 결과 열
# --------------------------------------------------------------------
iris_sr = iris_df.mean(numeric_only=True)
print(f"각 컬럼의 평균 === \n{iris_sr}\n")

iris_sr = iris_df.median(numeric_only=True)
print(f"각 컬럼의 중앙값 === \n{iris_sr}\n")

iris_sr = iris_df.mode(numeric_only=True)
print(f"각 컬럼의 최빈값 === \n{iris_sr}\n")

iris_sr = iris_df.min(numeric_only=True)
print(f"각 컬럼의 최소 === \n{iris_sr}\n")

iris_sr = iris_df.max(numeric_only=True)
print(f"각 컬럼의 최대 === \n{iris_sr}\n")

iris_sr = iris_df.std(numeric_only=True)
print(f"각 컬럼의 표준편차 === \n{iris_sr}\n")

# ------------------------------------------
# => 상관관계 계산 후 DataFrame
# -> 타켓/주제와 관련있는 변수/속성 선택위한 참고용
# -> 선택된 변수/속성 중 비슷한 변수/속성 필터링용
# ------------------------------------------
iris_corr = iris_df.corr(numeric_only=True)
print(f"상관계수 === \n{iris_corr}\n")
