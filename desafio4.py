print('Calculadora simples')

operação = input("Digite a operação (+, -, *, /): ")
# o usuário pode escolher a opreração q deseja realizar. A escolha vai ficar salva na variavel operação

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
# input recebe o valor como texto e float converte para número decimal

if operação == "+":
    resultado = n1 + n2
elif operação == "-":
    resultado = n1 - n2
elif operação == "*":
    resultado = n1 * n2
elif operação == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"
# realiza o cálculo de acordo com a operação e os números escolhidos
# OBS: se o número 2 for 0 o resultado da divisão dará erro, pois nenhum número pode ser dividido por zero

print("Resultado:", resultado)
# mostra o resultado da operação

print( 'Até a próxima!' )
# mensagem final 
