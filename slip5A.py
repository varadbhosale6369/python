#Write a Python script using class, which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class MyClass:
    def Get_String(self):
        self.MyStr=input("Enter any String: ")
    def Print_String(self):
         s=self.MyStr
         print("String in Upper Case: " , s.upper())
Obj=MyClass()
Obj.Get_String()
Obj.Print_String()
