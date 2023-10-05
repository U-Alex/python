import re


class Sname:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if (re.compile("^[a-zA-Zа-яА-ЯёЁ ]{2,}$").search(value)) and value.istitle():
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Sgrade:
    def __init__(self, s_min, s_max):
        self.s_min = s_min
        self.s_max = s_max

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.s_min <= value <= self.s_max:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Оценка должна быть целым числом от {self.s_min} до {self.s_max}')


class Student:
    name = Sname()
    _grade = Sgrade(s_min=2, s_max=5)
    _test_score = Sgrade(s_min=0, s_max=100)

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects_file = subjects_file
        self._subjects = {'Математика': {'grade': [], 'test': []},
                          'Физика': {'grade': [], 'test': []},
                          'История': {'grade': [], 'test': []},
                          'Литература': {'grade': [], 'test': []}
                          }

    def __str__(self):
        res = f'Студент: {self.name}\n'
        sbj = []
        for key, val in self._subjects.items():
            if len(val['grade']) or len(val['test']):
                sbj.append(key)
        res += 'Предметы: ' + ', '.join(sbj)
        return res

    def add_grade(self, subject, grade):
        self._grade = grade
        self._subjects[subject]['grade'].append(self._grade)

    def add_test_score(self, subject, test_score):
        self._test_score = test_score
        self._subjects[subject]['test'].append(self._test_score)

    def get_average_grade(self):
        res = []
        for _, ob in self._subjects.items():
            for ob2 in ob['grade']:
                res.append(ob2)
        if len(res):
            return sum(res) / len(res)
        return None

    def get_average_test_score(self, subject):
        if self._subjects.get(subject, False):
            res = []
            for ob2 in self._subjects[subject]['test']:
                res.append(ob2)
            if len(res):
                return sum(res) / len(res)
            return None
        raise ValueError(f"Предмет {subject} не найден")

    def get_subjects(self):
        return self._subjects


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("Математика", 3)
student.add_test_score("Математика", 80)
student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")
average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
print(student.get_subjects())
