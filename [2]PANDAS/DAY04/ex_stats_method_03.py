# ==============================================
# 통계 관련 메서드들
# ==============================================
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

# ----------------------------------------------
# [5] 통계 관련 메서드들 - 상관관계
# ----------------------------------------------
# => 상관관계 계산 후 DataFrame 반환 : .corr()
# => 수치 데이터 기반 계산
# => 컬럼들의 관계성을 -1 ~ 1 범위로 반환
# => 목적
#  * 주제와 관련된 변수/속성/컬럼 여부 검사용
#  * 선택된 변수/속성/컬럼 중 비슷한 속성들 필터링용
# ----------------------------------------------
iris_corr = iris_df.corr(numeric_only=True)
print(f"상관계수 === \n{iris_corr}\n")

## 타켓/주제에 해당하는 컬럼만 추출
print(iris_corr['petal.length'].abs().sort_values(ascending=False))
