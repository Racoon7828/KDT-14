# 컨테이너 자료형 - [3] string
# str 메서드

# 7. 문자열의 앞부분과 끝부분의 공백 제거하는 메서드 : strip()
# 문자열 사이 공백은 제거 X
msg = "   Good Luck~!!!  " # 전방 3개, 후방 2개 공백
print(f"msg 원소 개수 : {len(msg)}개, {msg}")
# 공백 모두 제거
msgall = msg.strip()
print(f"msg 원소 개수 : {len(msgall)}개, {msgall}")
# 우측 공백 제거
msgright = msg.rstrip()
print(f"msg 원소 개수 : {len(msgright)}개, {msgright}")
# 좌측 공백 제거
msgleft = msg.lstrip()
print(f"msg 원소 개수 : {len(msgleft)}개, {msgleft}")

# 8. 문자열의 앞부분과 끝부분의 특정 문자/열 제거하는 메서드 : strip()
# 문자열 사이 공백은 제거 X
data ="flower.jpg"
name_data = data.rstrip(".jpg")
print(data, name_data, sep= " ==> ")

data ="exflower.jpg"
name_data = data.rstrip(".jpg")
name_data = name_data.lstrip("e")
print(data, name_data, sep= " ==> ")

# 9. str의 끝에서 부터 인덱스 찾기 메서드
# rindex() --> 없으면 Error
# rfind()  --> 없으면 -1 반환
data = "3 1 -2 8 3 1 1 3"

idx = data.index("3")
print(idx)
idx = data.index("3", idx+1)
print(idx)
idx = data.index("3", idx+1)
print(idx)

idx = data.rindex("3")
print(idx)