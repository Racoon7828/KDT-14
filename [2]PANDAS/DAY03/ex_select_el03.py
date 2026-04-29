## ==============================================================
# DataFrame에서 행/열 원소 선택
## ==============================================================
# 
## ==============================================================
# [1] 모듈/패키지 로딩
import pandas as pd

# [2] DataFrame 인스턴스 생성
df1 = pd.DataFrame([[10, 20, 30, 40.],
                        [11, 22, 33, 44.]])

df2 = pd.DataFrame([[10, 20, 30, 40.],
                        [11, 22, 33, 44.]],
                        columns=['영','일','이','삼'],
                        index=['row0', 'row1'])

print("===df1", df1,sep="\n")
print("\n===df2",df2,sep="\n")

# [3] 원소 선택
# [3-1] 1개 원소 선택
# print("\n===row0",df2[0],sep="\n")
one_el = df2.iloc[0,3]
print("\n===",one_el,sep="\n")
print("\n===",df2.iloc[0,3],sep="\n")

print("\n===",df2.loc['row0','삼'],sep="\n")

# 행선택 후 열 지정
# one_el = df2.iloc[0][3]
# print("\n===",one_el,sep="\n")
# print("\n===",df2.iloc[0][3],sep="\n")
print("\n===",df2.loc['row0']['삼'],sep="\n")

# [3-2] 2개 이상 원소 선택 - 인덱스 리스트
print("\n===",df2.iloc[[0,1],3],sep="\n")
print("\n===",df2.loc[['row0','row1'],'삼'],sep="\n")

# => 10, 40.0, 11, 44.0 원소선택
print("\n===",df2.iloc[[0,1],[0,3]],sep="\n")
print("\n===",df2.loc[['row1','row0'],['영','삼']],sep="\n")

# [3-3] 2개 이상 원소 선택 - 인덱스 슬라이싱
print("\n===",df2.loc[:,['영','삼']],sep="\n")
print("\n===",df2.iloc[:,::3],sep="\n")
