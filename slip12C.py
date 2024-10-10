# Write a python program to count repeated characters in a string. Sample string: 'thequickbrownfoxjumpsoverthelazydog' Expected output: o-4, e-3, u-2, h-2, r-2, t-

check_string="MalegaonBaramatiPune"
dict = {}
for ch in check_string:
 if ch in dict:
     dict[ch] += 1
 else:
    dict[ch] = 1
 
for key in dict:
    print(key, "-" , dict[key])