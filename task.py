import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('C:/Users/jonat/Documents/GitHub/W03-Task-Reducing-Gun-Deaths/full_data.csv')

# Example: Engagement trends over months
data['Month'] = pd.to_datetime(data['date']).dt.month
monthly_engagement = data.groupby('Month')['engagement_metric'].mean()

plt.figure(figsize=(10, 6))
plt.plot(monthly_engagement, marker='o')
plt.title('Monthly Engagement Trends')
plt.xlabel('Month')
plt.ylabel('Engagement Metric')
plt.xticks(range(1, 13))
plt.grid()
plt.show()
