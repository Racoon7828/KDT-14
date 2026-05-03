# ===========================================
# 일반적이며 공통적으로 사용되는 함수 모음 모듈
# -> 모듈명 : utils
# -> 사용법 : import sys
#            sys.path.append(C:\Users\Win11Pro\Desktop\KDT-14\[2]PANDAS\utils)
#            import utlis
# ===========================================
# 함수기능 : DataFrame 로딩후 기본 정보 출력 기능
# 함수이름 : data_info
# 매개변수 : DataFrame 인스턴스, 변수 이름
#           
# 결과처리 : X
# ===========================================
def data_info(objDF, objName=None, isall=False):
    print("\n요약정보(.info())")
    objDF.info()
    # print("========\n")

    # 실제 데이터 확인 = 기본값 상위 5개 출력
    print(f'\n상위 정보\n{objDF.head()}\n...\n{objDF.tail(3)}')

    # 컬럼별 통계 정보 확인
    if isall == True:print(f'\n모든 컬럼별 정보\n{objDF.describe(include="all")}\n')
    else:print(f'\n수치 컬럼별 정보(.describe())\n{objDF.describe()}\n')

# --------------------------------------------------------------------
# 함수기능 : 생선된 DF 인스턴스의 일부 출력 기능
# 함수이름 : print_df
# 매개변수 : msg, df
# 매개변수 : 직접 출력 / 반환 없음
# --------------------------------------------------------------------
def print_df(msg, df):
    print(f"\n[{msg}]---")
    print(df.head())
    print(f"{'-'*30}\n")




