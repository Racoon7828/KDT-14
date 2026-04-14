# 컨테이너 자료형 - [4] Dictionary
# dict와 메서드
grade_dict1 = {"국어":99,"미술":80,"음악":100,"물리":80,"영어":72,"수학":81}

# 키만 보는 메서드 keys() -> dict_keys 타입 반환
keys = grade_dict1.keys()
print(f"키: {keys}")

# 값만 보는 메서드 values() -> dict_values 타입 반환
values = grade_dict1.values()
print(f"값: {values}")

# (키,값) 보는 메서드 items() -> dict_items 타입 반환
items = grade_dict1.items()
print(f"키,값: {items}", {type(items)})

# 인덱싱 방식으로 읽기 불가 => list/tuple로 형변환 후 가능
# for ~ in 반복문으로 접근은 가능
for j in values: print(j)
for i in keys: print(i)
for i, j in items: print(f'{i} - {j:>3}점')

# 값을 읽어오는 메서드 get(키, 기본값)
# 기본값 => 키가 존재하지 않을 시 반환할 값
print(grade_dict1.get("국어"))
print(grade_dict1.get("체육", "없다"))

# 값 추가 update(key:value)
grade_dict1.update({"체육":55})
grade_dict1["경제"] = 85
print(grade_dict1)

# 모든 요소 삭제 clear()
grade_dict1.clear()
print(f"{grade_dict1}")