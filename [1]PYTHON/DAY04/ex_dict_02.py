# 컨테이너 자료형 - [4] Dictionary
# dict와 연산자
grade_dict1 = {"국어":99,"미술":80,"음악":100,"물리":80,"영어":72,"수학":81}
grade_dict2 = {"국어":100,"체육":70,"경제":100}

# 1. 연산자 : 덧셈 dict + dict - 미지원
# new_dict = grade_dict1 + grade_dict2
# print(new_dict)

# 2. 멤버 연산자 : in - 지원
# key만 가능
print(f"'경제' in grade_dict2 = {'경제' in grade_dict2}")
print(f"'경제' in grade_dict1 = {'경제' in grade_dict1}")

# 값 존재 여부 체크 value - 안됨
print(f"'99' in grade_dict2 = {'99' in grade_dict2}")
print(f"'99' in grade_dict1 = {'99' in grade_dict1}")