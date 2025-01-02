class School:
    pass

class Student(School):
    pass

class Teacher(School):
    def __init__(self,
        teacher_name,
        teacher_f_name,
        teacher_phone_name,
        teacher_salary,
        ):
        self.teacher_name = teacher_name
        self.teacher_f_name = teacher_f_name
        self.teacher_phone_number = teacher_phone_name
        self.teacher_salary = teacher_salary

    def getteacher(self):
        return f" Name: {self.teacher_name}  Father Name: {self.teacher_f_name} Phone Number: {self.teacher_phone_number}"   

class Admin(School):
    pass

class Classrooms(School):
    pass
    
class Event(School):
    pass

class Exams(School):
    pass
  
class Stock(School):
    pass
