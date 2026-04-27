## ==================================================
# 사용자 정의 클래스
## ==================================================
## --------------------------------------------------
# 학생 클래스 정의
# -> 데이터 : 학번, 이름, 전공, 부전공, 학년, 학점
# -> 기능/역활 : 학생정보 출력 기능 => 학번, 이름, 전공, 부전공
#               전체학점 계산 기능 => 학점 -> 1/1, 1/2, 2/1, 2/2, 3/1, 3/2, 4/1, 4/2
#               공부 기능 => OOO이/가 OO과목 공부한다.
#               시험 기능 => OOO이/가 OO과목 시험친다.
## --------------------------------------------------
# 클래스이름 : Student
# 클래스속성 : stdno, name, major, minor, stdyear, grade
# 클래스기능 : print_info()
#            total_grade()
#            study()
#            test()
## --------------------------------------------------
class Student:
    # 공유되는 클래스 속성 property / 필드 field / 어트리뷰트 attribute
    def __init__(self, stdno, name, major, minor, stdyear, grade):
        self.stdno = stdno
        self.name = name
        self.major = major
        self.minor = minor
        self.stdyear = stdyear
        self.grade = grade
    
    # 인스턴스 메서드 정의
    def print_info(self):
        print(f'{self.stdno} {self.name} {self.major} {self.minor}')

    def total_grade(self):
        return f"{sum(self.grade)/len(self.grade):.2f}" if len(self.grade) else 0
        # grade = self.grade
        # for i in grade:
        #     total += i
        # return total

    def study(self, subject):
        print(f"{self.name}이/가 {subject}스킬 공부한다.")

    def test(self, subject):
        print(f"{self.name}이/가 {subject}스킬 시험친다.")

grade1 = [4,3.5,3.7,4.2,2.5,3]
grade2 = [4,3.5,3.7,4.2]
std1 = Student("001014", "홍길동", "법사", "화염", 3, grade1)
std1.print_info()
print(std1.total_grade())
std1.study("파이어볼")
std1.test("파이어볼")

std1.minor = "얼음"
std1.print_info()

std2 = Student("010101", "마징가", "전사", "쌍검", 1, grade2)
std2.print_info()
print(std2.total_grade())
std2.study("ㅗ")
std2.test("ㅗ")
