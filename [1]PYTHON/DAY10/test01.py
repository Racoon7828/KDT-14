# ================================================
# 문제 1. 메모 저장 기능 만들기
# ------------------------------------------------
# 구현 : 간단한 메모 프로그램의 저장 기능. 
#
# 요구사항
# -> 사용자에게 메모 내용을 입력받기.
# -> 날짜별 폴더 생성 및 해당 날짜 폴더에 파일 저장.
#    폴더 생성 함수는 import os 
#                   os.mkdir("폴더명")
# -> 입력받은 내용을 memo_YYYY_MM_DD.txt 파일에 저장.
# -> 저장이 끝나면 "메모가 저장되었습니다."를 출력.
#
# 저장 형식
# -> 날짜
# -> 메모 내용
# -> 기존 내용은 유지하고 새 내용은 뒤에 추가
# ================================================
# 1. 폴더 존재 여부 체크
# -> 없으면 생성 os.mkdir("TEST")
# 2. 내용 입력
# -> input()
#  
# 3. 메모저장
# -> memo_YYYY_MM_DD.txt 파일에 저장
# -> -> 저장이 끝나면 "메모가 저장되었습니다."를 출력.
# 
# 4. 함수구현
# -> 범위 : 입력따로, 저장 따로
#           메모 저장 기능 함수로
# -> 함수기능 : 메모내용 저장
# -> 매개변수 : 날짜, 내용
# -> 함수결과 : 저장 여부 메시지 출력
# ================================================
import os, datetime
def write_memo():
    today = datetime.date.today().strftime('%Y-%m-%d')
    now = datetime.datetime.now().strftime('%Y년-%m월-%d일-%H시-%M분')
    if "TEST" == False: os.mkdir("TEST")
    memo = f"C:/Users/Win11Pro/Desktop/KDT-14/TEST/memo_{today}.txt"
    user_memo = input("메모 입력: ")
    with open(memo, "a", encoding="utf8") as f:
        f.write(f"\n{[now]}\n{user_memo}\n")
        print("메모가 저장되었습니다.")
# write_memo()

# datetime 모듈 안쓰고
def save_memo(wdate, memo):
    memo_path = r"C:\Users\Win11Pro\Desktop\KDT-14\TEST"
    # (1) Memo 폴더 존재 여부
    os.mkdir("TEST") if not os.path.exists(memo_path) else print(f"{memo_path}가 존재합니다")
    # (2) 파일에 기록
    file_path = f"{memo_path}/memo_{wdate}.txt"
    wCnt = 0
    with open(file_path, "a", encoding="utf8") as f:
        wCnt = f.write("\n[Memo-1]\n")
        wCnt = f.write(memo+"\n")

    # (3) 저장 여부 출력
    msg = "저장실패" if not os.path.exists(file_path) else f"{wCnt}개 데이터 저장완료"
    print(msg)

# 입력 받은 메모 저장
# 입력 => 날짜, 메모 내용
def input_save_memo():
    inData = input("날짜와 메모내용 입력(예: 2026_03_01 내용입니다): ").strip().split()
    if len(inData)>=2:
        # 0번째 원소는 날짜
        if inData[0].replace("_","").isdecimal():
            # 1번째 원소부터는 메모 내용
            memo = "".join(inData[1:])
            save_memo(inData[0], memo)
        else: print("YYYY_MM_DD 형식의 날짜가 아닙니다.")
    else: ("날짜와 메모내용중 누락된 부분이 있습니다.")
# input_save_memo()

# ================================================
# 문제 2. 회원 추가 기능 만들기
# ------------------------------------------------
# 구현 : 회원 관리 프로그램의 회원 등록 기능.
#
# 요구사항
# -> 사용자에게 연락처, 이름, 지역, 직업, 취미 입력받기.
# -> 입력받은 정보를 users.txt 파일에 추가 저장.
# -> 이미 저장된 회원 정보는 유지되어야 함.
# -> 저장 후 "회원 등록 완료" 출력.
# -> 이미 존재하는 회원이면 "이미 등록되어 있습니다" 출력.

# 저장 형식
# -> 연락처         이름   지역  직업     취미
# -> 010-2222-1111 홍길동 대구 운동선수 태권도
# ================================================
# 1. 관련 기능 폴더 및 파일명 설정
# -> 폴더명 : Member 폴더
#    파일명 : users.txt
# 
# 2. 회원 등록 기능
# -> 함수이름: join_user
# -> 매개변수 : 연락처, 이름, 지역, 직업, 취미
# -> 함수기능 : users.txt 파일에 계속 추가
#              등록 데이터 검사
#              존재하는 회원일 경우 추가 X
#              미존재하는 회원만 추가, 메세지 출력
#  
# 3. 폴더 및 저장 파일 준비기능
# -> 함수이름 : create_dir_file
# -> 매개변수 : 생성할 폴더 또는 파일 경로
# -> 폴더 또는 파일 생성
# -> Member폴더 존재여부 체크 후 준비
#    users.txt 파일에 첫번째 줄 기록 되어 있어야 함
# ================================================
def user_info():
    memo = r"C:\Users\Win11Pro\Desktop\KDT-14\TEST\user.txt"
    info = input("연락처/이름/지역/직업/취미 :").split()
    with open(memo, "r", encoding="utf8") as f:
        f.write(f"\n{'연락처':<15}{'이름':<10}{'지역':<10}{'직업':<10}{'취미':<10}\n")
        for i in info:
            if 10 < len(i):f.write(f"{i:<15}")
            else:f.write(f"{i :<10}")
        print("정보가 저장되었습니다.")
# user_info()

MEMO_PATH = r"C:\Users\Win11Pro\Desktop\KDT-14\TEST"
MEMBER_PATH = r"C:\Users\Win11Pro\Desktop\KDT-14\TEST\MEMBER"
USER_FILE = f"{MEMBER_PATH}\\user.txt"

def create_dir_file(path, isfile=False):
    if not os.path.exists(path):
        # 폴더 생성
        if not isfile: os.mkdir(path) 
        else: 
            # 파일 생성
            with open(USER_FILE, "x", encoding="utf8") as f:
                f.write(f'{"연락처":<15}{"이름":<10}{"지역":<10}{"직업":<10}{"직업":<10}\n')
        return os.path.exists(path)
    else:
        return True

def join_user(phone, name, loc, job, hobby):
    # 연락처 데이터 형식 및 구성 검사
    if phone.replace("-","").isdecimal():
        # 파일 데이터 추출
        with open(USER_FILE, "r", encoding="utf8") as f:
            allDatas = f.read()

        # 중복 여부 체크
        if phone in allDatas:
            print(f"{phone} 이미 등록된 회원입니다")

        else:
            # 새로운 회원 추가
            with open(USER_FILE, "a", encoding='utf8') as f:
                wCnt=f.write(f"{phone:<15}{name:<10}{loc:<10}{job:<10}{hobby:<10}\n")
                print(f"{wCnt}개 데이터 저장")
    else: print("유효한 데이터가 아닙니다.")

if create_dir_file(MEMBER_PATH) and create_dir_file(USER_FILE, True):
    print("폴더 및 파일 준비 완료")

    # 등록 요청 메시지
    indata = input("회원등록 연락처, 이름, 자역, 직업, 취미 입력: ").strip().split(",")

    # 등록 정보 체크
    if len(indata)==5: join_user(*indata)
    else: print("필수 회원 정보 연락처, 이름, 지역, 직업, 취미가\n모두 입력되었는지 확인 바랍니다.")
else: print("폴더 및 파일 문제 체크 필요")
