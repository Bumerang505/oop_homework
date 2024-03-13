class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_join = ",".join(self.courses_in_progress)
        finished_courses_join = ",".join(self.finished_courses)
        for key in self.grades:
            grades_count += len(self.grades[key])
            self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {courses_in_progress_join}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {finished_courses_join}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Неправильное сравнение')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'

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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
