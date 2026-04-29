# 【사용 데이터】 --------------------------------------------------------------------- 
# 다음 데이터를 이용하여 students DataFrame을 생성하세요.
# 상품코드 상품명 가격 재고 카테고리
# P001 노트북 1200000 5 전자제품
# P002 마우스 25000 30 전자제품
# P003 의자 85000 12 가구
# P004 책상 150000 7 가구
# P005 키보드 45000 20 전자제품
# -------------------------------------------------------------------------------------- 
import pandas as pd
product = {'상품코드':['P001','P002', 'P003', 'P004', 'P005'],
            '상품명':['노트북','마우스', '의자', '책상', '키보드'],
            '가격':[12000000,25000,85000,150000,45000],
            '재고':[5,30,12, 7,20],
            '카테고리':['전자제품','전자제품','가구','가구','전자제품'],}
product = pd.DataFrame(product)
print(product,'\n')

# 문제 01) products DataFrame의 인덱스를 출력하세요. 
print(product.index,'\n')

# 문제 02) 상품코드 열을 인덱스로 설정한 products2 DataFrame을 생성하세요. 
product2 = product.set_index(['상품코드'])
print(product2,'\n')

# 문제 03) products2 DataFrame에서 인덱스가 P003인 행을 선택하여 출력하세요. 
print(product2.loc['P003'],'\n')

# 문제 04) products2 DataFrame에서 P001, P004, P005 행을 선택하여 출력하세요. 
print(product2.loc[['P001','P004','P005']],'\n')

# 문제 05) products2 DataFrame에서 P002부터 P004까지 선택하여 출력하세요. 
print(product2.loc['P002':'P004'],'\n')

# 문제 06) products2 DataFrame의 인덱스 이름을 code로 변경하세요. 
product2.index.name = "code"
print(product2,'\n')

# 문제 07) products2 DataFrame의 인덱스를 다시 일반 컬럼으로 되돌리세요. 
product2 = product2.reset_index()
print(product2,'\n')

# 문제 08) 상품명 열을 인덱스로 설정한 products3 DataFrame을 생성하세요. 
product3 = product.set_index('상품명')
print(product3,'\n')

# 문제 09) products3 DataFrame에서 인덱스 값 노트북을 고성능노트북으로 변경하세요.
# product3.index = ["고성능노트북",'마우스', '의자', '책상', '키보드']

# rename() : 변경해야되는 인덱스만 설정하면됨
# -> index 매개변수 = {이전인덱스:새인덱스}
# -> columns 매개변수 = {이전인덱스:새인덱스}
product3 = product3.rename(index = {"노트북":"고성능노트북"})
print(product3,'\n')

# 문제 10) products3 DataFrame의 인덱스를 오름차순으로 정렬하세요.
product3 = product3.sort_index()
print(product3,'\n')

# 문제 11) products3 DataFrame의 인덱스를 내림차순으로 정렬하세요. 
product3 = product3.sort_index(ascending=False)
print(product3,'\n')

# 문제 12) products3 DataFrame의 인덱스를 초기화하여 0, 1, 2, 3, 4 형태의정수 인덱스로 변경하세요. 
product3 = product3.reset_index()
print(product3,'\n')


# 문제 13) 다음 Series를 생성한 후, 인덱스에 중복 값이 있는지 확인하세요. 
s = pd.Series( [10, 20, 30, 40], index=["A", "B", "A", "C"])
print(s)
print(s.index.has_duplicates)
print(s.index.duplicated())

# 문제 14) 문제 13의 Series에서 인덱스가 A인 값을 선택하여 출력하세요.
print(s['A'])

# 문제 15) 다음 조건을 모두 수행하세요. 
# → products DataFrame에서 상품코드를 인덱스로 설정하세요. 
product = product.set_index(['상품코드'])
# → 인덱스 이름을 product_code로 변경하세요.
product.index.name = 'product_code'
# → P002와 P005 행을 선택하세요. 
print(product.loc[['P002','P005']],'\n')
# → P004 상품의 가격을 170000으로 수정하세요. 
product.loc['P004','가격'] = 17000
# → 인덱스를 다시 일반 컬럼으로 초기화하세요. 
product = product.reset_index()
# → 최종 DataFrame을 출력하세요.
print(product)
