num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

#Operadores aritméticos 

#soma +
soma = num1 + num2

#subtração -
sub = num1 - num2

#divisão /
div = num1 / num2
#Divisão com resto %
mod = num1 % num2

#Multiplicação *
mult = num1 * num2

#Exponenciação **
exp = num1 ** num2

print(f"soma: {soma}\n"
      f"Subtração: {sub}\n"
      f"Resto: {mod}\n"
      f"Potência do {num1} pelo {num2} é de: {exp}")

#Operadores de comparação

#Verifica se um número e maior que outro, no final retorna com TRUE or FALSE
bigger = num1 > num2
smaller = num1 < num2
#Igualdade 
equal = num1 == num2
#Diferença
different = num1 != num2
#maior ou igual 
biggerEqual = num1 >= num2
#menor ou igual 
smallerEqual = num1 <= num2

#Atribuição
num2 += 1 #adiciona mais um, se for menos trocar sinal

print(f"É maior ou menor: {bigger}\n")