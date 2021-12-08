class Student_class:

    def __init__(self, name, grades):
        self.name = name,
        self.grades = grades
        self.average_grade = self.get_average_grades()

    def get_average_grades(self):
        grades_int_list = list(map(int, self.grades.split(',')))
        return round(sum(grades_int_list) / len(grades_int_list), 1)