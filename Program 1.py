#!/usr/bin/env python
# coding: utf-8

#1A - Test Average
m1 = int(input("Enter marks for test1 : "))
m2 = int(input("Enter marks for test2 : "))
m3 = int(input("Enter marks for test3 : "))
if m1 <= m2 and m1 <= m3:
 avgMarks = (m2+m3)/2
elif m2 <= m1 and m2 <= m3:
 avgMarks = (m1+m3)/2
elif m3 <= m1 and m2 <= m2:
 avgMarks = (m1+m2)/2 
 
print("Average of best two test marks out of three test’s marks is", avgMarks);


#1B - Palindrome
val = int(input("Enter a value : "))
str_val = str(val)
if str_val == str_val[::-1]:
 print("Palindrome")
else:
 print("Not Palindrome")
 
for i in range(10):
 if str_val.count(str(i)) > 0:
    print(str(i),"appears", str_val.count(str(i)), "times")




