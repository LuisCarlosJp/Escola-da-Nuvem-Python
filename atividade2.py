
def atividades(numero):
    match numero:
        case 1:
            valor_em_reais= float(input("Insira o valor em reais: R$"))
            taxa_em_dolar= 5.20
            taxa_em_euro= 6.15

            valor_em_dolares=valor_em_reais*taxa_em_dolar
            valor_em_euros=valor_em_reais*taxa_em_euro

            print(f"Valor em dólares: ${valor_em_dolares: .2f}")
            print(f"Valor em euros: €{valor_em_euros: .2f}")
        
        case 2:
            nome_produto= input("Insira o nome do produto: ")
            preco_original= float(input("Insira o Preço original: "))
            desconto=input("Insira a porcentagem de desconto (ex: 10%): ")

            desconto_percentual = float(desconto.replace("%", "").strip())
            valor_desconto = preco_original * (desconto_percentual / 100)
            preco_final = preco_original - valor_desconto

            print(f"\nProduto: {nome_produto}")
            print(f"Preço original: R$ {preco_original:.2f}")
            print(f"Desconto aplicado ({desconto_percentual:.2f}%): R$ {valor_desconto:.2f}")
            print(f"Preço final: R$ {preco_final:.2f}")
        
        case 3:
            nota1= 7.5
            nota2= 8.0
            nota3= 6.5

            media= (nota1+nota2+nota3)/3

            print(f"Nota 1: {nota1:.2f}")
            print(f"Nota 2: {nota2:.2f}")
            print(f"Nota 3: {nota3:.2f}")
            print(f"Média final: {media:.2f}")
        
        case 4:
            distancia_percorrida = 300 
            combustivel_gasto= 25
            consumo_medio= distancia_percorrida/combustivel_gasto

            print(f"Distância percorrida: {distancia_percorrida: .2f}")
            print(f"Combustível gasto: {combustivel_gasto: .2f}")
            print(f"Consumo médio: {consumo_medio: .2f}km/l")
        case 5:
            print("Saindo do programa...")
            return True
        
while True:
    print("\nEscolha uma opção:")
    print("1 - Conversor de Moeda")
    print("2 - Calculadora de Desconto")
    print("3 - Calculadora de Média Escolar")
    print("4 - Calculadora de Consumo de Combustível")
    print("5 - Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao.isdigit():
        if atividades(int(opcao)):
            break
    else:
        print("Opção inválida. Digite um número válido.")

