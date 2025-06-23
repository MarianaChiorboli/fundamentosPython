#Além do valor temos a propriedade
filmeInception = {
    "Title" : "Inception",
    "yearRelease": 2010,
    "imdbRating": 8.8,
    #é possível passar mais de um genero com a estrutura lista, sendo possível passar dentro do dicionário 
    "genre": ["sci-fi", "ACtion", "Thriller"]
}
print(filmeInception)
print(len(filmeInception))

# 1 - Recuperar um elemento de um dicionário
print(filmeInception["genre"])
print(filmeInception.get("imdbRatting"))

# 2 - Buscar apenas as chaves do dicionário 
print(filmeInception.keys())

# 3 -  Buscar apenas os valores do dicionário 
print(filmeInception.values())

# 4 - Buscar itens do dicionário com chave e valor 
print(filmeInception.items())

# 5 - Adicionar itens no dicionário 
filmeInception["director"] = "Mariana Chiorboli"
print(filmeInception)

# 6 - Atualizar item no dicionário 
filmeInception.update({"imdbRating": 8.7})
print(filmeInception)

# 7 - remover um item de um dicionário
filmeInception.pop("director")
print(filmeInception)