print('Bem vindo ao programa que verifica se um número é impar ou par')   
# Mostra a primeira mensagem explicando o que o programa faz.

n = int(input("Digite um número: "))
# o imput serve para o usuário digitar um valor e int converte esse texto para um número inteiro

if n % 2 == 0:
    print(f"O número {n} é par.")
else:
    print(f"O número {n} é ímpar.")
# n % 2 calcula o resto da divisão de n por 2 Se o resto for 0, significa que o número é par então o if verifica se o resto é igual a zero.
# se o resto da divisão por 2 for 0 o número é par, se não o número é impar

print( 'Bons estudos! Até mais.' )
# mensagem final
