'''So far, you've used Python to build a variety of things, including calculators and games. In this project, we'll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event'''

from time import sleep, strftime

name = "Shiyi"
calendar = {}

def welcome():
  print "Welcome, %s!" %(name)
  print "Calendar opening..."
  sleep(1)
  print strftime("%A %m %d, %y")
  print strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
    welcome()
    start = True
    while start:
      user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ").upper()
      if user_choice == "V":
        if len(calendar.keys()) < 1:
          print "The calendar is empty"
        else:
          print calendar
      elif user_choice == "U":
        date = raw_input("What date? ")
        update = raw_input("Enter the update: ")
        calendar[date] = update
        print "Update successful"
      elif user_choice == "A":
        event = raw_input("Enter event: ")
        date = raw_input("Enter date (MM/DD/YYYY)")
        if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
          try_again = raw_input("Input not correct, try again? Y for yes, N for No: ").upper()
          if try_again == "Y":
            continue
          elif try_again == "N":
            start = false
          else:
            break;
        else:
          calendar[date] = event;
      elif user_choice == "D":
        if len(calendar.keys()) < 1:
          print "The calendar is empty"
        else:
          event = raw_input("What event? ")
          for date in calendar.keys():
            if calendar[date] == event:
              del calendar[date]
              print "The event was successfully deleted."
              print calendar
      elif user_choice == "X":
        start = False
      else:
        print "Invalid input"
        
start_calendar()
        
          
    				 
    
    
    
    
    
    
    
    
