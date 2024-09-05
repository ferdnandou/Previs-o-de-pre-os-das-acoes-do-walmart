# Previsão de Preços das Ações do Walmart

Este projeto realiza uma análise de séries temporais dos preços das ações do Walmart para prever os preços futuros e fornecer uma recomendação de compra ou venda com base nos dados históricos de 2010 a 2024. Utilizamos o modelo ARIMA para as previsões e analisamos o crescimento percentual dos preços para avaliar as decisões de investimento.

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Resultados](#resultados)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

O objetivo deste projeto é prever os preços das ações do Walmart usando modelos de séries temporais e fornecer uma análise de decisão de compra ou venda com base no crescimento percentual dos preços entre 2010 e 2024. A análise inclui:

- Treinamento de um modelo ARIMA com os dados históricos.
- Previsão dos preços das ações para um período de teste.
- Avaliação do modelo usando o erro quadrático médio (RMSE).
- Cálculo do crescimento percentual dos preços das ações e análise dos dividendos pagos entre 2010 e 2024.

## Tecnologias Utilizadas

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Scikit-learn

## Estrutura do Projeto

```
├── WMT.csv                   # Dados históricos das ações do Walmart
├── analysis.py               # Script Python para análise e previsão
└── README.md                 # Documentação do projeto
```

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
   
2. Instale as dependências:
   ```bash
   pip install pandas numpy matplotlib statsmodels scikit-learn
   ```
   
3. Execute o script `analysis.py`:
   ```bash
   python analysis.py
   ```

## Resultados

- O modelo ARIMA foi treinado com os dados de preços de fechamento das ações do Walmart.
- As previsões do modelo foram comparadas com os dados reais para avaliar a precisão usando RMSE.
- A análise de investimento baseada nos números de 2024 mostrou um crescimento percentual de XX% e recomendou uma decisão de **comprar/vender** ações do Walmart em 2010.
