grades_valid_list = range(1, 11)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if self.check_lecturer_course(lecturer, course):
            if self.check_grade(grade):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print(f'Уважаемый {self.name} {self.surname}, оценку {grade} ставить нельзя, допустимо от 1 до 10!')
        else:
            print(f'Уважаемый {self.name} {self.surname}, у вас нет прав ставить оценки '
                  f'лектору {lecturer.name} {lecturer.surname} за курс {course}')
            return 'Ошибка'

    def check_grade(self, grade):
        if grade in grades_valid_list:
            return True
        else:
            return False

    def check_lecturer_course(self, lecturer, course):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            return True
        else:
            return False

    def average_grade(self):
        for courses in self.grades:
            average = round(sum(self.grades[courses]) / len(self.grades[courses]), 1)
            return average

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.average_grade()}\n" \
              f"Курсы в процессе изучения: {(', ').join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {(', ').join(self.finished_courses)}"

        return res

    def __lt__(self, other):
        if self.average_grade() == other.average_grade():
            return f'Оба студента имеют одинаковый средний балл'
        else:
            if self.average_grade() < other.average_grade():
                return f'Студент {other.name} {other.surname} имеет средний балл выше'
            else:
                return f'Студент {self.name} {self.surname} имеет средний балл выше'

    def print_name(self):
        return 'студентов'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached = []):
        super().__init__(name, surname)
        self.grades = {}



    def average_grade(self):
        averange = float()
        for cours in self.grades.keys():
            if cours in self.courses_attached:
                averange_1 = float(round(sum(self.grades[cours]) / len(self.grades[cours]), 1))
            averange += averange_1
        return averange / len(self.grades.keys())

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {self.average_grade()}"
        return res

    def __lt__(self, other):
        if self.average_grade() == other.average_grade():
            return f'Оба лектора имеют одинаковый средний балл'
        else:
            if self.average_grade() < other.average_grade():
                return f'Лектор {other.name} {other.surname} имеет средний балл выше'
            else:
                return f'Лектор {self.name} {self.surname} имеет средний балл выше'

    def print_name(self):
        return 'лекторов'




best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Java', 'C++']
best_student.finished_courses += ['Введение в программирование', 'Git']


best_student_2 = Student('Nata', 'Steam', 'femail')
best_student_2.courses_in_progress += ['Python', 'C++', 'Jambo']
best_student_2.finished_courses += ['Git']

cool_lecturer = Lecturer('Lec', 'Speaker')
cool_lecturer.courses_attached += ['Python', 'C++', 'Jambo']

cool_lecturer_2 = Lecturer('Nick', 'Hudson')
cool_lecturer_2.courses_attached += ['Python', 'C++', 'Java']

cool_reviewer = Reviewer('Tom', 'Morthon')
cool_reviewer.courses_attached += ['Python', 'C++', 'Java']

cool_reviewer_2 = Reviewer('Some', 'Buddy')
cool_reviewer_2.courses_attached += ['Python', 'C++', 'Jambo']


best_student.rate_hw(cool_lecturer, 'Python', 5)
best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'C++', 3)
best_student.rate_hw(cool_lecturer, 'C++', 5)
best_student_2.rate_hw(cool_lecturer_2, 'C++', 9)
best_student_2.rate_hw(cool_lecturer_2, 'C++', 7)
best_student_2.rate_hw(cool_lecturer_2, 'Python', 5)
best_student_2.rate_hw(cool_lecturer_2, 'Python', 8)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer_2.rate_hw(best_student, 'Java', 15)
cool_reviewer.rate_hw(best_student, 'Python', 20)
cool_reviewer_2.rate_hw(best_student, 'C++', 45)
cool_reviewer.rate_hw(best_student, 'C++', 15)
cool_reviewer.rate_hw(best_student, 'Python', 20)

cool_reviewer.rate_hw(best_student_2, 'C++', 30)
cool_reviewer.rate_hw(best_student_2, 'Python', 15)
cool_reviewer.rate_hw(best_student_2, 'C++', 15)
cool_reviewer_2.rate_hw(best_student_2, 'C++', 35)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 30)
cool_reviewer_2.rate_hw(best_student_2, 'C++', 10)



print(best_student)
print()
print(best_student_2)
print()
print(cool_lecturer)
print()
print(cool_lecturer_2)
print()
print(best_student > best_student_2)
print()
print(cool_lecturer > cool_lecturer_2)
print()

students_list = [best_student, best_student_2]
lecturer_list = [cool_lecturer, cool_lecturer_2]


def average_grade(list, course):
    """

Общая фукция для подсчета среднего количества баллов
для студентов и для лекторов
    """
    grades_sum = 0
    grades_qty = 0
    for item in list:
        grades_sum += sum(item.grades[course])
        grades_qty += len(item.grades[course])
    average_all_item = round(grades_sum / grades_qty, 1)
    return f'Cредний бал всех {item.print_name()} для курса {course}: {average_all_item }'


print(average_grade(students_list, 'Python'))
print(average_grade(students_list, 'C++'))

print(average_grade(lecturer_list, 'Python'))
print(average_grade(lecturer_list, 'C++'))


