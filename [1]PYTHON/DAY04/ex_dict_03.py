# 컨테이너 자료형 - [4] Dictionary
# dict와 내장함수 : len(), max(), min(), sum(), sorted()
# key값만 적용
grade_dict1 = {"국어":99,"미술":80,"음악":100,"물리":80,"영어":72,"수학":81}

# 내장함수 : max(), min() : 키만 가능
mx, mn = max(grade_dict1), min(grade_dict1)
print(f"최대값: {mx}, 최솟값: {mn}")

# 내장함수 : sorted() : 키만 가능
# 결과는 List 반환
new_dict = sorted(grade_dict1)
print(f"정렬: {new_dict}, {type(new_dict)}")
