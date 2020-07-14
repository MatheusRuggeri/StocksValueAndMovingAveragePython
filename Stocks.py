import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Start and End dates
start = dt.datetime(2017,7,1)
end = dt.datetime(2020,12,31)

# Uses Panda Reader to import all the values from Yahoo API
df = web.DataReader ('WEGE3.SA', 'yahoo', start, end)
df.to_csv("export/WEGE3.csv")

# Moving Average vector
movingAverage = [];         color = [];
movingAverage.append(7);    color.append('b');
movingAverage.append(15);   color.append('g');
movingAverage.append(30);   color.append('c');
movingAverage.append(90);   color.append('m');
movingAverage.append(180);  color.append('y');
movingAverage.append(365);  color.append('b');


# Moving Average
for i in movingAverage:
    df[str(i)+'ma'] = df['Adj Close'].rolling(window=i).mean()

df['Date'] = df.index

# Creates 2 subplots, the first with 5/6 height
ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex=ax1)

# Set the img size
plt.gcf().set_size_inches(16, 10);
    
# Creates a line to the price and put dots in each adjusted price
ax1.plot(df['Date'].tail(365), df['Adj Close'].tail(365), 'r')
ax1.plot(df['Date'].tail(365), df['Adj Close'].tail(365), 'r.')

colorIndex = 0
for i in movingAverage:
    ax1.plot(df['Date'].tail(365), df[str(i)+'ma'].tail(365), color[colorIndex], label=str(i)+' M.A.')
    colorIndex += 1

legend = ax1.legend(loc='upper center', shadow=True, fontsize='x-large')

# Plot the volume in the small graphic below
ax2.bar(df['Date'].tail(365), df['Volume'].tail(365), color='b')

# Display the image
plt.show()
