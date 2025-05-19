# 1 - Programa de Saudação

print("Hello World")

# 2 - Calculadora de Soma

n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
soma = n1 + n2
print(f"A soma de {n1} e {n2} é igual a {soma}")

# 3 - Calculadora de Volume

print("Volume do paralelepipedo")
base = float(input("Insira a base(em metros): "))
altura = float(input("Insira a altura(em metros): "))
largura = float(input("Insira a largura(em metros): "))
volume = base * altura * largura
print(f"Volume do paralelepipedo é : {volume}m³")

# 4 - Calculadora de Preço Total

quantidade = int(input("Digite a quantidade de itens: "))
preco_unitario = float(input("Digite o preço unitário (R$): "))
preco_total = quantidade * preco_unitario
print(f"O preço total é R$ {preco_total:.2f}")

