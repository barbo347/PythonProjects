# Implementação de Regressão Linear Univariada

Este projeto tem como objetivo implementar um algoritmo de regressão linear univariada do zero usando Numpy e Python, além de criar visualizações de dados e gráficos utilizando a biblioteca Matplotlib.

## Objetivos do projeto

1. Implementar o algoritmo de descida do gradiente do zero.
2. Realizar uma regressão linear univariada com Numpy e Python.
3. Criar visualizações de dados e gráficos usando Matplotlib.

## Passos para alcançar os objetivos

1. Visualização dos dados:
   - Carregar os dados do arquivo 'dados.txt'.
   - Exibir as primeiras linhas do conjunto de dados.
   - Verificar as informações sobre o conjunto de dados.

2. Plotar os dados:
   - Utilizar a biblioteca Seaborn e a função scatterplot para plotar um gráfico de dispersão dos dados.
   - Configurar os rótulos dos eixos e o título do gráfico.
   - Exibir o gráfico plotado.

3. Cálculo da função de perda J(θ):
   - Definir a função `cost_function(X, y, theta)` para calcular a função de perda J(θ).
   - Calcular a função de perda para os dados utilizando os parâmetros theta inicializados com zeros.

4. Método do gradiente (minimização da função de perda):
   - Definir a função `gradient_descent(X, y, theta, alpha, iterations)` para realizar o método do gradiente.
   - Executar o método do gradiente com os parâmetros alpha (taxa de aprendizado) e iterations (número de iterações) desejados.
   - Exibir os valores otimizados de theta.

5. Plotar a função de perda J(θ):
   - Criar uma grade de valores para theta_0 e theta_1.
   - Calcular a função de perda para cada par de valores de theta_0 e theta_1.
   - Utilizar a biblioteca Matplotlib e a função plot_surface para plotar um gráfico 3D da função de perda.
   - Configurar os rótulos dos eixos e o título do gráfico.
   - Exibir o gráfico plotado.

6. Plotar a convergência:
   - Utilizar a biblioteca Matplotlib e a função plot para plotar um gráfico da função de perda ao longo das iterações.
   - Configurar os rótulos dos eixos e o título do gráfico.
   - Exibir o gráfico plotado.

7. Ajuste da regressão linear:
   - Utilizar a biblioteca Seaborn e a função scatterplot para plotar novamente o gráfico de dispersão dos dados.
   - Calcular os valores de y correspondentes aos valores de x utilizando os parâmetros otimizados de theta.
   - Utilizar a função plot para traçar uma linha representando a regressão linear ajustada.
   - Configurar os rótulos dos eixos e o título do gráfico.
   - Exibir o gráfico plotado.

8. Inferência com os valores otimizados de θ:
   - Definir a função `predict(x, theta)` para realizar a inferência utilizando os valores
