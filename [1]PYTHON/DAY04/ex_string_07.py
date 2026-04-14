# 컨테이너 자료형 - [3] string
# str 메서드

# 11. 원하는 출력 형태 설정을 위한 메서드 : format()
# "{} {}".format({}데이터)

# ex) 2026년도 수능일자는 11월 12일 입니다.
# index 방식 : "{0}, {1}, {2}".format(0번 인덱스, 1번 인덱스, ...)
# {} 개수보다 데이터가 적으면 Error
d_day = "{}년도 수능일자는 11월 {}일 입니다.".format(2026, 12)
print(d_day)
d_day = "{1}년도 수능일자는 11월 {0}일 입니다.".format(2026, 12)
print(d_day)

# name 방식 : "{age} {birth}".format(age= 데이터, birth= 데이터)
d_day = "{year}년도 수능일자는 11월 {day}일 입니다.".format(year=2026, day=12)
print(d_day)

# f-string = name 방식
year, day = 2026, 12
d_day = f"{year}년도 수능일자는 11월 {day}일 입니다."
print(d_day)

# 12. {} 안에 데이터 출력에 대한설정 : format()
#  {index 또는 name:설정부분}
# 사용하는 칸수 설정
# 데이터 정렬 방식 설정
# {index 또는 name:칸수}                            {0:10}
# {index 또는 name:정렬방식칸수}                     {0:<10} {0:^10} {0:>10}
# {index 또는 name:공백설정정렬방식칸수}              {0:*^10}
# {index 또는 name:공백설정정렬방식칸수.실수자릿수f}    {0:*^10.2F}  
msg = "Good Luck"
print("\n[기본] 오늘 남길 말 : {}!".format(msg))
print("[설정] 오늘 남길 말 : {:>15}!".format(msg))
print("[설정] 오늘 남길 말 : {:<15}!".format(msg))
print("[설정] 오늘 남길 말 : {:=^15}!".format(msg))

msg = "Happy New Year 2027! Good Luck"
print("[설정] 오늘 남길 말 : {:=^15}!".format(msg))

# => 파일을 복사 저장시 파일명을 이미지_001.jpg, 이미지_016.jpg
for i in range(1,11):
    filename = "파일명_{:0>3}.jpg".format(i)
    print(filename)