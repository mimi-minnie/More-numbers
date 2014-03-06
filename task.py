from datetime import data as dat

def getYear():
    year = input ("PLease enter the year that you were born. ")
    year = int (year)
    return year
    
def age(yearOfBirth):
    today = dat.today()
    thisyear = today.year
    age = thisyear - yearOfBirth
    
year = getyear ()
print("you will be %s years old this year on your birthday" %age(year))
