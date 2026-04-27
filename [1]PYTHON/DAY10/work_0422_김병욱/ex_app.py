## =================================================
##      메모 관리 프로그램  - MEMO APP
## =================================================
## -> 주요기능 : 메모 저장, 삭제, 보기 
## =================================================
## -------------------------------------------------
## 모듈 로딩
## -------------------------------------------------
import os, datetime

## -------------------------------------------------
## 전역변수
## -------------------------------------------------
MEMO_DIR = r'C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY10\work_0422_김병욱\Memo'
M_VIEW, M_SAVE, M_EXIT = list('123')
M_MEMO, M_ADJUST, M_DELETE, M_RETURN = list('1234')

## -------------------------------------------------
## 사용자정의 함수 
## -------------------------------------------------
## 함수기능 : 메뉴 출력
## 함수이름 : print_menu
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------
def print_menu():
    print("="*30)
    print(f"{'MENU':^30}")
    print("="*30)
    print("1.메모보기")
    print("2.새메모쓰기")
    print("3.종료")
    print("="*30)

## -------------------------------------------------
## 사용자정의 함수 
## -------------------------------------------------
## 함수기능 : 메뉴 출력
## 함수이름 : print_memo_menu
## 1.메모 보기 출력 메뉴 
## -------------------------------------------------
def print_memo_menu():
    print("1.선택메모보기")
    print("2.선택메모수정")
    print("3.선택메모삭제")
    print("4.뒤로")
    print("="*30)

def print_stat(msg):
    print("="*30)
    print(f"{msg:^30}")
    print("="*30)

## -------------------------------------------------
## 함수기능 : 메모 목록 출력
## 함수이름 : print_meno
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------
def print_memo():
    mlist = os.listdir(MEMO_DIR)
    print("="*30)
    print(f"{'-메모목록-':^30}")
    print("="*30)
    for m in mlist:
        print(m)
    print("="*30)

## -------------------------------------------------
## 함수기능 : 메모 내용 보기
## 함수이름 : view_memo
## 메모 번호 입력하면 메모 읽어오기 (r)
## -------------------------------------------------
def view_memo():
    ## 메모 선택
    mitems = [f for f in os.listdir(MEMO_DIR) if '.memo' in f and f.endswith('.txt')]
    try:
        choice = int(input("메모 번호를 입력하세요. (취소: 0): ").strip())
        if 1 <= choice <= len(mitems):
            selected_file = mitems[choice - 1]
            with open(f'{MEMO_DIR}/{selected_file}', mode='r', encoding='utf8') as F:
                print("="*30)
                print(F.read())
        elif choice == 0: 
            print_memo()
            return
        else: print('존재하지 않는 메모입니다.')
    except ValueError: 
        print("="*30)
        print("숫자 제대로 입력하십시오. 휴먼")
    print_memo()

## -------------------------------------------------
## 함수기능 : 메모 삭제
## 함수이름 : adjust_memo
## 메모 번호 입력하면 메모 수정 후 덮어쓰기 (w)
## -------------------------------------------------
def adjust_memo():
    ## 메모 선택
    mitems = [f for f in os.listdir(MEMO_DIR) if '.memo' in f and f.endswith('.txt')]
    try:
        choice = int(input("수정할 메모 번호를 입력하세요. (취소: 0): ").strip())
        if 1 <= choice <= len(mitems):
            selected_file = mitems[choice - 1]
            memo = input(f"메모 내용입력: ")
            with open(f'{MEMO_DIR}/{selected_file}', "w", encoding="utf8") as f: f.write(memo)
        elif choice == 0: 
            print_memo()
            return
        else: print('존재하지 않는 메모입니다.')
    except ValueError: 
        print("="*30)
        print("숫자 제대로 입력하십시오. 휴먼")
    print_memo()

## -------------------------------------------------
## 함수기능 : 메모 삭제
## 함수이름 : delete_memo
## 메모 번호 입력하면 삭제
## 삭제 후 메모 번호 재정렬
## -------------------------------------------------
def delete_memo():
    mitems = [f for f in os.listdir(MEMO_DIR) if '.memo' in f and f.endswith('.txt')]
    if not mitems:
        print("삭제할 메모가 없습니다.")
        return
    
    try:
        choice = int(input("삭제할 번호를 입력하세요. (취소: 0): ").strip())
        if choice == 0: 
            print_memo()
            return
        elif 1 <= choice <= len(mitems):
            selected_file = mitems[choice - 1]
            os.remove(f'{MEMO_DIR}/{selected_file}')
            # 파일 이름 재정렬 (젬미니 물어봄)
            remaining_files = [f for f in os.listdir(MEMO_DIR) if '.memo_' in f and f.endswith('.txt')]
            remaining_files.sort()
            for i, filename in enumerate(remaining_files, 1): # enumerate =  인덱스와 원소로 이루어진 튜플(tuple)을 만들어 준다
                parts = filename.split('.', 1) 
                if len(parts) < 2: continue
                content_part = parts[1]
                new_filename = f"{i}.{content_part}"
                if filename != new_filename: os.rename(f'{MEMO_DIR}/{filename}', f'{MEMO_DIR}/{new_filename}')
        else: print("잘못된 번호입니다.")
    except ValueError: 
        print("="*30)
        print("숫자 제대로 입력하십시오. 휴먼")
    print_memo()

## -------------------------------------------------
## 함수기능 : 메모 저장 
## 함수이름 : save_meno
## 현재 날짜로 새 메모 작성
## 메모 앞에 번호 붙이기
## -------------------------------------------------
def save_memo():
    mitems = [f for f in os.listdir(MEMO_DIR) if '.memo' in f and f.endswith('.txt')]
    numbering = []
    for f in mitems:
        num = int(f.split('.')[0])
        numbering.append(num)
    
    next_num = max(numbering) + 1 if numbering else 1

    today = datetime.date.today().strftime('%Y_%m_%d')
    item = f'{next_num}.memo_{today}.txt'
    filepath = f'{MEMO_DIR}/{item}'
    
    memo = input(f"[{item}] 메모 내용입력: ")
    with open(filepath, "w", encoding="utf8") as f: f.write(memo)
    print(f"'{item}' 저장 완료")

## -------------------------------------------------
## 함수기능 : 메모 메뉴
## 함수이름 : memo_menu
## -------------------------------------------------
def memo_menu():
    while True:
        print_memo_menu()
        choice = input("메뉴 선택(1~4):").strip()
        if choice == M_MEMO:
            view_memo()
        elif choice == M_ADJUST:
            adjust_memo()
        elif choice == M_DELETE:
            delete_memo()
        elif choice == M_RETURN:
            print("메인 메뉴로 돌아갑니다.")
            break
        else:
            print(f"{choice}는 유효하지 않은 메뉴입니다.")

## =================================================
## 프로그램 구동
## =================================================
if __name__ == '__main__':
    print_stat('MEMO APP START')

    while True:
        print_menu()
        choice = input("메뉴 선택(1~3):").strip()
        if choice not in [M_VIEW, M_SAVE, M_EXIT]:
            print(f"{choice}는 유효하지 않은 메뉴입니다.")
        elif choice == M_VIEW:
            print_memo()
            memo_menu()
        elif choice == M_SAVE:
            save_memo()
        else:
            print("사용자 요청으로 종료합니다.")
            break

    print_stat('MEMO APP END')