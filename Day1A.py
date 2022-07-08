# import modules used to get time and date
import calendar
from datetime import date

date = date.today()

day = calendar.day_name[date.weekday()][:3]

# conditional statement to validate fare
if day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
    fare = 100
elif day == 'Sat':
    fare = 60
elif day == 'Sun':
    fare = 80
else:
    print('Error invalid day')

# print outputs
print(f'Date: {date}')
print(f'Day: {day}')
print(f'Fare: {fare}')





