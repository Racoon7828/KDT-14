# Iterable 타입 : 반복이 가능한 데이터 타입
#              => for ~ in 반복문으로 요소 추출 가능한 타입들
#              => 확인 : 메서드에 __iter__() 존재
#  -----------------------------------------------------------------
# for ~ in 반복문에서 __iter__(), __next__() 사용됨
iterator = [10,20,30].__iter__()
try:
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
except StopIteration:
    print("반복 종료")
finally:
    print(f"END\n")
    
#  -----------------------------------------------------------------
# 내장함수 : 반복자를 생성 또는 가져오는 함수 : iter(반복가능한타임)
#           다음 요소/원소 가져오는 내장함수 : next(반복자)
#  -----------------------------------------------------------------
nums = [4,7,-1,3,5]
niterator = iter(nums)
try:
    print(next(niterator))
    print(next(niterator))
    print(next(niterator))
    print(next(niterator))
    print(next(niterator))
    print(next(niterator))
    print(next(niterator))
except StopIteration:
    print("반복 종료")
finally:
    print("END\n")

#  -----------------------------------------------------------------
# 내장함수 : 특정값이 나올때까지만 반복해주는 함수 : iter(함수이름, 특정값)
#           => 사용자 정의 함수때 실습

