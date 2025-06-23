#Usa chave, é um pouco paecido com o dicionário 
filmeSet = { "Branca de Neve", "Cinderela", "Frozen",
              "Bela Adormecida", "Interstellar" }

#Funções
# 1 - Buscar o tamanho do set - temos a função len de length(tamanho)
print(len(filmeSet))

# 2 - Valor True e 1, são considerados o mesmo valor
exampleSet = {"Inception", True, 1, 8.7}
print(exampleSet) # Valor true e 1, são retornados como o mesmo valor 

# 3- podemos adicionar um item de outro set
filmeSet.update(exampleSet)
print(filmeSet)

# 4 - Remover um item no set
filmeSet.remove(True)
filmeSet.remove(8.7)
print(filmeSet)