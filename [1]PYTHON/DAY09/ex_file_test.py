## =======================================================
## 파일 복사 기능 구현
## - 파일명 : member.txt
## - 구 현  :
## - (1) member.txt 파일 생성
##        이름 성별 지역
## ---------------------------------
##       홍길동 남자 부산
##       마징가 여자 대구
##       김철수 남자 서울
## =======================================================
data =  r'C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY09\member.txt'
with open(data, "w",encoding="utf8") as f:
    f.write("""이름 / 성별 / 지역\n---------------------------------\n홍길동 / 남자 / 부산\n마징가 / 여자 / 대구\n김철수 / 남자 / 서울""")

## =======================================================
# - 복사 기능
# member_copy.txt
## =======================================================
# 원본 파일 내용 ---> 복사 파일 넣기
data_copy =  r'C:\Users\Win11Pro\Desktop\KDT-14\[1]PYTHON\DAY09\member_copy.txt'
with open(data, "r",encoding="utf8") as r:
    with open(data_copy, "w",encoding="utf8") as w: w.write(r.read())
