# student_mental_health_proj

## resources 
https://www.kaggle.com/datasets/shariful07/student-mental-health


## Step 1 (Cleaning Data)

### Steps Performed
1. Dealt with missing values on Age column (replaced with mean of column)
2. Converted TimeStamp into date_time and divided into hours, days, and months
3. Renamed all columns
4. Made values lower cased
5. Generalized courses into either Sciences or Arts (Due to small dataset)
6. Split Year into numeric values
7. Categorized CGPA into Grades and classified into binary
8. Converted categorical values in Question related columns to binary
9. Converted Gender into binary

Note: Most of the categorical data has been converted into numerical data as model performs much better with non-categorical data.

### Common Functions involved in the step
isnull(), fillna(), apply(), map(), to_datetime, replace(), read_csv(), to_csv(), type(), iloc[], rename()

### Libraries Used in the step
Pandas, NumPy
