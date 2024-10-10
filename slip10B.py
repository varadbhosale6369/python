#Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' ']’. These brackets must be close in the correct order. for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

s="{()[}("
lst=[]
if len(s) % 2 != 0:
    print("Invalid Sequence")
else:
    for b in s:
         if b=="(" or b=="{" or b=="[":
            lst.append(b)
         elif b==")" or b=="}" or b=="]":
            cnt=len(lst)-1
            if b==")":
                if lst[cnt]=="(":
                    lst.pop()
                else:
                 print("Invalid Sequence")
                 break
            if b=="}":
                 if lst[cnt]=="{":
                     lst.pop()
            else:
                 print("Invalid Sequence")
                 break
         if b=="]":
            if lst[cnt]=="[":
                lst.pop()
         else:
             print("Invalid Sequence")
             break
    if len(lst)==0:
        print("valid Sequence")