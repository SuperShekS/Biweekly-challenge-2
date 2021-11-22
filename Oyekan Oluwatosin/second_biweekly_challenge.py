# # Bi-weekly Challenge 

# ### Write a python program that prompts for inputs from the user. The inputs should be the user's name and the age.


def age_func(input):
    
# declare user's name and age input
    try:
        user_name= str(input())
        age = int(input())

        # concatinate the strings and input
        print('Hello ' + user_name + ',' + ' you are ' + str(age) + ' years old')
    except ValueError:
        print('Oops that was not a valid number')
    except TypeError:
        print('Argument must be a number')
    try:
        year = 2020
        user_DOB = year - age
        # Print the user’s age
        print('Your year of birth is ' + str(user_DOB ))
    except ValueError:
        print('Oops that was not a valid number')
    except TypeError:
        print('Argument must be a number')

    # State which age group the user belongs to

# Legend
# Infants: <1
# Children: 1-11 years
# Teens: 12-17 
# Adults: 18-64
# Older Adults: 65+
    
    if age < 1:
        print('As you are ' + str(age) + ' years old, you are an infant')
    elif (age >=1) & (age <=11):
        print('As you are ' + str(age) + ' years old, you are a children')
    elif (age >=12) & (age <=17):
        print('As you are ' + str(age) + ' years old, you are a teen')
    elif (age >=18) & (age <=64):
        print('As you are ' + str(age) + ' years old, you are an adult')
    else:
        print('As you are ' + str(age) + ' years old, you are a older adult')
        
        
    decade_age = age - 10
    print('I was ' + str(decade_age) + 'years old a decade ago')
    
    
    new_age = []
    new_year = [] 
    

    for x in range(10,60,10): 
        age_new = age + x
        new_age.append(age_new)
        year_new = x + year
        new_year.append(year_new)
    
    for x in range(len(new_age)):
          new_a = new_age[x]
          new_y = new_year[x]

          print(" In " + str(new_y) + " i'll be " + str(new_a) + "y.o")


# In[15]:


age_func(input)

