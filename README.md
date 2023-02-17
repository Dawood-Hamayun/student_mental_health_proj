# student_mental_health_proj

## resources 
https://www.kaggle.com/datasets/shariful07/student-mental-health


## Step 1 (Cleaning Data)

### Steps Performed:
1. Dealt with missing values on Age column (replaced with mean of column)
2. Converted TimeStamp into date_time and divided into hours, days, and months
3. Renamed all columns
4. Made values lower cased
5. Generalized courses into either Sciences or Arts (Due to small dataset)
6. Split Year into numeric values
7. Categorized CGPA into Grades and classified into binary
8. Converted categorical values in Question related columns to binary
9. Converted Gender into binary

**Note**: Most of the categorical data has been converted into numerical data as model performs much better with non-categorical data. Moreover, there is plenty of unnecessary data present inside the dataset that probably won't be of any use, but is still included to maximize learning to deal with data. 

### Common Functions involved in the step:
isnull(), fillna(), apply(), map(), to_datetime, replace(), read_csv(), to_csv(), type(), iloc[], rename()

### Libraries Used in the step:
Pandas, NumPy

### Technology Used in the step:
Spyder

## Step 2 (Exploratory Data Analysis)

**Disclaimer**: The analysis is performed on a relatively small dataset. Furthermore, these findings are just for the purpose of the project itself and to practice data insights.

### Steps Performed:
1. As Depression, Anxiety, and Panic Attack can all be considered in the category of mental health, these were all classified into a single column with binary values
2. Another column made with the same purpose as above but with categorical values (mainly for visualization)
3. Basic visualization for getting insights from useful data (further explained in findings section)  


### Findings and insights: 
1. Most individuals are female
2. People who are suffering from Depression are most likely suffering from Anxiety or Panic Attacks as well (But not all of them)
3. Although data is still insufficient to make a conclusion, but initial impression leads to believe that lower CGPA does not really imply a bad mental state
4. From the data gathered so far, it can be seen clearly how Marital status can be one of the biggest factors leading to some sort of bad mental state (100% effect on males)
5. Even with courses categorized as either Science or Arts, there isn't that big of a difference between individuals belong to either when it comes to a bad mental state
6. Anxiety seems to be more common in females. 
7. With correlation matrix, it seems Marital status and CGPA are the biggest factors followed by Year, Age, and Gender. 
8. Even though Female sample is much bigger, Males can be considered more inclinded towards poor mental health (Averaging total sample from affected individuals after grouping by Gender)
9. First Year students were the most affected individuals in the dataset (Although they made up most of the individual count)


### Plotting Techniques Used:
Countplot(), Barplot(), Heatmap().


### Functions Used:
read_csv(), head(), info(), describe(), apply(), corr(), value_counts(), groupby(), size()

get_values(), get_cat() -> User Defined


### Libraries Used in the step:
Pandas, Matplotlib.pyplot, Seaborn


### Technology Used:
Jupyter Notebook
