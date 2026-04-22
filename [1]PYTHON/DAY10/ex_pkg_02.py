# --------------------------------------------
# 파이썬 표준 모듈 및 패키지
# --------------------------------------------
# 날짜/시간 모듈들
# -> datetime 모듈
# -> date 모듈
# -> time 모듈
# --------------------------------------------
# 
# --------------------------------------------
import datetime, time
# 모듈 사용
print(time.ctime())

current = datetime.datetime.now()
print(f"{current.year}년 {current.month}월 {current.day}일 {current.hour}시 {current.minute}분 {current.second}초")

print(datetime.date.today().strftime('%Y-%m-%d'))
print(datetime.datetime.now().strftime('%Y년-%m월-%d일-%H시-%M분-%S초'))
print(datetime.datetime.now().strftime('%A'))


# 원하는 날짜에 관련된 datetime 타입 생성
d_day = datetime.datetime(2026, 12, 25)
print(d_day)







