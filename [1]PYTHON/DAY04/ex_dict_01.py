# 컨테이너 자료형 - [4] Dictionary
# dict = {Key:Value, ...}
# 순서 X
grade_dict = {"국어":99,"미술":80,"음악":100,"물리":80,"영어":72,"수학":81}
print(f"점수 => {type(grade_dict)}, 원소 개수:{len(grade_dict)}, {grade_dict}")
print(f"{grade_dict.keys()}, \n{grade_dict.values()}, \n{grade_dict}")

# 1. Dict 자료형의 원소 다루기 => 원소 읽기 : 변수명[key]
print(f"grade_dict[국어] : {grade_dict['국어']}")

# 2. Dict 자료형의 원소 값 변경
grade_dict["영어"] = 92
print(f"grade_dict[영어] : {grade_dict['영어']}")

# 3. Dict 자료형의 원소 값 추가
# 존재하지 않는 키 '체육'점수를 85점으로
grade_dict['체육'] = 85
print(f"{grade_dict}")

# 4. Dict 자료형의 원소 값 삭제
del grade_dict['음악']
print(f"{grade_dict}")
