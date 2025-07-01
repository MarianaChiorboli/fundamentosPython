"""
Fatorial de um número:
1 -> 1*1
2 -> 2*1
3 -> 3*2*1
"""

# 1 - Fatorial de um número
def factorial (num):
    if num == 1:  # caso base
        return 1
    else:
        return(num * factorial(num - 1)) # chamada recursiva - ela se chama novamente porém com outro valor
number = int(input("Digite um número: "))
print(f"Fatorial de {number} é {factorial(number)}")


# 2 - soma total de um número
def soma_num(num):
    if num == 1:
        return 1
    else:
        return (num + soma_num(num -1))
    
num = int(input("Digite um número para soma: "))
print(f"Soma dos números = {num}")
