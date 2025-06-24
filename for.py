#Objetivo imprimir os filmes fora da lista

moviesList = ["Titanic", "The God Father", "Frozen", "Carrosel"]

# 1 - Iterando valores de uma lista 
for movies in moviesList:
    print(movies)

#  Quando usar o for, é importante saber usar o break, para encerrar o looping
for movies in moviesList:
    if movies == "Frozen":
        break
    print(movies)

# Continue - quando a condição for atendida, o looping vai para a próxima interação 
for movies in moviesList:
    if movies == "Frozen":
        continue
    print(movies)

# Avaliação do filme 
movieName = input("Informe o nome do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

#contador 
total = 0 
for i in range(movieRating):
    note = float(input("DIgite a nota para o filme: \n"))
    total += note 

if movieRating > 0:
    #Média da avaliação do filme
    average = total / movieRating 
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")