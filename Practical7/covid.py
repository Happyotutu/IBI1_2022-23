import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/asus/IBI1_2022-23/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
print(covid_data.head(5))
covid_data.info()
print(covid_data.info())
covid_data.describe()
print(covid_data.describe())
# The mean of new cases is 194.546773. Standard deviation is 2083.395028.
# The range of total cases is 0 - 777798.000000.

print(covid_data.iloc[0,1])
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
# print(covid_data.iloc[0:1001:100,1])
covid_data.iloc[0:3,[0,1,3]]
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3,my_columns]
my_columns = [True, False]
# print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])
#print(covid_data.loc[0:81,"total_cases"])
# covid_data.loc[:, "location"]
my_raws = covid_data["location"] == "Afghanistan"
print(covid_data.loc[my_raws, "total_cases"])
raws = covid_data["date"] == "2020-03-31" 
columns = [False, True, True, True, False, False]
new_data = covid_data.loc[raws, columns]
print(new_data)
cases = new_data.loc[1:, "new_cases"]#The number of new cases was taken out
deaths = new_data.loc[1:, "new_deaths"]#The number of new deaths was taken out
print(np.average(cases))
print(np.average(deaths))
# The mean new cases is 640.461538. The mean new death is 37.928205. The number of patients increased on the day. 
#The proportion of new deaths as a proportion of the new cases on 31 March is 5.922%
 
#draw boxplot of new cases
data= new_data.loc[:, "new_cases"]
plt.boxplot(data,sym='o',whis=1.5)
plt.title('The new cases for the whole world on March 31st 2020')
plt.show()
#draw boxplot of new deaths
data= new_data.loc[:, "new_deaths"]
plt.boxplot(data,sym='o',whis=1.5)
plt.title('The new deaths for the whole world on March 31st 2020')
plt.show()

#plot the data for the whole world over time
world_dates=covid_data.loc[:, "date"]
world_new_cases=covid_data.loc[:,"new_cases"]
plt.plot(world_dates, world_new_cases, 'b+')
#1plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#plt.plot(world_dates, world_new_cases, 'r+')
#plt.plot(world_dates, world_new_cases, 'bo')
plt.title('The new cases for the whole world over time')
plt.show()

#plot the data for the new cases and new deaths
world_new_deaths=covid_data.loc[:,"new_deaths"]
world_dates=covid_data.loc[:, "date"]
world_new_cases=covid_data.loc[:,"new_cases"]
plt.legend(['world new deaths', 'world new cases'], loc='upper left')
plt.plot(world_dates, world_new_deaths, 'r+', label='new deaths') 
plt.plot(world_dates, world_new_cases, 'b+', label='new cases')
plt.legend(loc=2, ncol=3)
plt.title('The new cases and deaths for the whole world over time')
plt.show()

#Try to Answer Question: How have new cases and total cases developed over time in the UK?
raw1 = covid_data["location"] == "United Kingdom"
Chi = covid_data.loc[raw1,:]
print(Chi)
UK_new_cases=Chi.loc[:,"new_cases"]
UK_total_cases=Chi.loc[:,"total_cases"]
UK_dates=Chi.loc[:,"date"]
plt.legend(['UK new cases', 'UK total cases'], loc='upper left')
plt.plot(UK_dates, UK_total_cases, 'r+', label='total cases') 
plt.plot(UK_dates, UK_new_cases, 'b+', label='new cases')
plt.legend(loc=2, ncol=3)
plt.title('The new cases and total cases for UK over time')
