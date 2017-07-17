from operacoes import Operacoes


def main():
    num1 = input("Informe um número: ")
    num2 = input("Informe outro número: ")
    op = input("""Informe o nº da operação:
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão

    Opção: """)
    operacoes = Operacoes(num1, num2)
    if op == "1":
        print("O resultado é: " + str(operacoes.somar()))
    elif op == "2":
        print("O resultado é: " + str(operacoes.subtrair()))
    elif op == "3":
        print("O resultado é: " + str(operacoes.multiplicar()))
    elif op == "4":
        print("O resultado é: " + str(operacoes.dividir()))


if __name__ == "__main__":
    main()
