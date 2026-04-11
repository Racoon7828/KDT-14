# 컨테이너 자료형 - [1] 순서있는 자료형 List
# 다양한 내장함수 활용
# 다양한 데이터
datas1 = []
datas2 = [5,1,62,2626,345,555]
datas3 = ['Abc', 'APPle', 'ananconda', 'zoo']

# 내장함수: sorted() -> 정렬
# 리스트로 반환
print(f'sorted(datas2) : {sorted(datas2)}, {datas2}')
print(f'sorted(datas3) : {sorted(datas3)}, {datas3}', '\n')

# 내림차순
print(f'내림차순 sorted(datas2) : {sorted(datas2, reverse=True)}, {datas2}')
print(f'내림차순 sorted(datas3) : {sorted(datas3, reverse=True)}, {datas3}', '\n')

# 내장함수: range(시작값, 끝값+1, 간격) -> 데이터 범위
# 많은 데이터 생성 시 사용하는 함수
# 데이터 범위 객체/타임 생성

# 1~10 데이터 저장
datas1=[1,2,3,4,5,6,7,8,9,10]
datas2=range(1, 11)

print(f'datas1 : {datas1}, {len(datas1)}개, {type(datas1)}')
print(f'datas2 : {datas2}, {len(datas2)}개, {type(datas2)}', '\n')

# 1~100000000
datas1=[1,2,3,4,5,6,7,8,9,10]
datas2=range(1, 100000001)

print(f'datas1 : {datas1}, {len(datas1)}개, {type(datas1)}')
print(f'datas2 : {datas2}, {len(datas2)}개, {type(datas2)}', '\n' )

# 1~30 숫자중 3의배수 저장
datas1=[3,6,9,12,15,18,21,24,27,30]
datas2=range(3, 31, 3)
print(f'datas1 : {datas1}, {len(datas1)}개, {type(datas1)}')
print(f'datas2 : {list(datas2)}, {len(datas2)}개, {type(datas2)}', '\n')

# 50 ~ 1까지 범의의 숫자 출력
datas1=list(range(50,0,-1))
print(f'datas1 : {datas1}', '\n', f'{len(datas1)}개, {type(datas1)}', '\n')
