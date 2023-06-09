import matplotlib.pyplot as plt 
plt.style.use('ggplot')
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import pandas as pd 
import seaborn as sns
plt.rcParams['figure.figsize'] = (12, 8)

#Visualização dos dados e propriedades
data = pd.read_csv('dados.txt') # Carrega os dados do arquivo 'dados.txt'
data.head() # Exibe as primeiras linhas do conjunto de dados
data.info() # Exibe informações sobre o conjunto de dados

#Plotando os dados livremente
ax = sns.scatterplot(x="Population", y="Profit", data=data)
ax.set_title("Profit in $10000 vs City Population in 10000")
plt.show()

#Calculando a Função de Perda J(θ)
def cost_function(X, y, theta):
    m = len(y)
    y_pred = X.dot(theta)
    error = (y_pred - y) ** 2
    return 1 / (2 * m) * np.sum(error)
m = data.Population.values.size
X = np.append(np.ones((m, 1)), data.Population.values.reshape(m, 1), axis=1)
y = data.Profit.values.reshape(m, 1)
theta = np.zeros((2, 1))

cost_function(X, y, theta)

#Método do gradiente (min da função)
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    costs = []
    for i in range(iterations):
        y_pred = X.dot(theta)
        error = np.dot(X.transpose(), (y_pred - y))
        theta -= alpha * 1/m * error
        costs.append(cost_function(X, y, theta))
    return theta, costs
theta, costs = gradient_descent(X, y, theta, alpha=0.01, iterations=2000) # Executa o método do gradiente
print("h(x) = {} + {}x1".format(str(round(theta[0, 0], 2)),
                                str(round(theta[1, 0], 2)))) # Exibe os valores otimizados de theta

#Plotando a Função de Perda J(θ)
theta_0 = np.linspace(-10, 10, 100)
theta_1 = np.linspace(-1, 4, 100)
cost_values = np.zeros((len(theta_0), len(theta_1)))
for i in range(len(theta_0)):
    for j in range(len(theta_1)):
        t = np.array([theta_0[i], theta_1[j]])
        cost_values[i, j] = cost_function(X, y, t)
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(theta_0, theta_1, cost_values, cmap = 'viridis')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.xlabel("$\Theta_0$")
plt.ylabel("$\Theta_1$")
ax.set_zlabel("$J(\Theta)$")
ax.view_init(30, 330)
plt.show()

#Plotando a Convergência 
plt.plot(costs)
plt.xlabel("Iterations")
plt.ylabel("$J(\Theta)$")
plt.title("Values of the Cost Function over iterations of Gradient Descent")
plt.show()

#Ajuste da regressão linear
theta = np.squeeze(theta)
sns.scatterplot(x="Population", y="Profit", data=data)
x_value = [x for x in range(5, 25)]
y_value = [(x * theta[1] + theta[0]) for x in x_value]
plt.plot(x_value, y_value, 'r')
plt.xlabel("Population in 10000s")
plt.ylabel("Profit in $10,000s")
plt.title("Linear Regression Fit")
plt.show()

#Inferência usando os valores otimizados de θ (h_θ(x) = θ^T x)
def predict(x, theta):
    y_pred = np.dot(theta.transpose(), x)
    return y_pred
y_pred_1 = predict(np.array([1,4]), theta) * 10000
print ("For a population of 40,000 people, the model predicts a profit of $" + str(round(y_pred_1, 0)))
y_pred_2 = predict(np.array([1,8.3]), theta) * 10000
print ("For a population of 40,000 people, the model predicts a profit of $" + str(round(y_pred_2, 1)))
