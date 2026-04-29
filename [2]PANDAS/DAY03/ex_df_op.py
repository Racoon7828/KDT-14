## ===============================================
## DataFrame 연산
## ===============================================
# [1] 모듈 로딩
import pandas as pd

# [2] Series인스턴스 생성
df1 = pd.DataFrame([[11,22,33], 
                   [10,20,30]])

# ------------------------------
# [3] 연산
# ------------------------------
# [3-1] DataFrame과 숫자 연산
# ------------------------------
print(f"\ndf1 + 10 = \n{df1 + 10}")
print(f"\ndf1 * 10 = \n{df1 * 10}")
print(f"\ndf1 >= 10 = \n{df1 > 20}")

# ------------------------------
# [3-2] DataFrame과 DataFrame 연산
# ------------------------------
df2 = df1 * 2
print(f"\ndf1 + df2 = \n{df1 + df2}")
print(f"\ndf1 * df2 = \n{df1 * df2}")
print(f"\ndf1 > df2 = \n{df1 > df2}")

df2.index = [0,2]
print(f"\ndf1 + df2 = \n{df1 + df2}")
print(f"\ndf1 * df2 = \n{df1 * df2}")
print(f"\ndf1 % df2 = \n{df1 % df2}")

# ------------------------------
# [3-3] DataFrame연산 관련 메서드 활용
# -> 같은 인덱스가 없는 경우 : NaN
# -> 데이터가 NaN인 경우    : NaN
# => 해결 : fill_value 매개변수
# ------------------------------
print(f"\ndf1 + df2 = \n{df1.add(df2, fill_value=0)}")
print(f"\ndf1 * df2 = \n{df1.mul(df2, fill_value=1)}")





