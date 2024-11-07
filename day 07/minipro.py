import pandas as pd # type: ignore

# Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 78, 92, 88, 76],
    'Science': [90, 82, 85, 95, 80],
    'English': [88, 79, 93, 85, 77]
}

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculate the average grade for each student
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Display the DataFrame with the average grades
print("\nDataFrame with Average Grades:")
print(df)

# Calculate the overall average grade for each subject
average_grades = df[['Math', 'Science', 'English']].mean()

# Display the overall average grades
print("\nOverall Average Grades:")
print(average_grades)

# Find the student with the highest average grade
top_student = df.loc[df['Average'].idxmax()]

# Display the top student
print("\nTop Student:")
print(top_student)
