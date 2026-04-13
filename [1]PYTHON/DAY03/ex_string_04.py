# 컨테이너 자료형 - [3] string
# str 메서드
msg = ("Good Luck"+" ") * 3

# 4. 원소/요소 변경 후 반환 : replace("바뀔거", "바꿀거", 갯수 만큼)
# 변환된 새로운 str 반환 (원본 str 변경 안됨)
new_msg = msg.replace("G", "g")
print(f"{msg} => {new_msg}")
new_msg = new_msg.replace("L", "l", 2)
print(f"{msg} => {new_msg}")

# 5. 1개 str => 여러개 str 분리 : split()
# 공백문자(" ") 기준으로 분리(기본값)
# 메서드 사용 시 분리 기준(문자/문자열) 설정 가능
# 리스트에 여러개 분리된 str 담아서 반환
data = "Happy New Year 2026!!"
ret = data.split()
print(f"data : {data}, {type(data)}, {len(data)}개")
print(f"ret : {ret}, {type(ret)}, {len(ret)}개")

# ret = data.split("e")
# print(f"data : {data}, {type(data)}, {len(data)}개")
# print(f"ret : {ret}, {type(ret)}, {len(ret)}개")

# 6. 여러개 str => 1개 str 연결 : join()
# 연결문자 지정
new_data = "-".join(ret)
print(f"\nnew_data : {new_data}, {type(new_data)}, {len(new_data)}개")
print(ret, new_data, sep=" => ")

