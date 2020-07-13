import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Start and End dates
start = dt.datetime(2019,1,1)
end = dt.datetime(2020,12,31)

# Uses Panda Reader to import all the values from Yahoo API
df = web.DataReader ('WEGE3.SA', 'yahoo', start, end)

# Creates 2 subplots, the first with 5/6 height
ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex=ax1)

# Set the img size
plt.gcf().set_size_inches(16, 10);
    
# Creates a line to the price and put dots in each price (adjusted)
ax1.plot(df.index, df['Adj Close'], 'r')
ax1.plot(df.index, df['Adj Close'], 'r.')

# Plot the volume in the small graphic below
ax2.bar(df.index, df['Volume'])

# Display the image
plt.show()
