# Define a class Date (Day, Month, Year) with functions to accept and display it. Accept date from user. Throw user defined exception “invalid Date Exception” if the date is invalid.

class MyDate:
 def accept(self):
     self.d=int(input("Enter Day:"))
     self.m=int(input("Enter Month:"))
     self.y=int(input("Enter Year:"))
 def display(self):
    try:
        if self.d>31:
            raise ValueError("Day value is greater than 31")
        if self.m>12:
            raise ValueError("Month Value is Greater than 12")
            print("Date is: ", self.d, "-" ,self.m , "-",self.y )
    except ValueError as e:
        print(e)
Obj= MyDate()
Obj.accept()
Obj.display()