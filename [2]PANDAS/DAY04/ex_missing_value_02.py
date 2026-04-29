# ======================================================
# 결측치 처리 - 삭제
# ------------------------------------------------------
# DataFrame.dropna() [기본] 행 단위 1개라도 결측치 있으면 삭제
# -> axis = 0       삭제 축 기준
# -> how = 'any'    삭제 방법
# -> thresh = 숫자   정상 데이터의 최소 개수 설정
# -> subset = 컬럼명 특정 컬럼만 결측치 검사
# ======================================================
# [1] 모듈 로딩
import pandas as pd, numpy as np

# [2] 데이터 준비
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                    "toy" : [np.nan, 'Batmobile', 'Bullwhip'],
                    "born" : [pd.NaT, pd.Timestamp("1940-04-25"),pd.NaT]})

## DF 출력
print(df,"\n")

# ------------------------------------------------------
# 결측치 삭제 - dropna()
# ------------------------------------------------------
# [1] 기본 설정값으로 결측치 삭제
print(f'[행단위 삭제]df.dropna() === \n{df.dropna()}\n')

# [2] 모든 데이터가 결측치면 삭제 - how = 'all'
print(f"[행단위 삭제]df.dropna() === \n{df.dropna(how='all')}\n")

# [3] 컬럼(열) 방향 삭제 - axis = 1
print(f"[열단위 삭제]df.dropna() === \n{df.dropna(axis=1)}\n")
print(f"[열단위 삭제]df.dropna() === \n{df.dropna(axis=1,how='all')}\n")

# [4] 데이터 최소 개수 삭제 - thresh = n
print(f"[최소 개수 삭제]df.dropna() === \n{df.dropna(thresh=2)}\n")

# [5] 특정 컬럼 또는 행만 삭제 - subset = ['컬럼명']
print(f"[특정 컬럼 삭제]df.dropna() === \n{df.dropna(subset=['name','toy'])}\n")
print(f"[생년월일 결측치인 행 삭제]df.dropna() === \n{df.dropna(subset=['born'])}\n")
