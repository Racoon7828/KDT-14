# 제어문 - [1] 조건문 : 조건에 맞는 코드 실행 문법
# if 조건구문:
#   실행코드
# else:
#   실행코드

# ex) msg가 존재하면 msg 화면 출력, 없으면 출력 X
print("---예제 코드 실행---")
msg=""
if len(msg):
    print("msg", msg)
else:
    print("없음")
print("---예제 코드 종료---")

# 
uName = input("이름?").strip()
if len(uName):
    print(f"당신 이름은 {uName}이군요!")
else:
    print("재입력")

