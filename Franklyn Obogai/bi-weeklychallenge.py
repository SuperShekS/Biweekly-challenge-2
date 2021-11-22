#Solution

from datetime import *
#From the question, current year is 2020. So the variable "today_in_2020" is intended to set a date in 2020 for use in the succeeding computation.  
current_year = 2020
today_in_2020 = str(date.today() - timedelta(days=365))
try:
  name = input("What is your name?: ")
  age = int(input("How old are you?: "))
except ValueError:
  print("Oh... oh..., that was not a valid entry, input a number.")
except NameError:
    print("Variable is not properly defined.")
except TypeError:
  print("Argument must be a number.")
#Below is the input function to capture name and age.
def capture_detail(name, age):
    """"
    Returns a screen printout from the arguments parsed when called. 
    
    Parameters:
             name (str): takes in a string of the client's name.
             age (int): takes in an integer of the client's age.
    
    Returns:
            A print to screen of a message like this below.
            e.g. Hello John Doe, you are 3 years old.
             Your year of birth is 2051.
             As you are 3 years old, you are an adult.
             In 2046 you were -7 years old.
             In 2064 you’ll be 13y.o.
             In 2074 you’ll be 23y.o. etc.
    """
    dob = datetime.strptime(today_in_2020, "%Y-%m-%d") - timedelta(days=(365*int(age))) #dob (Date of birth) is calculated by subtracting the 'age' inputed from the set date.
    yob = dob.year #yob (Year of birth) - this codes pulls the year from the above computation.
    return print(
"Hello {}, you are {} years old".format(name, age),"\n",
"Your year of birth is {}".format(yob))
capture_detail(name, age)

def age_group(age):
        if age < 1:
            age_range = "an infant."
        elif age == 1 or age <= 11:
            age_range = "a child."
        elif age == 12 or age <= 17:
            age_range = "a teenager."
        elif age == 18 or age <= 64:
            age_range = "an adult."
        else:
            age_range = "an older adult."
        return age_range
        
print("As you are {} years old, you are {} ".format(age, age_group(age)))        
     
#Creates a list for ages and years
ages = []
years = [] 
    
for i in range(10,60,10): #creates lists for ages and years in the range parsed, with the computation 
    age_new = age + i
    ages.append(age_new)
    year_new = current_year + i
    years.append(year_new)


for i in range(len(ages)): 
    cal_age = ages[i]
    cal_year = years[i]
    print("In {}, you will be {} years old.".format(cal_year, cal_age))
    
