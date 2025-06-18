#UTilizando o input(entrada de dado)
#Código sem converter o tipo de dado, ele identifica tudo como String
"""
name = input("Digite o nome do filme: \n")
yearLaunch = input("Digite o ano de lançamento do filme: \n")
noteMovie = input("Informe a nota: \n")

print (type(name))
print(type(yearLaunch))
print(type(noteMovie))
"""
#Tipo de dado convertido
name = input("Digite o nome do filme: \n")
yearLaunch = int(input("Digite o ano de lançamento do filme: \n"))
noteMovie = float(input("Informe a nota: \n"))

print (type(name))
print(type(yearLaunch))
print(type(noteMovie))