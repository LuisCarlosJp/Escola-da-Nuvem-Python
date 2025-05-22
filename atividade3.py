
def atividades(numero):
    match numero:
        case 1:
            try:
                idade = int(input("Insira sua idade: "))
                if idade < 0:
                    print("Insira uma idade válida (não negativa).")
                elif 0 <= idade <= 12:
                    print("Você é classificado como uma criança")
                elif 13 <= idade <= 17:
                    print("Você é classificado como um adolescente")
                elif 18 <= idade <= 59:
                    print("Você é classificado como um adulto")
                else:
                    print("Você é classificado como idoso")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número inteiro para a idade.")
        
        case 2:
            try:
                peso = float(input("Digite seu peso (kg): "))
                altura = float(input("Digite sua altura (m): "))

                imc = peso / (altura ** 2)

                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                elif imc < 25:
                    classificacao = "Peso normal"
                elif imc < 30:
                    classificacao = "Sobrepeso"
                else:
                    classificacao = "Obeso"

                print(f"\nSeu IMC é: {imc:.2f}")
                print(f"Classificação: {classificacao}")

            except ValueError:
                print("Entrada inválida! Certifique-se de digitar números corretamente.")

        case 3:
            try:
                temperatura= float(input("Insira a temperatura: "))
            except ValueError:
                print("Entrada inválida! Digite um número para a temperatura.")
                return
            origem = input("Informe a unidade de origem (Celsius, Fahrenheit e Kelvin): ").strip().title()
            destino = input("Informe a unidade de destino (Celsius, Fahrenheit e Kelvin): ").strip().title()

            unidades_validas = ["Celsius", "Fahrenheit", "Kelvin"]
            if origem not in unidades_validas or destino not in unidades_validas:
                print("Unidade inválida. Por favor, escolha entre Celsius, Fahrenheit e Kelvin.")
                return

            if origem == destino:
                resultado= temperatura
            elif origem == "Celsius" and destino =="Fahrenheit":
                resultado= temperatura*(9/5)+32
            elif origem == "Fahrenheit" and destino =="Celsius":
                resultado= (temperatura-32)*(5/9)
            elif origem == "Celsius" and destino =="Kelvin":
                resultado= temperatura + 273.15
            elif origem == "Kelvin" and destino =="Celsius":
                resultado= temperatura - 273.15
            elif origem == "Fahrenheit" and destino =="Kelvin":
                resultado= ((5/9)*(temperatura-32))+ 273.15
            elif origem == "Kelvin" and destino =="Fahrenheit":
                resultado= ((9/5)*(temperatura-273.15))+ 32

            print(f"\nA temperatura convertida é: {resultado: .2f} {destino}")

        case 4:
            try:
                ano = int(input("Digite um ano: "))
            except ValueError:
                print("Entrada inválida! Digite um número inteiro para o ano.")
                return

            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                print(f"{ano} é um ano bissexto.")
            else:
                print(f"{ano} não é um ano bissexto.")
        case 5:
            print("Saindo do programa...")
            return True
        
while True:
    print("\nEscolha uma opção:")
    print("1 - Classificador de Idade")
    print("2 - Calculadora de IMC")
    print("3 - Conversor de Temperatura")
    print("4 - Verificador de Ano Bissexto")
    print("5 - Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao.isdigit():
        if atividades(int(opcao)):
            break
    else:
        print("Opção inválida. Digite um número válido.")

