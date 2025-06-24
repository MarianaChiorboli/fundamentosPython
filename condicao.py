"""
#Obs: ctrl, ponto e vírgula comenta tudo

# Infos sobre filmes 

name = input("Digite o nome do filme: \n")
yearRelease = int(input("Digite o ano de lançamento: \n"))
rating = float(input("Digite a nota de avaliação: \n"))

#Verifica se o filme é recomendado
# Primeira condição se rating tem uma nota maior do que 8, and (operador lógico E), Se tanto o critério 1 e 2 forem verdadeiros, irá cair na primeira condição 
# Caso apenas 1 seja verdadeiro, ele automaticamente cai no else 

if rating > 8.0 and yearRelease > 2015:
    print(f"O filme {name} é excelente! \n")
else: 
    print(f"O filme {name} não é recomendado")
"""

#Elif 
num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
operation = input("Digite a operação a ser realizada: ( + - * / ) \n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num1 != 0:
        result = num1 / num2
    else: 
        print("Erro, divisão por 0!")
        result = 0
else:
    print("Operação inválida!")
    result = 0

print(f"Essa é a resposta da operação: {result}")
