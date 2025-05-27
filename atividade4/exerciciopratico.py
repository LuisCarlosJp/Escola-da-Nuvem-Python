while True:
    try:
        numero1 = float(input("\nInsira o primeiro número: "))
        numero2 = float(input("Insira o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ").strip()

        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        else:
            print("Erro: Operação inválida. Tente novamente.")
            continue

        print(f"\nResultado: {resultado:.2f}")

        sair = input("\nDeseja finalizar (Y/N)? ").strip().upper()
        if sair == "Y":
            print("Programa finalizado.")
            break

    except ValueError:
        print("Erro: Insira um valor numérico válido.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
