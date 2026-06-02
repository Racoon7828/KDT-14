#%%
import numpy as np
# %%
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
a
# %%
# 텍스트 모드로 저장
# 1,2,3
# 4,5,6
f = open("data.txt", "w")
rows, cols = a.shape
for y in range(rows):
    for x in range(cols):
        f.write(str(a[y, x]))
        f.write(",")
    f.write("\n")
f.close()

# %%
# data.txt 불러오기
f = open("data.txt", "r")
data = []
for line in f.readlines():
    row = []
    for num in line.strip().split(","):
        if num == "": continue
        row.append(int(num))
    data.append(row)
np.array(data)

# %%
import pandas as pd

# ','를 기준으로 컬럼을 나누고
# '\n'를 기준을 행을 나누는 포맷
pd.read_csv("data.txt")

# %%
# csv 외
# xml, json, yaml, html
# 과거 xml
# 현재 json
# 서버 - 클라이언트 통신을 위해 최초 제작
# javascript-python dictionary, list를 기본 지원 
# python에서도 json 매우 잘 어울림

import json
# json은 numpy룰 그대로 저장 못함
json.dump(a.tolist(), open('data.json', 'w'))

# %%
# 오픈한 파일을 f.close하지 않아도 운영체제에서 알아서 실행 후 닫아주긴 한다.
open('data.json', 'r').readlines
# %%
a = np.array(json.load(open('data.json')))
a

# %%
import pickle
pickle.dump(a, open('data.pkl', 'wb'))

# %%
a = pickle.load(open('data.pkl', 'rb'))
a

# %%
np.save('asdf.npy', a)
# %%
np.load('asdf.npy')
# %%
