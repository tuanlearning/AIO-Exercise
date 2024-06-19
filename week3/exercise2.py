class Person:
    def __init__(self, name, yob):
        assert isinstance(yob, int), 'Year of birth has to be an integer'
        assert isinstance(name, str), 'Name has to be a string'
        self._name = name
        self._yob = yob
    def describe(self):
        print(f'This person name is :{self._name}, yob: {self._yob}')

class Student(Person):
    def __init__(self, name, yob, grades):
        super().__init__(name, yob)
        self.__grades = grades
    def describe(self):
        print(f'This person name is :{self._name}, yob: {self._yob}, grade: {self.__grades}')

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject
    def describe(self):
        print(f'This person name is :{self._name}, yob: {self._yob}, subject: {self.__subject}')

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist
    def describe(self):
        print(f'This person name is :{self._name}, yob: {self._yob}, specialist: {self.__specialist}')

class Ward():
    def __init__(self, name):
        self.__name = name
        self.__persons = []
    def add_person(self, person: Person):
        self.__persons.append(person)
    def ward_population(self):
        return len(self.__persons)
    def describe(self):
        print(f"The ward name is: {self.__name}")
        if self.ward_population() == 0:
            print(f"The ward has no people")
        else:
            for person in self.__persons:
                person.describe()
    def count_doctor(self):
        number_of_doctor = sum([1 for person in self.__persons if type(person) == Doctor])
        print(f"Number of doctor : {number_of_doctor}")
        return number_of_doctor
    def sort_age(self):
        self.__persons.sort(key = lambda x: x._yob, reverse = True)
    def compute_average(self):
        number_of_teacher = sum([1 for person in self.__persons if type(person) == Teacher])
        if number_of_teacher == 0:
            print(f"There are no teachers in the ward")
        else:
            yob_lists = [person._yob for person in self.__persons if type(person) == Teacher]
            average_yob = sum(yob_lists)/len(yob_lists)
            print(f"The average year of birth of all teachers in the ward is: {average_yob}")