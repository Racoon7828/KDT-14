#  -----------------------------------------------------------------
# 반복가능한 타입의 원소에 인덱스를 제공해주는 내장함수 - enumerate()
# 사용 : for ~ in 반복문에서 요소/원소 인덱스 필요한 경우 사용
#  -----------------------------------------------------------------
datas = ['Good', 2006, 'Happy', '좋은날']

# [문제] 원소 중 str 타입이 아닌 것은 str타입으로 변환 후 저장
# for d in datas: 
#     if isinstance(d, int):
#         datas[] = str(d)

for idx in range(len(datas)):
    if isinstance(datas[idx], int):
        datas[idx] = str(datas[idx])
        print(type(idx))

# for ~ in 반복에서 원소에 번호부여 하는 내장함수
for cnt, d in enumerate(datas):
    if not isinstance(d, str):
        datas[cnt] = str(d)
    print(type(d))
    print(d)
