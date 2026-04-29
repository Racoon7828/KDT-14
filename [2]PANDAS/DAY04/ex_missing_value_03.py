# ======================================================
# 결측치 처리 - 치환
# ------------------------------------------------------
# DataFrame.fillna() 
# ======================================================
# [1] 모듈 로딩
import pandas as pd, numpy as np

# [2] 데이터 준비
df = pd.DataFrame([ [np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, np.nan],
                    [np.nan, 3, np.nan, 4]],
                    columns=list("ABCD"))

## DF 출력
print(df,"\n")

# ------------------------------------------------------
# 결측치 치환 - fillna()
# ------------------------------------------------------
# [1] 특정 값으로 결측치 채우기 (value = 0)
print(f'[모든 결측치 0]df.fillna() === \n{df.fillna(value=0)}\n')

# [2] 컬럼마다 특정 값으로 결측치 채우기
values = {"A": 0, "B": 1, "C": 2, "D": 3}
print(f'[결측치 values값]df.fillna() === \n{df.fillna(value=values)}\n')

# [3] 특정 값으로 결측치 채울 개수 설정 - (limit = 1)
print(f'[limit=1]df.fillna() === \n{df.fillna(value=values, limit=1)}\n')

# [4] 다음/이전 값들로 결측치 채우기 - ffill(), bfill()
print(f"[다음 값]df.ffill() === \n{df.ffill()}\n")
print(f"[이전 값]df.bfill() === \n{df.bfill()}\n")

print(f"[다음 열의 값]df.ffill() === \n{df.ffill(axis=1)}\n")

# ------------------------------------------------------
# 보간법 - interpolate()
# ------------------------------------------------------
# 두 개 이상의 알고 있는 데이터 포인트들 사이에 예상되는 값들 추정 
print(df,"\n")
print(f"[보간법]df.interpolate() === \n{df.interpolate('linear', limit_direction='both')}\n")
