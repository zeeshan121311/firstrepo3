class School:
    pass

class Student(School):
    def __init__(
        self,
        student_id,
        student_name,
        student_f_name,
        student_phone_number,
        student_address,
        student_fees
        ):
        self.student_id = student_id
        self.student_name = student_name
        self.student_f_name = student_f_name
        self.student_phone_number = student_phone_number
        self.student_address = student_address
        self.student_fees = student_fees   

    def getStudent(self):    
        return f"id = {self.student_id},name = {self.student_name},father name = {self.student_f_name},phone number = {self.student_phone_number},address = {self.student_address},fee = {self.student_fees}"     

student1 = Student(
    "1",
    "Ali",
    "Usman",
    "923163425678",
    "Azam Town Karachi",
    "1000"
)
student2 = Student(
    "2",
    "Abdullah",
    "Ikraam",
    "923224536738",
    "Manzoor Colony Karachi",
    "1500"
)
student3 = Student(
    "3",
    "Shoaib",
    "Shakeel",
    "923453678989",
    "Azam Town Karachi",
    "1500"
)
student4 = Student(
    "4",
    "Abdullah",
    "Ikraam",
    "923224536738",
    "Manzoor Colony Karachi",
    "1500"
)
student5 = Student(
    "5",
    "Talha",
    "IQbal",
    "923343647896",
    "Azam Town Karachi",
    "2000"
)
student6 = Student(
    "6",
    "Abdullah",
    "Raees khan",
    "923476789684",
    "Manzoor Colony Karachi",
    "2500"
)
information = student1.getStudent()
print(information)
information = student2.getStudent()
print(information)
information = student3.getStudent()
print(information)
information = student4.getStudent()
print(information)
information = student5.getStudent()
print(information)
information = student6.getStudent()
print(information)

class Teacher(School):
    pass

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
