"""

	This is the graded assignment for the course.
"""

import datetime            #Importing the required module.


def days_in_month(year, month): 
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    elif month in (4, 6, 9, 11):
        days = 30
    else:
        if year%4 == 0:
            days = 29
        else:
            days = 28


    return days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
 
    flag = True

	# To check the year validity.
    if year in range(datetime.MINYEAR, datetime.MAXYEAR):
        pass
	
    else:
        flag = False
        return flag

    
# To check the month validity.
    if month in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        pass
    else:
        flag = False
        return flag

	# To check day validity.
    days = days_in_month(year, month)
    if day in range(1, (days+1)):
        pass
    else:
        flag = False
        return flag

    return flag	

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """

    valid1 = is_valid_date(year1, month1, day1)
    valid2 = is_valid_date(year2, month2, day2)

    if valid1 and valid2: 
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        difference = date2 - date1

        if difference.days >= 0:            
            flag = difference.days 
        else: 
            flag = 0
    else:
        flag = 0

    return flag

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    date2 = datetime.date.today()

    age = days_between(year, month, day, date2.year, date2.month, date2.day)
    return age


