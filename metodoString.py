movieName = "Top Gun"

movieDescription = '''
    Top Gun é um filme de aviação e aventura, muito consagrado na insdústria
'''

#deixa tudo maiusculo o título
print(movieName.upper())
#deixa tudo minusculo
print(movieName.lower())
#primeira letra em maiuscula 
print(movieName.capitalize())
#mesmo objetivo de capitalize
print(movieName.title())
#retona string centralizada com caractere de preenchimento
print(movieName.center(10, '-'))
#Procurar caracter ou conta caracteres
print(movieName.find("u"))
#Substituir palavra por outra
print(movieName.replace("Top", "Matrix"))
#quebrar string em partes 
print(movieDescription.split(','))