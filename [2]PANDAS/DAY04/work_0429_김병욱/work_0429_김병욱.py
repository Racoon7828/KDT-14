# [교재]
# part3 p130 ~ p148
# part5 p260 ~ p282
import pandas as pd, sys, seaborn as sns
sys.path.append(r'C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\utils')
import utils


# read_csv() 함수로 df 생성
df = pd.read_csv(r'C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\DATA\auto_mpg.csv')

# df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','car name']

# 현재 csv 파일에서 1번째 줄에 column이 적혀있으므로 1번째 줄 컬럼 등록 후 삭제
# df.columns = df.iloc[0]
# df.columns.name = None
# 컬럼 삭제
# df.drop(0, inplace=True)

# Pandas가 데이터를 처음 읽어올 때나 행을 조작할 때, 자동으로 타입을 재해석하지 않는다.
# df = df.convert_dtypes() # => str

# df.apply 데이터프레임의 행(row)이나 열(column) 단위로 함수를 반복 적용할 때 사용
# pd.to_numeric 문자열(object) 상태인 데이터를 숫자형(int 또는 float)으로 변환
# df = df.apply(pd.to_numeric, errors='ignore')
# df = df.sort_index(ignore_index=True)

print(df.dtypes)
utils.data_info(df)

print(f"\n{df.describe(include='object')}\n")
print(f"열 === \n{df.columns}\n")
print(f"행/열 === \n{df.shape}\n")
print(f"타입 === \n{df['mpg'].dtype}\n")
print(f"원소 개수 === \n{df.count()}\n")
print(f"origins 원소 개수 === \n{df['origin'].value_counts()}\n")

# 각 고유값 개수 / 전체데이터 개수 = 상대적 구성비 - (normalize=True)
print(f"origins 구성비 === \n{df['origin'].value_counts(normalize=True)}\n")

# 상대적 구성비 - 백분율(%)
print(f"origins 구성비 === \n{(df['origin'].value_counts(normalize=True) * 100).round(1)}\n")

print(f"평균값 === \n{df.mean(numeric_only=True)}\n")
print(f"중앙값 === \n{df.median(numeric_only=True)}\n")
print(f"최대값 === \n{df.max(numeric_only=True)}\n")
print(f"최소값 === \n{df.min(numeric_only=True)}\n")
print(f"표준편차 === \n{df.std(numeric_only=True)}\n")
print(f"상관계수 === \n{df.corr(numeric_only=True)}\n")

# 누락 데이터 확인
df = sns.load_dataset('titanic')
# print(f'df\n')
print(f'titanic정보 :\n{df.info()}\n')
print(f'titanic누락 데이터 :\n{df.head().isnull()}\n')
print(f'titanic누락 데이터 수 :\n{df.isnull().sum()}\n')

# 누락 데이터 제거
df_drop = df.dropna(axis=1, thresh=500)
print(f'누락 데이터(500개이상) 제거 :\n{df_drop}\n') # => deck열 제거

df_drop = df_drop.dropna(subset=["age"],how='any', axis=0)
print(f'age 제거 :\n{len(df_drop)}\n')
print(f'age 제거 :\n{df_drop.head(8)}\n')

# 누락 데이터 대체
mean_age = df['age'].mean()
df['age'] = df['age'].fillna(mean_age)
print(f'age 평균값 대체 :\n{df["age"].head(8)}\n')

# 누락 데이터 최빈값 대체
print(f'embark_town :\n{df["embark_town"][825:830]}\n')

most_freq = df['embark_town'].mode()[0]
print(f'최빈값:\n{most_freq}\n')

df['embark_town'] = df['embark_town'].fillna(most_freq)
print(f'최빈값 대체 :\n{df["embark_town"][825:830]}\n')

df = sns.load_dataset('titanic')

# 누락 데이터 이웃값 대체
df['embark_town'] = df['embark_town'].ffill()
print(f'앞값 대체 :\n{df["embark_town"][825:831]}\n')

df = sns.load_dataset('titanic')
df['embark_town'] = df['embark_town'].ffill()
print(f'뒷값 대체 :\n{df["embark_town"][825:831]}\n')

df = pd.DataFrame({'c1':['a','a','b','a','b'],
                   'c2':[1,1,1,2,3],
                   'c3':[1,1,2,2,2],})

print(df)

# 중복 데이터 확인
# 가장 처음 행만 False (keep='first')
df_dup_first = df.duplicated()
print(f'중복 데이터 확인(first) :\n{df_dup_first}\n')

# 가장 마지막 행만 False (keep='last')
df_dup_last = df.duplicated(keep='last')
print(f'중복 데이터 확인(last) :\n{df_dup_last}\n')

# 모든 행 False (keep=False)
df_dup_false = df.duplicated(keep=False)
print(f'중복 데이터 확인(False) :\n{df_dup_false}\n')

# 중복 데이터 제거
df2 = df.drop_duplicates()
print(f'중복 데이터 제거 :\n{df2}\n')

# 가장 마지막 행 제외 제거 (keep='last')
df2 = df.duplicated(keep='last')
print(f'마지막 행 제외 제거(last) :\n{df2}\n')


