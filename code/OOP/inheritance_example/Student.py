from BabsonPerson import BabsonPerson
from Person import Person


class Student(BabsonPerson):
    pass


class UG(Student):
    def __init__(self, name, class_year):
        BabsonPerson.__init__(self, name)
        self.year = class_year

    def get_class_year(self):
        return self.year

    def speak(self, utterance):
        return BabsonPerson.speak(self, " Dude, " + utterance)


class Grad(Student):
    pass


def is_student(obj):
    return isinstance(obj, Student)


def main():
    s1 = UG("Shoaib Rahaman", 2021)
    s2 = UG("Anna Zhang", 2022)
    s3 = UG("Palida Prasitanond", 2022)
    s4 = Grad("Matt Damon")

    student_list = [s1, s2, s3, s4]

    print(s1)

    print(s1.get_class_year()) 
    # print(s1.year)

    print(s1.speak("where is the quiz?"))

    print(s2.speak("I have no clue!"))

    print(s4.speak("I am not sure why I am here."))

    # print(is_student(s1))

    # p1 = Person("Taylor Swift")
    # print(is_student(p1))


if __name__ == "__main__":
    main()
