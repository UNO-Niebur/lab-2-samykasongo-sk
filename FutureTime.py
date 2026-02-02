#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  add_hours = int(input("Enter hours to add: "))
  #Ask user for minutes
  add_minutes = int(input("Enter minutes to add: "))
  #Calculate the time after the user-supplied time has passed.
  future_time = now + datetime.timedelta(hours=add_hours, minutes=add_minutes)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("Future time will be:", future_time.strftime("%H:%M"))


if __name__ == '__main__':
  main()
