# 컨테이너 자료형 - [3] string
# str 메서드
msg = "Good Luck"

# 1. 원소/요소의 인덱스 반환 => find()
# 대소문자 일치
print(msg.find("L"))
print(msg.find(" Lu")) 
def find_idx(i):
    idx = msg.find(i)
    if idx == -1: # 인덱스 없을시 -1 반환
        return "읎다"
    else:
        return idx
print(find_idx("a"))
print(find_idx("Lu"))

# 2. 원소/요소 대소문자 변환
print(msg.lower()) # 소문자
print(msg.upper()) # 대문자
print(msg.swapcase()) # 대/소문자 반대로

# 3. 원소/요소 검사 : isXXXX() => True/False
msg = "Happy"
phone = "01011112222"
userid = " k1234"
print(f"\n{msg}.isalpha() :  {msg.isalpha()}")
print(f"{phone}.isalnum() :  {phone.isalnum()}")
print(f"{userid}.isdecimal() :  {userid.isdecimal()}")
print(f"{userid}.isalnum() :  {userid.isalnum()}")

def isXXXX(msg):
  if msg.isalpha == True:
    return "알파벳"
  elif msg.isalnum == True:
    return "숫자"
  else:
     return False
  
# 3. 원소/요소 검사 : isXXXX() => True/False
msg1 = "Good"
msg2 = "HAPPY"
msg3 = "    "

print(f"\n{msg1}.isupper() :  {msg1.isupper()}")
print(f"{msg2}.isupper() :  {msg2.isupper()}")
print(f"{msg3}.isspace() :  {msg3.isspace()}") # 공백
