from functools import reduce

class Student:
    _list_student = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self._list_student.append(self)

    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.finished_courses and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rating(self):
        if self.grades:
            rating_list = [rate for rate in self.grades.values() for rate in rate]
            average_rate = (reduce(lambda x, y: x + y, rating_list)) / len(rating_list)
            return f'Средняя оценка за домашние задания: {round(average_rate, 1)}'
        else:
            return 'Студент не имеет баллов за домашние задания'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} - не лектор')
            return
        return self.__average_rating() < other.__average_rating()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n{self.__average_rating()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    _list_lecturer = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self._list_lecturer.append(self)

    def __average_rating(self):
        if self.grades:
            rating_list = [rate for rate in self.grades.values() for rate in rate]
            average_rate = (reduce(lambda x, y: x + y, rating_list)) / len(rating_list)
            return f'Средняя оценка за лекции: {round(average_rate, 1)}'
        else:
            return 'Лектор не имеет баллов за лекций'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} - не лектор')
            return
        return self.__average_rating() < other.__average_rating()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}' \
               f'\n{self.__average_rating()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student = Student('Ruoy', 'Eman', 'your_gender')
student.finished_courses += ['Введение в программирование', 'Git']
student.courses_in_progress += ['Python']

student1 = Student('Roy', 'Jons', 'your_gender')
student1.finished_courses += ['Введение в программирование', 'Git']
student1.courses_in_progress += ['Python']

mentor = Reviewer('Some', 'Buddy')
mentor.courses_attached += ['Python', 'Введение в программирование', 'Git']

mentor.rate_hw(student, 'Python', 10)
mentor.rate_hw(student, 'Git', 9)
mentor.rate_hw(student, 'Git', 10)
mentor.rate_hw(student, 'Git', 11)
mentor.rate_hw(student, 'Python', 8)
mentor.rate_hw(student, 'Введение в программирование', 7)
mentor.rate_hw(student, 'Введение в программирование', 10)

mentor.rate_hw(student1, 'Python', 9)
mentor.rate_hw(student1, 'Git', 9)
mentor.rate_hw(student1, 'Введение в программирование', 8)

print(student)
print()
print(student1)
print()
print(student1.__lt__(student))
print()
print(mentor)
print()

mentor1 = Lecturer('Kriss', 'Karry')
mentor1.courses_attached += ['Python', 'Git', 'Введение в программирование']
student.rate_hw(mentor1, 'Введение в программирование', 10)
student.rate_hw(mentor1, 'Git', 5)
student.rate_hw(mentor1, 'Git', 5)

mentor2 = Lecturer('Kri', 'Kro')
mentor2.courses_attached += ['Python', 'Git', 'Введение в программирование']
student.rate_hw(mentor2, 'Введение в программирование', 9)
student.rate_hw(mentor2, 'Git', 5)
student.rate_hw(mentor2, 'Git', 5)

print(mentor1)
print()
print(mentor2)
print()
print(mentor1.__lt__(mentor2))
print()


def average_rating_student(students, course):
    rez = 0
    for student_ in students:
        if course in student_.grades:
            for score in student_.grades[course]:
                rez += score
    return rez


def average_rating_lecturer(lecturers, course):
    rez = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            for score in lecturer.grades[course]:
                rez += score
    return rez


print(average_rating_student(Student._list_student, 'Git'))

print(average_rating_lecturer(Lecturer._list_lecturer, 'Введение в программирование'))

