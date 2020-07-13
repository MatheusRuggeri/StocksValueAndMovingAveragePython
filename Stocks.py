import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Start and End dates
start = dt.datetime(2019,1,1)
end = dt.datetime(2020,12,31)

# Uses Panda Reader to import all the values from Yahoo API
df = web.DataReader ('WEGE3.SA', 'yahoo', start, end)

# Moving Average vector
movingAverage = []
movingAverage.append(7)
movingAverage.append(15)
movingAverage.append(30)
movingAverage.append(90)
movingAverage.append(180)
movingAverage.append(365)


# Moving Average
for i in movingAverage:
    df[str(i)+'ma'] = df['Adj Close'].rolling(window=i).mean()

# Creates 2 subplots, the first with 5/6 height
ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex=ax1)

# Set the img size
plt.gcf().set_size_inches(16, 10);
    
# Creates a line to the price and put dots in each adjusted price
ax1.plot(df.index, df['Adj Close'], 'r')
ax1.plot(df.index, df['Adj Close'], 'r.')
for i in movingAverage:
    ax1.plot(df.index, df[str(i)+'ma'], 'b')

# Plot the volume in the small graphic below
ax2.bar(df.index, df['Volume'])

# Display the image
plt.show()
