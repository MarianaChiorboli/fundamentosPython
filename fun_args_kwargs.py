"""
Parametros 
*Args - utilizados para quando não temos certeza de quantos args queremos em uma função
- São passados como uma tupla
- Apenas usando o asterico *, já sendo chamdo o args

"""

# 1 - Soma de nums

def soma(*num): #Itens dentro de uma tupla
    soma_total = 0
    for n in num:
        soma_total += n

    print(f"Soma é: {soma_total}")

soma(5)
soma(8,9)

"""
Parametros
**Kwargs - Além dos valores são passados as respectivas chaves para cada argumento
- Argumentos são passados como um dicionário (tendo a chave e o valor)
"""

# 2 - Apresentação de cursos 
def presentation(**data): # data == a dicionário
    for key, value in data.items():
        print(f"{key} - {value}")
print("Listas de cursos: ")
presentation(name="Python", category="Backend", level = "Iniciante")