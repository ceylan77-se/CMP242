class Student:
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name  = name 
        self.gpa = gpa 
        Student.count += 1 
        Student.total_gpa += gpa

    #INSTANCE METHOD 
    def get_info(self): 
        return f"{self.name} {self.gpa}"
    @classmethod
    def get_count(cls): 
        return f"There is a total number of {cls.count} students : " 
    
    @classmethod
    def get_average_gpa(cls): 
        if cls.count == 0: 
            return 0 
        else:
            return f"average gpa: {cls.total_gpa / cls.count: .2f}" 
student1 = Student(  "thog",  3.9) 

student3 = Student( "kerem", 4.0) 

print(student1.name) 
print(student1.get_count())
print(student1.get_average_gpa())
