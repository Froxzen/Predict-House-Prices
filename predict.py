import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('home_dataset.csv')

house_sizes = data['HouseSize'].values
house_prices = data['HousePrice'].values

plt.scatter(house_sizes, house_prices, marker = 'o', color = 'blue')
plt.title('House Prices vs House Size')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price ($)')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(house_sizes, house_prices, test_size=0.2, random_state=42)

X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

plt.scatter(X_test, y_test, marker='o', color='blue', label='Actual Prices')
plt.plot(X_test, predictions, color='red', linewidth=2, label='Predicted Prices')
plt.title('Property Price Prediction with Linear Regression')
plt.xlabel('House Size (sq.ft)')
plt.ylabel('House Price (millions $)')
plt.legend()
plt.show()