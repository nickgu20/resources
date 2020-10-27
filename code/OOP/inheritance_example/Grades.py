from Student import UG, Grad


class Grades:
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}  # maps id -> list of grades
        self.is_sorted = True  # True if self.students is sorted

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)
        self.grades[student.id] = []
        self.is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.id].append(grade)
        except KeyError:
            raise ValueError("Student not in grade book")

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:  # return copy of student's grades
            return self.grades[student.id][:]
        except KeyError:
            raise ValueError("Student not in grade book")

    def all_students(self):
        """Return a list of the students sorted in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True

        # return copy of list of students
        return self.students[:]


def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.all_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot / num_grades
            report.append(str(s) + "'s mean grade is " + str(average))
        except ZeroDivisionError:
            report.append(str(s) + " has no grades")
    return "\n".join(report)


def main():
    ug1 = UG("Shoaib Rahaman", 2021)
    ug2 = UG("Anna Zhang", 2022)
    ug3 = UG("Palida Prasitanond", 2022)
    ug4 = UG("Susanna A D'Souza", 2020)

    g1 = Grad("Matt Damon")
    g2 = Grad("Ben Affleck")

    mis3640 = Grades()
    mis3640.add_student(g1)
    mis3640.add_student(ug2)
    mis3640.add_student(ug1)
    mis3640.add_student(g2)
    mis3640.add_student(ug4)
    mis3640.add_student(ug3)

    mis3640.add_grade(g1, 100)
    mis3640.add_grade(g2, 25)
    mis3640.add_grade(ug1, 95)
    mis3640.add_grade(ug2, 85)
    mis3640.add_grade(ug3, 90)

    print("after first test:")
    print(gradeReport(mis3640))

    mis3640.add_grade(g1, 90)
    mis3640.add_grade(g2, 45)
    mis3640.add_grade(ug1, 80)
    mis3640.add_grade(ug2, 100)

    print()
    print("after second test:")
    print(gradeReport(mis3640))

    for student in mis3640.students:
        print(student.speak("I am excited to see the results!"))


if __name__ == "__main__":
    main()
