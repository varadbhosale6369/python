#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case. Further modify the program to reverse a string word by word and print it in lower case.

class MyClass:
     def Get_String(self):
        self.MyStr=input("Enter any String: ")
     def Print_String(self):
         s=self.MyStr
         print("String in Upper Case: " , s.upper())
         cnt=len(s)
         i=cnt-1
         RevStr=""
         while(i >= 0):
             RevStr=RevStr + s[i]
             i=i-1
             print("String in Reverse & Lower case:" , RevStr.lower())
Obj=MyClass()
Obj.Get_String()
Obj.Print_String()