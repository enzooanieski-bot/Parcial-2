# conversao_tempo_completa.py

def converter_para_horas(valor, tipo):
    if tipo == 1:  # segundos
        return valor / 3600
    elif tipo == 2:  # minutos
        return valor / 60
    elif tipo == 3:  # horas
        return valor
    else:
        return None


def main():
    print("=== Conversão de Tempo ===")
    print("Escolha o tipo de entrada:")
    print("1 - Segundos")
    print("2 - Minutos")
    print("3 - Horas")

    tipo = int(input("Digite a opção (1/2/3): "))
    valor = float(input("Digite o valor: "))

    horas = converter_para_horas(valor, tipo)

    if horas is None:
        print("Opção inválida!")
        return

    minutos = horas * 60
    segundos = minutos * 60

    print(f"\nHoras: {horas:.2f}")
    print(f"Minutos: {minutos:.2f}")
    print(f"Segundos: {segundos:.2f}")


if __name__ == "__main__":
    main()
