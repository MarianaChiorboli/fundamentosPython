# 1 - Listando valores de 0 a 10 que sejam menores do que 4

"""
Utilizando o for:
for i in range(10):
    if i < 4:
        print(i)s
"""

#Uma única estrutura dentro de uma lista, que retorne uma lista também 
#Imprima o i, onde o i será uma iteração de 10 números
listNumbers = [i for i in range(10) if i < 4 ]
print(listNumbers)

moviesList = ["Titanic", "The God Father", "Frozen", "Carrosel"]

#Filtrando - filmes que contenham a letra 'e', ele retorna apenas os filmes que contém.
moviesE = [movie for movie in moviesList if 'e' in movie.lower()]
print(moviesE)

#Filmes assistidos
moviesAssistidos = [movie for movie in moviesList if movie != "Carrosel"]
print(moviesAssistidos)

#Encontrando um filme pelo nome 
while True:
    searchName = input("Digite  um filme para buscar na lista (ou sair para encerrar): \n")
    if searchName.lower() == "sair":
        print("Programa encerrado")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme encontrado: {searchName}!")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme encontrado!")