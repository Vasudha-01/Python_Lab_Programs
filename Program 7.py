#!/usr/bin/env python
# coding: utf-8

# In[1]:


#6A Inheritance  
import math 
 
class Shape: 
    def __init__(self): 
        self.area = 0 
        self.name = "" 
         
    def showArea(self): 
        print("The area of the", self.name, "is", self.area, "units") 
         
class Circle(Shape): 
    def __init__(self,radius): 
        self.area = 0 
        self.name = "Circle" 
        self.radius = radius 
         
    def calcArea(self): 
        self.area = math.pi * self.radius * self.radius 
     
class Rectangle(Shape): 
    def __init__(self,length,breadth): 
        self.area = 0 
        self.name = "Rectangle" 
        self.length = length 
        self.breadth = breadth 
         
    def calcArea(self): 
        self.area = self.length * self.breadth 
 
class Triangle(Shape): 
    def __init__(self,base,height): 
        self.area = 0 
        self.name = "Triangle" 
        self.base = base 
        self.height = height 
         
    def calcArea(self): 
        self.area = self.base * self.height / 2 
     
 
     
c1 = Circle(5) 
c1.calcArea() 
c1.showArea() 
r1 = Rectangle(5, 4) 
r1.calcArea() 
r1.showArea() 
t1 = Triangle(3, 4) 
t1.calcArea() 
t1.showArea()


# In[3]:


class Employee: 
    def __init__(self): 
        self.name = "" 
        self.empId = "" 
        self.dept = "" 
        self.salary = 0 
    def getEmpDetails(self): 
        self.name = input("Enter Employee name : ") 
        self.empId = input("Enter Employee ID : ") 
        self.dept = input("Enter Employee Dept : ") 
        self.salary = int(input("Enter Employee Salary : ")) 
    def showEmpDetails(self): 
        print("Employee Details") 
        print("Name : ", self.name) 
        print("ID : ", self.empId) 
        print("Dept : ", self.dept) 
        print("Salary : ", self.salary) 
    def updtSalary(self): 
        self.salary = int(input("Enter new Salary : ")) 
        print("Updated Salary", self.salary) 
e1 = Employee() 
e1.getEmpDetails() 
e1.showEmpDetails() 
e1.updtSalary() 


# In[ ]:




