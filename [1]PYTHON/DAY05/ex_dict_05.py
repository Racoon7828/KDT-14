# 컨테이너 자료형 - [4] Dictionary
# Key : unique, 반드시 존재
# ex) 학생 정보 저장
# 이름, 성별, 전공, 나이, 학점 => 학생별 학점을 저장하길 원함!
student_dict = {"홍길동":4.1, "마징가": 3.7, "배트맨":3.2, "홍길동":4.3}
print(f"학생정보: {len(student_dict)}명\n{student_dict}\n")

# 유니크한 키 조합 - 이름 + 전공
# 키 저장 후 변경이 되면 안됨 (list) -> tuple 사용 
student_dict = {("홍길동", "컴공"):4.1, ("마징가", "기계공"):3.7, ("배트맨", "컴공"):3.2, ("홍길동", "기계공"):4.3}
print(f"학생정보: {len(student_dict)}명\n{student_dict}\n")

# 튜플 타입의 키로 데이터 다루기
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items(),"\n")

# 원소의 데이터 읽기 : 변수명[(키묶음)]
print(student_dict[("홍길동", "컴공")])
print(student_dict[("홍길동", "기계공")])
