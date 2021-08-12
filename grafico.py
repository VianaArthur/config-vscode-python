# importar o modulo
import matplotlib.pyplot as plt

# valores do eixo x
x = [1,2,3]

# valores do eixo y
y = [2,4,1]

# plotando os pontos
plt.plot(x, y)

# nomeando o eixo x
plt.xlabel('eixo x')

# nomeando o eixo y
plt.ylabel('eixo y')

# titulo do grafico
plt.title('Meu gráfico')

# mostrando o grafico
plt.show()
