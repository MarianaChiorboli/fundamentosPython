name = input("Digite o nome do filme: \n")
yearLaunch = input("Digite o ano de lançamento do filme: \n")
noteMovie = input("Informe a nota: \n")

#1 alternativa de concatenação
print ("Dados do filme: " )
print("=================================")
"""
print("Nome do filme: ", name)
print("Ano de lançamento: ", yearLaunch)
print("Nota avaliada do filme: ", noteMovie)

"""

#2 alternativa - print tudo junto
"""
print("Nome do Filme: ", name, "\nAno de lançamento: ", yearLaunch, "\nNota Avaliada do filme: ", noteMovie)
"""

#3 alternativa - f String 
print(f"NOme do filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota avaliada: {noteMovie}"
      )
