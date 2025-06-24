moviesList = ["Titanic", "The God Father", "Frozen", "Carrosel"]

# 1 - Iterando valores de uma lista utilizando o while 
index = 0
#len para percorrer o tamanho
while index < len(moviesList):
    print(moviesList[index])
    index += 1 # percorre o tamanho da lista e para quando encontrar o último indice

# 2 - Quando a condição for atendida o looping será encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "Frozen":
        break
    print(moviesList[index])
    index += 1

# Continue - quando a condição for atendida, o looping vai para a próxima interação 
index = 0
while index < len(moviesList):
    if moviesList[index] == "Frozen":
        index += 1 
        continue
    print(moviesList[index])
    index += 1

# Avaliação do filme 
movieName = input("Informe o nome do filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

#contador 
total = 0 
count = 0

while count < movieRating :
    note = float(input("Digite a nota do filme: \n"))
    total += note
    count += 1

if movieRating > 0:
    #Média da avaliação do filme
    average = total / movieRating 
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")