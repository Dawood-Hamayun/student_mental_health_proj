# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:38:50 2023

@author: dawood
"""
# Import Libraries
import pandas as pd
import numpy as np

#Read DataFrame
df = pd.read_csv('Student Mental health.csv')

#Initial Findings or things to look at
 
# 1. Deal with missing values
df['Age'].isnull()
df['Age'] = df['Age'].fillna(value = df['Age'].mean().ceil())
# 2. Is there something that needs to be done with timestamp?
# Converted String into datetime object and made 3 new columns
type(df['Timestamp'].iloc[0])
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Hour'] = df['Timestamp'].apply(lambda time: time.hour)
df['Month'] = df['Timestamp'].apply(lambda time: time.month)
df['Day of Week'] = df['Timestamp'].apply(lambda time: time.dayofweek)
dmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu',4:'Fri', 5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# 3. Deal with column names
df.info()
df.columns
df.rename(columns = {'Choose your gender': 'Gender', 'What is your course?': 'Course', 
                     'Your current year of Study': 'Year', 'What is your CGPA?':'CGPA',
                     'Do you have Depression?': 'Depression', 'Do you have Anxiety?': 'Anxiety',
                     'Do you have Panic attack?':'Panic Attack', 
                     'Did you seek any specialist for a treatment?': 'Seeked Help'},
                      inplace = True)


# 4. Deal with course column (Lower case, Categorize into something general)
df['Course'] = df['Course'].apply(lambda x: x.lower())
df['Course'].unique()

df['Course'] = df['Course'].replace(['engineering', 'bit', 'mathemathics', 'bcs', 'psychology'
                                     , 'enm', 'marine science', 'engine', 'engin', 
                                     'biomedical science', 'it', 'mhsc', 'biotechnology'], 'Science')
df['Course'][df['Course'] != 'Science']   = 'Arts'      
df['Science'] = df['Course'].apply(lambda x: 1 if 'Science' in x else 0)
df['Arts'] = df['Course'].apply(lambda x: 1 if 'Arts' in x else 0)

# 5. Year column (same lower case) (Remove word 'year' in values)
df['Year'] = df['Year'].apply(lambda x: x.lower().split(' ')[1])


# 6. GPA (Division into Grades) (A+ for 3.50+, A for 3+, B for 2.50+, C for 2+, D for 0-1.99)
df['CGPA Rank'] = df['CGPA'].apply(lambda x: x.split('-')[1])
df['CGPA Rank'].unique()
df['A+'] = df['CGPA Rank'].apply(lambda x: 1 if '4.00' in x else 0)
df['A'] = df['CGPA Rank'].apply(lambda x: 1 if '3.49' in x else 0)
df['B'] = df['CGPA Rank'].apply(lambda x: 1 if '2.99' in x else 0)
df['C'] = df['CGPA Rank'].apply(lambda x: 1 if '2.49' in x else 0)
df['D'] = df['CGPA Rank'].apply(lambda x: 1 if '1.99' in x else 0)

# 7. Encode Last 4 columns to numeric
 df['Marital status'] = df['Marital status'].map({'Yes': 1, 'No': 0})
 df['Depression'] = df['Depression'].map({'Yes': 1, 'No': 0})
 df['Anxiety'] = df['Anxiety'].map({'Yes': 1, 'No': 0})
 df['Panic Attack'] = df['Panic Attack'].map({'Yes': 1, 'No': 0})
 df['Seeked Help'] = df['Seeked Help'].map({'Yes': 1, 'No': 0})
 
# 8. Convert Gender into Binary 
df['Gender'] = df['Gender'].map({'Female':0 , 'Male': 1})

df.to_csv('student_mental_health_cleaned.csv', index = False)
