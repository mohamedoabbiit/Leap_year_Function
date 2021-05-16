#!/usr/bin/env python
# coding: utf-8

# In[19]:


year = int(input("Enter a year to check if year is a leap year or not: "))
def year_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
    
year_leap(year)


    


# In[8]:


2020


# In[7]:


2020


# In[ ]:





# In[17]:


year = int(input("please enter a year:"))

if not (year % 400 ) or (not year % 4 and year % 100):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")


# In[ ]:




