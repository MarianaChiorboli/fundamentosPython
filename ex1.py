"""
Escreva um programa que le dois nomes e retorne uma String formatada no formato "Ultimo nome", "primeiro nome"

nome = "Mariana Chiorboli"
partes = nome.split()

print(partes[1], partes[0])


primeiroNome = input("Digite seu nome: ")
segundoNome = input("Digite seu sobrenome: ")

nomeFormatado = f"{segundoNome} {primeiroNome}"

print(nomeFormatado)

"""

"""
Exercício 2 - inverta a ordem das palavras em uma String fornecida:

texto = "primeiro e segundo"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])

print(textoInvertido)

"""
#3 - verifique se uma STring fornecida é palindromo(pode ser lida da mesma forma de trás para frente)

texto1 = "arara"
texto2 = "python"

texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

palindromo1 = texto1_format == texto1_format[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(f"{palindromo1}\n",
      f"{palindromo2}\n")