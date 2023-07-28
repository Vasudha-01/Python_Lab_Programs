#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
              lst[k] = left_half[i]
              i += 1
              k += 1
        while j < len(right_half):
              lst[k] = right_half[j]
              j += 1
              k += 1
    return lst
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
my_list = []
for i in range(10):
    my_list.append(random.randint(0, 999))
print("\nUnsorted List")
print(my_list)
print("Sorting using Insertion Sort")
insertion_sort(my_list)
print(my_list)
my_list = []
for i in range(10):
    my_list.append(random.randint(0, 999))
print("\nUnsorted List")
print(my_list)
print("Sorting using Merge Sort")
merge_sort(my_list)
print(my_list)



#4 B program
#Roman
def roman2Dec(romStr):
    roman_dict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
 # Analyze string backwards
    romanBack = list(romStr)[::-1]
    value = 0
 # To keep track of order
    rightVal = roman_dict[romanBack[0]] 
    for numeral in romanBack:
        leftVal = roman_dict[numeral]
 # Check for subtraction
        if leftVal < rightVal:
          value -= leftVal
        else:
            value += leftVal
            rightVal = leftVal
        return value
romanStr = input("Enter a Roman Number : ")
print(roman2Dec(romanStr))




