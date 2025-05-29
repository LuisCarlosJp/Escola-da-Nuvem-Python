#Crie um programa que gera uma senha aleatória com o modulo random, utilizando caracteres especiais, possiblitando o 
# usuário a informar a quantidade de caracteres desse senha aleatória
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite a quantidade de caracteres da senha: "))
senha_gerada = gerar_senha(tamanho_senha)
print(f"Senha gerada: {senha_gerada}")

#Crie um programa que gera um perfil de usuário aleatório usando o API 'Random User Generator'.
#O programa deve exibir o nome, email e país do usuário gerado.
import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]
        
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao obter os dados da API.")

gerar_usuario()


#Desenvolva um programa  que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
# O programa deve exibir o logradouro, bairro, cidade e estado correspondes ao CEP consultado.
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP inválido. Tente novamente.")
        else:
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")
    else:
        print("Erro ao acessar a API.")


cep_usuario = input("Digite um CEP para consulta: ")
consultar_cep(cep_usuario)

#Crie um programa que consulte a cotação atual de um moeda estrangeira em relação ao Real Brasileiro
#O usuáro deve informar o código da moeda desejada (ex: USD, EUR, GBP) e o program deve exibir o valor
#atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da 
#AwesomwAPI para obter os dados da cotação
import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        chave_moeda = f"{moeda}BRL"
        
        if chave_moeda in dados:
            cotacao = dados[chave_moeda]
            print(f"Moeda: {cotacao['name']}")
            print(f"Valor atual: R$ {cotacao['bid']}")
            print(f"Valor máximo: R$ {cotacao['high']}")
            print(f"Valor mínimo: R$ {cotacao['low']}")
            print(f"Última atualização: {cotacao['create_date']}")
        else:
            print("Código da moeda inválido. Tente novamente.")
    else:
        print("Erro ao acessar a API.")

# Solicita o código da moeda ao usuário
moeda_usuario = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda_usuario)
