# To get current date and time
# We need to use the datetime library
from datetime import datetime, timedelta

today = datetime.now()
# the now function returns a datetime object
print('Today is: ' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('yesterday was: ' + str(yesterday))

# use date functions to control date formatting
from datetime import datetime
current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

# Received date as a string and
# convert it to datetime object

from datetime import datetime
birthday = input('When is your birthday (dd/mm/yy)? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%y')

print('Birthday: ' + str(birthday_date))