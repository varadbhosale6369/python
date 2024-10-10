# Write a python program to accept string and remove the characters which have odd index values of given string using user defined function.

def MyStr():
     Str=input("Enter any String: ")
     cnt=len(Str)
     newStr=""
     for i in range(0,cnt):
        if i%2 ==0:
         newStr=newStr + Str[i]
         print("New String with removed odd Index Character: ",newStr)
MyStr()