class Student:
    def __init__(self, name, surname, gender):
        self.average_student = None
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return Student.average_student(self) < Student.average_student(other)

    def average_student(self):
        count = 0
        for grade in self.grades:
            count += len(self.grades[grade])
        self.average_student = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_student

    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {Student.average_student(self)}\nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses} '


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_lector = None
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return Lecturer.average_lector(self) < Lecturer.average_lector(other)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.average_lector(self)}'

    def average_lector(self):
        count = 0
        for grade in self.grades:
            count += len(self.grades[grade])
        self.average_lector = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_lector


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
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

some_student = Student('Olga', 'Avdeeva', 'female')
some_student.courses_in_progress += ['Git']
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer = Reviewer('Good', 'Boy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_lecturer1 = Lecturer('Good', 'Teacher')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.courses_attached += ['Git']

some_student.rate_lector(some_lecturer, 'Python', 15)
some_student.rate_lector(some_lecturer, 'Python', 5)
some_student.rate_lector(some_lecturer, 'Python', 10)

some_student.rate_lector(some_lecturer1, 'Python', 150)
some_student.rate_lector(some_lecturer1, 'Python', 5)
some_student.rate_lector(some_lecturer1, 'Python', 100)

some_student.rate_lector(some_lecturer, 'Python', 15)
some_student.rate_lector(some_lecturer, 'Python', 5)
some_student.rate_lector(some_lecturer, 'Python', 10)

some_reviewer.rate_hw(some_student, 'Python', 100)
some_reviewer.rate_hw(some_student, 'Python', 100)
some_reviewer.rate_hw(some_student, 'Git', 110)

some_reviewer.rate_hw(best_student, 'Python', 200)
some_reviewer.rate_hw(best_student, 'Python', 300)
some_reviewer.rate_hw(best_student, 'Git', 110)

print(best_student > some_student)
print(some_lecturer > some_lecturer1)
print(some_reviewer)
print(some_lecturer)
print(some_student)


student_list = [best_student, some_student]
lecture_list = [some_lecturer, some_lecturer1]


def average_mark_student(student, course):
    total = 0
    quantity = len(student)
    # print(quantity)
    for person in student:
        if course not in person.grades:
            quantity -= 1
            continue
        else:
            total += (sum(person.grades[course]) / len(person.grades[course]))
            # print(total)
    print(f' Средняя оценка за домашнее задание по курсу {course} {round((total / quantity), 2)}')
    return


average_mark_student(student_list, 'Python')


def average_mark_lectore(lectore, course):
    total = 0
    quantity = len(lectore)
    # print(quantity)
    for person in lectore:
        if course not in person.grades:
            quantity -= 1
            continue
        else:
            total += (sum(person.grades[course]) / len(person.grades[course]))
            # print(total)
    print(f' Средняя оценка за лекцию {course} {round((total / quantity), 2)}')
    return


average_mark_lectore(lecture_list, 'Python')


