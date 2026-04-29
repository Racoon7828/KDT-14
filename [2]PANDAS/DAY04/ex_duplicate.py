# ======================================================
# 중복 데이터 검사 및 처리 - 중복
# ------------------------------------------------------
# -> 검사 : DataFrame.duplicated() True/False 반환 
# -> 처리 : DataFrame.drop_duplicates() 
# ======================================================
# [1] 모듈 로딩
import pandas as pd, numpy as np

# [2] 데이터 준비
df = pd.DataFrame( {'brand' : ['Yum', 'Yum', 'Indo', 'Indo', 'Indo'],
                    'style' : ['cup', 'cup', 'cup', 'pack', 'pack' ],
                    'rating': [4, 4, 3.5, 15, 5]})

## DF 출력
print(df,"\n")

# ------------------------------------------------------
# 중복 데이터 검사 - DataFrame.duplicated()
# ------------------------------------------------------
# 행단위로 중복 여부 검사 후 True/False
dup_df = df.duplicated()
print(f'df.duplicated() === \n{dup_df}\n')
print(f'중복 개수 확인 : {dup_df.sum()}\n')

# ------------------------------------------------------
# 중복 데이터 처리 - DataFrame.drop_duplicates()
# ------------------------------------------------------
dup_df = df.drop_duplicates()
dup_df = dup_df.sort_index(ignore_index=True)
print(f'df.duplicated() === \n{dup_df}\n')

# 특정 컬럼만 중복 처리
dup_df = df.drop_duplicates(subset='brand')
print(f"subset='brand' === \n{dup_df}\n")
