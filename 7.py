import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = {
    'Sales':[130,140,160,145]
}
df = pd.DataFrame(data)

model = ARIMA(df,order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps = 5)
print("forecast",forecast)
df.plot(label = "Historical data")
forecast.plot(label = "Forecast",legend = 'True',color = 'red',linestyle='--')
plt.title("Salws o srima")
plt.show()
