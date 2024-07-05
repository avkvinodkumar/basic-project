#Python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
weather_data = pd.read_csv('weather_data.csv')

# View the first few rows of the dataset
print(weather_data.head())

# Check the data types of each column
print(weather_data.info())

# Calculate the average temperature and precipitation for each month
monthly_avg_temp = weather_data.groupby(weather_data['date'].dt.strftime('%Y-%m'))['temperature'].mean()
monthly_avg_precipitation = weather_data.groupby(weather_data['date'].dt.strftime('%Y-%m'))['precipitation'].mean()

# Plot the average temperature and precipitation for each month
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg_temp.index, monthly_avg_temp.values, label='Average Temperature')
plt.plot(monthly_avg_precipitation.index, monthly_avg_precipitation.values, label='Average Precipitation')
plt.xlabel('Month')
plt.ylabel('Average Value')
plt.title('Monthly Average Temperature and Precipitation')
plt.legend()
plt.show()

# Calculate the number of days with precipitation for each month
monthly_precipitation_days = weather_data.groupby(weather_data['date'].dt.strftime('%Y-%m'))['precipitation'].sum()
monthly_precipitation_days[monthly_precipitation_days > 0].plot(kind='bar', figsize=(10, 6))
plt.title('Number of Days with Precipitation by Month')
plt.xlabel('Month')
plt.ylabel('Number of Days')
plt.show()
