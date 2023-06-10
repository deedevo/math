import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pandas_datareader import data as pdr
import yfinance as yf
from scipy.stats import pearsonr


yf.pdr_override()

# Define the time period
start_date = '2013-01-01'
end_date = '2023-01-01'

# Fetch the stock prices from Yahoo Finance
df = pdr.get_data_yahoo('AAPL', start=start_date, end=end_date)

# Select only the 'Close' prices
df = df[['Close']]

# Add a column for the days
df['Days'] = np.arange(len(df))

# Split the data into features (X) and target (y)
X = df[['Days']].values
y = df['Close'].values

# Create a linear regression model and fit the data
regression_model = LinearRegression()
regression_model.fit(X, y)

# Get the coefficients and intercept of the linear regression line
slope = regression_model.coef_[0]
intercept = regression_model.intercept_

# Plot the actual data
plt.scatter(X, y, color='b', label='Actual Price')

# Plot the regression line
plt.plot(X, regression_model.predict(X), color='r', label='Regression Line')

# Add labels and title
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Linear Regression - AAPL Stock Price')

# Add legend
plt.legend()

# Show the plot
plt.show()

# Define the number of days in the future for prediction
future_days = 365

# Create an array of future days
future_X = np.arange(len(df), len(df) + future_days).reshape(-1, 1)

# Predict the future prices
future_prices = regression_model.predict(future_X)


# Calculate the correlation coefficient and p-value
correlation_coef, p_value = pearsonr(X, y)

# Display the correlation coefficient
print("Correlation Coefficient:", correlation_coef)
