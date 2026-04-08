print('Converções de tempo')
# mensagem inicial sobre oque o programa faz

def converter_para_horas(valor, tipo):
# define uma função chamada converter_para_horas: 'valor' = número digitado  'tipo' = tipo de unidade (segundos, minutos ou horas)

    if tipo == 1:  # segundos
        return valor / 3600
# se o valor estiver em segundos divide por 3600 para transformar em horas (1 hora = 3600 segundos)

    elif tipo == 2:  # minutos
        return valor / 60
# se estiver em minutos divide por 60 para converter em horas

    elif tipo == 3:  # horas
        return valor
# se já estiver em horas repete o valor

    else:
        return None
# se o usuário digitar uma opção inválida retorna None (valor nulo)

def main():
# Define a função principal do programa.
    print("=== Conversão de Tempo ===")
    print("Escolha o tipo de entrada:")
    print("1 - Segundos")
    print("2 - Minutos")
    print("3 - Horas")
# mostra o título e as opções que o usuário pode escolher

    tipo = int(input("Digite a opção (1/2/3): "))
    valor = float(input("Digite o valor: "))
# o usuário escolhe a transformação q ele deseja fazer e o valor

    horas = converter_para_horas(valor, tipo)
# converte tudo para horas e guarda o resultado na variável horas

    if horas is None:
        print("Opção inválida!")
        return
# verifica se a conversão falhou (opção inválida) e mostra erro e encerra a função com return

    minutos = horas * 60
    segundos = minutos * 60
# converte horas pra minutos e minutos pra segundos multiplicando o valor por 60

    print(f"\nHoras: {horas:.2f}")
    print(f"Minutos: {minutos:.2f}")
    print(f"Segundos: {segundos:.2f}")
# mostra horas com 2 casas decimais, minutos e segundos

if __name__ == "__main__":
    main()
# O main só será executado se o arquivo for rodado diretamente

print('Bons estudo!')
# mensagem final
