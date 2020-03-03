# Get projected total sales.
# 2/20/2020
# CTI-110 P2T1-Sales Prediction
# Koby Forbes
#
total_sales = float(input('Enter projected sales: '))

# Calculate th profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
