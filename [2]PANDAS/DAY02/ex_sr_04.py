#===========================================
# 시리즈 인스턴스 생성과 데이터 자료형
#===========================================
# List/Tuple/Set/Str 데이터 => Series
# Dict 데이터 => Series
#===========================================
# [1] 모듈로딩 
import pandas as pd, func

# [2] Series 객체 생성
# 데이터 준비
data1 = [11,33,55,77]
data2 = 111,333,554,777
data3 = {1,3,5,7,7,7}
data4 = {'A':90, 'B':80}
data5 = 'Good'

# [3] Series 인스턴스 생성
sr1 = pd.Series(data1)
sr2 = pd.Series(data2)
# sr3 = pd.Series(data3) # unsequence type 불가
sr4 = pd.Series(data4)   # dict => Series key -> index
sr5 = pd.Series(data5)

# [4] 인스턴스 정보 확인
func.print_info(sr1, "sr1")
func.print_info(sr2, "sr2")
# func.print_info(sr3, "sr3")
func.print_info(sr4, "sr4")
func.print_info(sr5, "sr5")
