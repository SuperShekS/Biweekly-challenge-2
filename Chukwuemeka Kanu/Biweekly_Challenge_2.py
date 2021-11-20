#!/usr/bin/env python
# coding: utf-8

# In[23]:


"""
- Bi Weekly Challenge 2
OBJECTIVE:
- Collect and print user's data
- Check and print user's age category
- Calculate user's age in decades
"""


## A function (users_data) housing the entire code. Calling the function activates program to start collecting data dnd
## printing outputs

def users_data():
    try: 
        ## Making sure users don't input digits for names
        while True:
            name_input = input('input your name: ')
            if name_input.isdigit():
                print('Sorry: Name required in Alphabets')
                continue
            else:
                break
        ## Collecting user's age
        age_input = int(input('input your age: ')) 
        print('Hello', name_input,', you are', age_input, 'years old')
    
    except ValueError:
        print('Try Again: Input the correct value')

    ## Collecting user's Date of birth and printing current age
    dob = 2021 - age_input
    print('Your year of Birth is', dob)

    # Finding user's age group
    if age_input<1:
        print('As you are', age_input, 'years old, you are an Infant')
    elif age_input<=11:
        print('As you are', age_input, 'years old, you a an Child')
    elif age_input<=17:
        print('As you are', age_input, 'years old, you are a Teen')
    else:
        print('As you are', age_input, 'years old, you are an Adult')

    # Calculating users age after every decade
    decades = range(-10,51,10)
    decade_age = 0
    for i in decades:
        decade_calculation = 2021 + i
        decade_age = age_input + i
        print('In', decade_calculation, 'you were', decade_age, 'years old')
        
users_data()


# In[ ]:




