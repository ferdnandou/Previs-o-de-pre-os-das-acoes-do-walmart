##Análise de Séries Temporais com ARIMA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")

file_path = 'WMT.csv'
data = pd.read_csv(file_path)

print(data.head())

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

prices = data['Close']

plt.figure(figsize=(10, 5))
plt.plot(prices)
plt.title('Preços das Ações do Walmart ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.show()

train_size = int(len(prices) * 0.8)
train, test = prices[:train_size], prices[train_size:]

print(f"Tamanho do treino: {len(train)}, Tamanho do teste: {len(test)}")

model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit()

predictions = model_fit.forecast(steps=len(test))

plt.figure(figsize=(10, 5))
plt.plot(test.index, test, label='Dados Reais')
plt.plot(test.index, predictions, color='red', label='Previsões ARIMA')
plt.title('Previsões de Preços das Ações do Walmart')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend()
plt.show()

rmse = np.sqrt(mean_squared_error(test, predictions))
print(f'Erro Quadrático Médio (RMSE): {rmse:.2f}')

##Análise de Investimento (Compra ou Venda)
data_filtered = data[(data.index.year >= 2010) & (data.index.year <= 2024)]

start_price = data_filtered['Close'].loc[data_filtered.index.min()]
end_price = data_filtered['Close'].loc[data_filtered.index.max()]
growth = ((end_price - start_price) / start_price) * 100

if 'Dividends' in data_filtered.columns:
    total_dividends = data_filtered['Dividends'].sum()
else:
    total_dividends = 0

print(f"\nPreço inicial em 2010: ${start_price:.2f}")
print(f"Preço final em 2024: ${end_price:.2f}")
print(f"Crescimento percentual de 2010 a 2024: {growth:.2f}%")
print(f"Total de dividendos pagos: ${total_dividends:.2f}")

if growth > 0:
    decision = "comprar"
else:
    decision = "vender"

print(f"Baseando-se nos números de 2024, a decisão em 2010 seria: {decision} ações do Walmart.")
