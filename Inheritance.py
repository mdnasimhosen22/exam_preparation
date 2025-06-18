class person:
    def __init__(self,name,age):  # constructor
        self.nam = name
        self.age = age
    def show_info (self):
        print(f"Name: {self.nam}")
        print(f"Age: {self.age}")

# ✅ Child class (inherits from Person)
class students(person):
    def __init__(self,name,age,studenId):
        super().__init__(name,age) # parent class এর constructor কল করি
        self.student_id = studenId

    def show_student(self):
        self.show_info()
        print(f"Student_Id : {self.student_id}")

# creat object
obj = students("Md Nasim Hosen",20,"stud123")
obj.show_student()