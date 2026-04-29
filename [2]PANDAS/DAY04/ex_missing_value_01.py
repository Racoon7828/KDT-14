# ======================================================
# 결측치 체크 및 검사
# ------------------------------------------------------
# DataFrame.isnull() / .isna() => True/False 원소마다 검사
# ======================================================
# [1] 모듈 로딩
import pandas as pd, numpy as np, sys
sys.path.append(r'C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\utils')
import utils

# [2] 데이터 준비
## DF 생성
df = pd.DataFrame(dict( age =[ 5, 6, np.nan ],
born =[ pd.NaT, pd.Timestamp('1939-05-27'), pd.Timestamp('1940-04-25')],
name=['Alfred', 'Batman', ''],
toy=[None, 'Batmobile', 'Joker']) )

## DF 출력
utils.data_info(df,isall=True)

# ------------------------------------------------------
# 결측치 체크
# ------------------------------------------------------
print(f'df.isna() ===\n{df.isna()}\n')
print(f'df.isnull() ===\n{df.isnull()}\n')

print(f'컬럼별 결측치 개수\n{df.isnull().sum()}\n')

