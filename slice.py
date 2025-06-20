movieName = "Top Gun"
#Dentro dessa string vou ter [inicio e fim] - lembrando que indice começa na posição 0 e vai ate a posição final, que é  indice -1

#1 - Buscar toda String á partir da primeira posição
print (movieName[0:])

#2 - Buscar toda Strig até a última posição
print (movieName [:7])

#3 - Buscar toda STring desde o começo
print(movieName [2:])

"""
entro dessa string vou ter [inicio, fim e passo] - lembrando que indice começa na posição 0 e vai ate a posição final, que é  indice -1
passo - determina o incremento, que por padrão é 1.

"""

#4 - Buscar toda Strind de 2 e 2 caracteres
print(movieName[::2]) #vou pegando de 2 em 2 posições

#5 - Buscar toda STring nos indices impares 
print(movieName [1::2])

#6 - inverter String de trás para frente
print(movieName[::-1])
# -1, começa a contagem da direita para a esquerda