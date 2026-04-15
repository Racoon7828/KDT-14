# 컨테이너 자료형 - [4] Dictionary
# 다양한 dict 추가 메서드 살펴보기
# dict에 원소/요소 읽어오는 메서드 => get()
data_dict={1:100, 2:98,3:100}
print(f"dataDict: {len(data_dict)}, {data_dict}")

# 키 존재
value = data_dict.get(2)
print(f"get(2): {value} | {data_dict}")

# 키 존재하지 않을 때
value = data_dict.get("A")
print(f"get('A'): {value} | {data_dict}")

# 키 정보만 가지고 dict 생성 메서드 : fromkeys()
keys = range(10,100,10)
data_dict = dict.fromkeys(keys)
print(f"dataDict: {len(data_dict)}, {data_dict}")

data_dict = dict.fromkeys(keys,0)
print(f"dataDict: {len(data_dict)}, {data_dict}")
