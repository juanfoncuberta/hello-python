## Dates ##
from datetime import datetime, time, date, timedelta

"""
  3 types of data for date/time 

"""



now = datetime.now()
print(now)
print(now.hour)
print(now.day)

timestamp = now.timestamp()
print(timestamp)

new_year = datetime(2023,1,5)
def print_date(new_year):
  print(f'{new_year.day}/{new_year.month}/{new_year.year} ')


current_time = time(10,4,4)
print(current_time)
print(current_time.minute)
print(current_time.min)
print_date(new_year)
 
current_date = date.today()
print(current_date.day)

random_date = date(2022,1,6)
print_date(random_date)


print(current_date.year - random_date.year)
#you can substract dates. the results are in days
print(now - new_year )

#timedelta is an object helps tooperate with dates
time_delta = timedelta(
  100, hours=6
) 
print(time_delta)

# Using current time
ini_time_for_now = datetime.now()
 
# printing initial_date
print ("initial_date", str(ini_time_for_now))
 
# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + \
                        timedelta(days = 730)
 
future_date_after_2days = ini_time_for_now + timedelta(days = 2)
 

print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))
