class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def average(self):
        grades_lst = sum(self.grades.values(), [])
        return sum(grades_lst) / len(grades_lst)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_join = ",".join(self.courses_in_progress)
        finished_courses_join = ",".join(self.finished_courses)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.average()}\n' \
               f'Курсы в процессе обучения: {courses_in_progress_join}\n' \
               f'Завершенные курсы: {finished_courses_join}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Неправильное сравнение')
            return
        return self.average() < other.average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for v in self.grades:
            grades_count += len(self.grades[v])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_rating.__round__(2)}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Неправильное сравнение')
            return
        return self.average_rating < other.average_rating


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_lecturer_1 = Lecturer('Иван', 'Петров')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Сергей', 'Ярославцев')
best_lecturer_2.courses_attached += ['Java']

cool_reviewer_1 = Reviewer('Дмитрий', 'Гоев')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Олег', 'Первухин')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

best_student_1 = Student('Антон', 'Локтев', 'М')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ['Введение в программирование']

best_student_2 = Student('Кирилл', 'Варов', 'М')
best_student_2.courses_in_progress += ['Java']
best_student_2.finished_courses += ['Введение в программирование']

best_student_1.rate_hw(best_lecturer_1, 'Python', 7)
best_student_1.rate_hw(best_lecturer_1, 'Python', 7)
best_student_1.rate_hw(best_lecturer_1, 'Python', 9)

best_student_1.rate_hw(best_lecturer_2, 'Python', 5)
best_student_1.rate_hw(best_lecturer_2, 'Python', 7)
best_student_1.rate_hw(best_lecturer_2, 'Python', 8)

best_student_1.rate_hw(best_lecturer_1, 'Python', 7)
best_student_1.rate_hw(best_lecturer_1, 'Python', 8)
best_student_1.rate_hw(best_lecturer_1, 'Python', 9)

best_student_2.rate_hw(best_lecturer_2, 'Java', 10)
best_student_2.rate_hw(best_lecturer_2, 'Java', 8)
best_student_2.rate_hw(best_lecturer_2, 'Java', 9)

cool_reviewer_1.rate_hw(best_student_1, 'Python', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)

cool_reviewer_2.rate_hw(best_student_2, 'Java', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 7)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 9)

print(f'Студенты:\n\n{best_student_1}\n\n{best_student_2}')

print(f'Лекторы:\n\n{best_lecturer_1}\n\n{best_lecturer_2}')

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{best_student_1.name} {best_student_1.surname} < {best_student_2.name} {best_student_2.surname} = '
      f'{best_student_1 > best_student_2}')

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = '
      f'{best_lecturer_1 > best_lecturer_2}')

student_list = [best_student_1, best_student_2]
lecturer_list = [best_lecturer_1, best_lecturer_2]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all=0
    for stud in student_list:
        if course_name in stud.courses_in_progress:
            sum_all += sum(stud.grades.get(course_name, []))
            count_all = len(stud.grades.get(course_name, []))
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")

