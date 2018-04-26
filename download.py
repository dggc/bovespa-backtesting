from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
# from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib
import matplotlib.pyplot as plt
import os
from pprint import pprint

ts = TimeSeries(key=os.environ['API_KEY'], output_format='pandas')
# Get json object with the intraday data and another with  the call's metadata
ticker = 'ABEV3.SA'
data, meta_data = ts.get_daily_adjusted(ticker, outputsize='full')
data['5. adjusted close'].plot()
plt.title('Adjusted Close Times Series for the %s stock (daily)' % (ticker))
plt.grid()
plt.show()