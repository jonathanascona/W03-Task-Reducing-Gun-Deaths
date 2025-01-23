import pandas as pd

# Load the provided data files to explore their structure
file_path = r'C:\Users\jonat\Documents\GitHub\W03-Task-Reducing-Gun-Deaths\full_data.csv'

# Load the full_data.csv file
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print(data.head())
print(data.info())


#Dataset containes 11 columns


import matplotlib.pyplot as plt
import seaborn as sns

# Filter data for suicides only and clean up missing values
suicides = data[(data['intent'] == 'Suicide') & (data['age'].notna())]

# Group by month to analyze seasonal trends
monthly_suicides = suicides.groupby('month').size()

# Plot seasonal trends in suicides
plt.figure(figsize=(10, 6))
plt.plot(monthly_suicides.index, monthly_suicides.values, marker='o', linestyle='-', linewidth=2)
plt.title("Seasonal Trends in Suicides", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Number of Suicides", fontsize=12)
plt.xticks(range(1, 13), 
           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid()
plt.show()


# Gender distribution of suicides
gender_distribution = suicides['sex'].value_counts()

# Plot gender distribution as a pie chart
plt.figure(figsize=(8, 8))
gender_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'pink'])
plt.title("Gender Distribution of Suicides", fontsize=14)
plt.ylabel("")  # Remove y-axis label for cleaner pie chart
plt.show()

# Age group distribution of suicides
suicides['age_group'] = pd.cut(
    suicides['age'], 
    bins=[0, 14, 34, 64, 100], 
    labels=["0-14", "15-34", "35-64", "65+"],
    include_lowest=True
)

age_group_distribution = suicides['age_group'].value_counts().sort_index()

# Plot age group distribution as a bar chart
plt.figure(figsize=(10, 6))
age_group_distribution.plot(kind='bar', color='cornflowerblue')
plt.title("Suicides by Age Group", fontsize=14)
plt.xlabel("Age Group", fontsize=12)
plt.ylabel("Number of Suicides", fontsize=12)
plt.xticks(rotation=0)
plt.show()
