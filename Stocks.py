import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import csv

# Import the list with all stocks to be analyzed
data = []
with open('import/list.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row[0])
    
# Start and End dates
start = dt.datetime(2017,7,1)
end = dt.datetime(2020,12,31)

for stocks in data:
    print(stocks)
    # Uses Panda Reader to import all the values from Yahoo API and save
    df = web.DataReader (str(stocks)+'.SA', 'yahoo', start, end)
    df.to_csv("export/csv/" + stocks + ".csv")
    
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
    
    # Create a new date column, this column accepts .tail or .head
    df['Date'] = df.index
    
    # Creates a figure with 2 subplots, the first with 5/6 height
    fig = plt.figure()
    ax1 = plt.subplot2grid((20,1), (0,0), rowspan = 16, colspan = 1)
    plt.title(str(stocks), fontsize=25)
    ax2 = plt.subplot2grid((20,1), (17,0), rowspan = 3, colspan = 1, sharex=ax1)
    
    # Set the img size
    plt.gcf().set_size_inches(16, 10)
        
    # Creates a line to the price and put dots in each adjusted price
    ax1.plot(df['Date'].tail(365), df['Adj Close'].tail(365), 'r')
    ax1.plot(df['Date'].tail(365), df['Adj Close'].tail(365), 'r.')
    
    colorIndex = 0
    for i in movingAverage:
        ax1.plot(df['Date'].tail(365), df[str(i)+'ma'].tail(365), color[colorIndex], label=str(i)+' M.A.')
        colorIndex += 1
    
    # Print the legend
    legend = ax1.legend(loc='upper center', shadow=True, fontsize='x-large')
    
    # Plot the volume in the small graphic below
    ax2.bar(df['Date'].tail(365), df['Volume'].tail(365), color='b')
    
    # Display the image
    plt.show()
    
    fig.savefig("export/img/" + stocks + ".png", dpi = 300)
    plt.close(fig)
