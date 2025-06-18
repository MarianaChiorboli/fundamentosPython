#STring em python é case sensitive, ou seja, valores podem ser os mesmos porém com letras em maiscúlo e outro em minuscúlo

movieName = "Top Gun"
movieName2 = "top Gun"

print(movieName == movieName2)

#Descrição multilinha
movieDescription = '''
    Top Gun é um filme de aviação e aventura, muito consagrado na insdústria
'''

print(movieName)
#Multiplicação de Strings:
line = "="
print(line*50)
print(movieDescription)

#Procurar uma palavra dentro de um texto
print("top" in movieName)