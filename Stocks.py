import datetime as dt
import pandas_datareader.data as web

start = dt.datetime(2019,1,1)
end = dt.datetime(2020,12,31)

df = web.DataReader ('WEGE3.SA', 'yahoo', start, end)
