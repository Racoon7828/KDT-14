## ==============================================================
# CSV 파일 => 표 형태 즉, DataFrame으로 읽기
## ==============================================================
# 사용함수 : read_csv("경로/파일명.csv", 옵션들...)
## ==============================================================
# [1] 모듈/패키지 로딩
import pandas as pd, numpy as np

# [2] csv 데이터 읽어오기
DATA_FILE = 'C:/Users/Win11Pro/Desktop/KDT-14/[2]PANDAS/DATA/iris.csv'
data_frame = pd.read_csv(DATA_FILE)

# [3] csv 데이터 확인
print("\n============== CSV => 전체 데이터 프레임 ==============", data_frame)
print("\n============== 속성들 ==============")
print(f"index : {data_frame.index}")
print(f"columns : {data_frame.columns}")
print(f"shape : {data_frame.shape}")
print(f"dtypes: {data_frame.dtypes}")



data_frame = np.array(data_frame)
