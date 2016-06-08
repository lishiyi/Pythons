'''Area Calculator'''
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "Calculator is On"
print "%s/%s/%s %s:%s" %(now.month, now.day, now.year, now.hour, now.minute)
sleep(1)

hint = "Don't forget to include the correct units! \nExiting"

option = raw_input("Enter C for Circle or T for Triangle:  ").upper()

if (option == "C"):
  radius = float(raw_input("Please input the radius:  "))
  area = pi * (radius ** 2) 
  print "The pie is baking..."
  sleep(1)
  print "%.2f \n%s" %(area, hint)
elif (option == "T"):
  base = float(raw_input("Please input the base:  "))
  height = float(raw_input("Please input the height:  "))
  area = base * height
  print "Uni Bi Tri..."
  sleep(1)
  print "%.2f \n%s" %(area, hint)
else:
  print "Not valid value, the program will exit"
  
  
