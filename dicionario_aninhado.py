#Para deixar mais legível, é necessário usar um módulo 
import pprint #Ajuda visualizar melhor o dicionário 

filmesDict = {
    #Ajuda a mapear outros filmes aqui dentro
   "inception": {
       #Dentro desse dicionário tenho as propriedades do meu filme
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["sci-fi", "ACtion", "Thriller"]
   }, 

   "Interstellar": {
       "yearRelease": 2015,
        "imdbRating": 9.5,
        "genre": ["sci-fi", "Drama"]
   }, 

   "Lilo and Stitch - Live Action": {
       "yearRelease": 2025,
        "imdbRating": 9.0,
        "genre": ["fiction", "cartoon"]
   }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesDict)

# 1 - Buscar infos dentro de um dicionário aninhado
print(filmesDict["Interstellar"]["genre"])

# 2 - Adicionar um novo item 
filmesDict["inception"]["Director"] = "Mari Chiorboli"
print(filmesDict["inception"])

# 3 - Excluir um dicionário
del filmesDict["Interstellar"]
pp.pprint(filmesDict)