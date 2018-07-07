
import requests
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
import Config

ApiKey = Config.config['alphaVantageApiKey']

ts = TimeSeries(key=ApiKey, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data.plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()

ti = TechIndicators(key=ApiKey, output_format='pandas')
data, meta_data = ti.get_macd(symbol='MSFT',interval='1min')
data.plot()
plt.title('MACD for the MSFT stock (1 min)')
plt.show()
