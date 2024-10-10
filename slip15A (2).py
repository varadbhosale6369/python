# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.

class Student:
    def Accept(self):
         self.name=input("Enter Student Name:")
         self.mark=int(input("Enter Student Total Marks:"))
    def Modify(self):
         self.oldmark=self.mark
         self.mark=int(input("Enter Student New Total Marks:"))
         print("Student Name:",self.name)
         print("Old Total Mark:",self.oldmark)
         print("New Total Mark:",self.mark)
Stud1=Student()
Stud1.Accept()
Stud1.Modify()