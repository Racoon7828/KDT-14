## ==============================================================
# DataFrame/Series에서 행/열/원소 삭제
## ==============================================================
# [1] 모듈/패키지 로딩
import pandas as pd

# [2] DataFrame 인스턴스 생성
df = pd.DataFrame([[10, 20, 30, 40.],
                  [11, 22, 33, 44.]],
                  columns=['영','일','이','삼'],
                  index=['row0', 'row1'])
print("===df", df,sep="\n")

# -----------------------------------------------------------------
# [3] DataFrame 삭제
# -> 삭제할 인덱스
# -> 삭제할 방향 : 행 0 또는 index, 열 1 또는 columns
# -> 원본 사용 여부 : inplace = True 원본 사용
# ->                inplace = False 복사본 사용
# -----------------------------------------------------------------
# [3-1] 열/컬럼 삭제
# '이' 컬럼 삭제
c_df = df.drop('이', axis=1) # 원본유지
df.drop('이', axis=1, inplace=True) # 원본삭제
print("\n===c_df",c_df,sep="\n")
print("\n===df",df,sep="\n")

# '삼' 컬럼 삭제
c_df = df.drop(columns='삼', inplace=True) # 원본삭제
print("\n===df",df,sep="\n")

df = pd.DataFrame([[10, 20, 30, 40.],
                  [11, 22, 33, 44.]],
                  columns=['영','일','이','삼'],
                  index=['row0', 'row1'])

# '영','삼' 컬럼 삭제
c_df = df.drop(columns=['영','삼']) # 원본유지
print("\n===c_df",c_df,sep="\n")

# [3-2] 행 삭제
c_df = df.drop('row1')
print("\n===c_df1",c_df,sep="\n")

c_df = df.drop(['row0','row1'])
print("\n===c_df1",c_df,sep="\n")

# -----------------------------------------------------------------
# [4] Series 삭제
# -----------------------------------------------------------------
# Series 데이터 추출
sr = df.iloc[-1]
print('\n',sr)

# 원소 삭제
c_sr = sr.drop(['영','삼'])
print('\n',c_sr)
