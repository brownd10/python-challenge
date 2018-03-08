#create dependencies to be used
import os
import sys
import pandas as pd

#read in the files
employee1 = pd.read_csv('employee_data1.csv')
employee2 = pd.read_csv('employee_data2.csv')

#check for status of dataframe on first data set
type(employee1)

#check for status of dataframe on second data set
type(employee2)

#verify columns of employee1 dataframe
employee1.columns

#verify columns of employee2 dataframe
employee2.columns

#show first five rows of employee1 dateframe
employee1.head()

#show first five rows of employee2 dateframe
employee2.head()

#combine the two dataframes
employee_all = employee1.append(employee2)
employee_all

#rename Name column
employee_all.rename(columns = {'Name':'First Name'}, inplace = True)

employee_all.columns

#add new column for Last Name
employee_all['Last Name'] = 'Brown'

#reorder the columns
employee_final=employee_all[['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]