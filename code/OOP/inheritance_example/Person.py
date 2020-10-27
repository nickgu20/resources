import datetime


class Person:
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.last_name = name.split(" ")[-1]

    def set_birthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def get_age(self):
        """returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
           less than other's name, and False otherwise""" 
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name

    # other methods

    def __str__(self):
        """return self's name"""
        return self.name


def main():
    p1 = Person("Mark Zuckerberg")
    p1.set_birthday(5, 14, 84)
    p2 = Person("Barack Obama")
    p2.set_birthday(8, 4, 61)
    p3 = Person("Bill Gates")
    p3.set_birthday(10, 28, 55)
    p4 = Person("Donald Trump")
    p5 = Person("Michelle Obama")

    person_list = [p1, p2, p3, p4, p5]

    for e in person_list:
        print(e)

    person_list.sort()

    print()

    for e in person_list:
        print(e)


if __name__ == "__main__":
    main()
