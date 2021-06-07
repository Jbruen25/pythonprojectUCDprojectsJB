# Create and print list names
names = ['Apple Inc', 'Coca Cola','Walmart']
print(names)

# Create and print list names
prices = [159.54, 37.13, 71.17]
print(prices)

# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(names[-1])

# prices
prices = [159.54, 37.13, 71.17]

# Use exteneded slicing on the list price
prices_subset = prices[:2]
print(prices_subset)

# Create and print the nexted list stocks
stocks = [names, prices]
print (stocks)

# Use list indexing to obtain the list of prices
print (stocks[1])

# Use the indexing to obtain company name Coca Cola
print(stocks[0][1])

# Use indexing to obtain 71.17
print(stocks[1][2])

# Print the sorted list prices
prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)

# Find the maximum price in the list price
prices = [159.54, 37.13, 71.17]
prices_max = max(prices)
print(prices_max)

# Apend a name to the list names
names.append('Amazon.com')
print(names)

# Extend list names
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)


# Import numpy as np
import numpy as np

# list
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [ 9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# NumPy arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Print the array
print(prices_array)
print(earnings_array)

# Import numpy as np
import numpy as np

# Create PE ratio array
pe_array = np.array(prices_array/earnings_array)

# Print pe_array
print(pe_array)

# subset first three elements
prices_subset_1 = prices_array[:3]
print(prices_subset_1)

#subset last three elements
prices_subset_2 = prices_array[-3:]
print(prices_subset_2)

#subset every third element
prices_subset_3 = prices_array[0:7:3]
print(prices_subset_3)

# Import numpy as np
import numpy as np

# Create a 2D array of prices and earnings
stock_array = np.array([prices, earnings])
print(stock_array)

# Print the shape of stock_array
print(stock_array.shape)

# Print the size of stock_array
print(stock_array.size)

# Transpose stock_array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)

# Print the shape of stock_array
print(stock_array_transposed.shape)

# Print the size of stock_array
print(stock_array_transposed.size)

# Subset prices from stock_array_transposed
prices = stock_array_transposed[:,0]
print(prices)

# Subset earnings from stock_array_transposed
earnings = stock_array_transposed[:,1]
print(earnings)

# Subset price and earnings for first company
company_1 = stock_array_transposed[0,:]
print(company_1)

# Calculate the mean
prices_mean = np.mean(prices)
print(prices_mean)

# Calculate the standard deviation
prices_std = np.std(prices)
print(prices_std)

# Import numpy as np
import numpy as np

# Create and print company IDs
company_ids = np.arange(1,8,1)
print(company_ids)

# Use array slicing to select specfic company IDs
company_ids_odds = np.arange(1,8,2)
print(company_ids_odds)

# list
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
days = [ 10, 50, 100, 150, 200, 250, 300]

# Import matplotlib.pyplot with the alisa pit
import matplotlib.pyplot as plt

# Plot the price of stock over time
plt.plot(days, prices, linestyle="--")

# Display the plot
plt.show()

# Plot prices as a function of time
plt.plot(days, prices, linestyle="--")

# Add x and y labels
plt.xlabel('Days')
plt.ylabel('prices, $')

# Add plot title
title('company Stock Prices Over Time')

# Show plot
plt.show()

# Plot two lines of varing colors
plt.plot(days, prices1, color='red')
plt.plot(days, prices2, color='green')

# Add labels
plt.xlabel('Days')
plt.ylabel('prices, $')
plt.title('company Stock Prices Over Time')
plt.show()

# Plot histogram of stocks_A
plt.hist(stock_A, bin=100, alpha=0.4)

# Plot histogram of stocks_B
plt.hist(stock_B, bin=100, alpha=0.4)

# Display plot
plt.show()


crash_text = "Friday the 13th, Oct, 1989"

# Create a format string mapping the text
crash_format_str = "%Y the %dth, %b, %m"
min_crash = datetime.datetime.strptime(crash_text, crash_format_str)
print(min_crash)

recession_text = "07/03/90"

# Create format string
recession_format_str = "%Y/%m/%d"

# Create datetime from text using format string
nineties_rec = datetime.datetime.strptime(____, ____)
print(nineties_rec)

ttttt
rrrrr