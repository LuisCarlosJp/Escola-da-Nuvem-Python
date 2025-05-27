#Função que calcula idade ade uma pessoas em dias, baseado no ano de nascimento
from datetime import date
def calcula_idade_em_dias(ano_nascimento):
    data_atual= date.today()
    date_nascimento= date(ano_nascimento, 1, 1)
    diferenca = data_atual - date_nascimento
    return diferenca.days

print(f"Sua idade em dias: {calcula_idade_em_dias(y := int(input("Qual é seu ano de nascimento? ")))}")


#Crie um função que calcule a gorjeta a ser deixada em um restaurante, baseado no valor total da conta e na porcentagem de gorgeta desejada
def Gorjeta_Calculo (valor_compra, percentual_gorjeta):
    return valor_compra * (percentual_gorjeta/100)

print(f"O valor da gorjeta é de: {(resultado:= Gorjeta_Calculo(compra := float(input("Qual valor total da compra: ")),gorjeta := float(input("% da gorjeta: "))) ):.2f}")


#Crie uma função  que verifique se uma palavra ou frase é palindrome
def is_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]

print("É palíndromo!" if is_palindromo(word:=input("Digite uma palavra ou frase: ")) else "Não é palíndromo.")



