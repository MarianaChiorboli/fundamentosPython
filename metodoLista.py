filmesList = ["Branca de Neve", "Cinderela", "Frozen",
              "Bela Adormecida", "Interstellar"]

# 1 - verificar o tamanho da lista 
print(len(filmesList))#len de length, percorre o tamanho 

# 2 - Recuperar um item da lista pelo nome
print(filmesList.index("Interstellar"))#index - busca o código 4

# 3 - podemos adicionar um item no final da lista 
filmesList.append("Lilo and stitch")
print(filmesList)

# 4 - ordenar a lista 
filmesList.sort()
print(filmesList)

# 5 - copia os itens de uma lista para a outra 
filmsCopy = filmesList.copy()
filmsCopy.remove("Interstellar")
print(filmsCopy)

# 6 - remove todos os itens da lista
filmesList.clear()
print(filmesList)