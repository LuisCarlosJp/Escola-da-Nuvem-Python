import csv
import os

tempos = []

# Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. 
with open('logs_treinamento.csv','r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)
    for linha in leitor:
        modelo, tempo = linha
        tempos.append(int(tempo))

# Cálculo da média e do desvio padrão
media=sum(tempos)/len(tempos)
Xi=[(x-media)**2 for x in tempos]
desvio_padrao = (sum(Xi)/(len(tempos)-1))**0.5

print("                   ATIVIDADE 01               \n")
print(f'Tempo médio de execução: {media:.2f} segundos')
print(f'Desvio padrão: {desvio_padrao:.2f} segundos.\n')


#Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
print("                   ATIVIDADE 02               \n")
caminho_arquivo = 'pessoas.csv'
arquivo_existe = os.path.exists(caminho_arquivo)
with open(caminho_arquivo, 'a', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    
    # Se o arquivo não existe, escreve o cabeçalho
    if not arquivo_existe:
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
    
    # Adiciona uma nova linha de dados
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ").strip()
        if nome.lower() == 'sair':
            print("Encerrando...")
            break

        idade = int(input("Digite a idade: ").strip())
        cidade = input("Digite a cidade: ").strip()

        # Grava os dados no CSV
        escritor.writerow([nome, idade, cidade])
        print(f"{nome} foi adicionado ao arquivo.\n")

#Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
print("                   ATIVIDADE 03               \n")
with open('pessoas.csv','r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    print("---------------------------------------------")
    if arquivo_existe:
        for linha in leitor:
            Nome, Idade, Cidade = linha
            print(f"| {Nome:<10} | {Idade:^5} | {Cidade:<20} |")
    print("---------------------------------------------\n")
            

#Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
import json

caminho_arquivo = 'dados.json'
print("                   ATIVIDADE 04               \n")
# Tenta carregar dados existentes do arquivo
if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)
else:
    dados = []

# Adiciona novas pessoas via input
while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        print("Encerrando...")
        break

    idade = int(input("Digite a idade: ").strip())
    cidade = input("Digite a cidade: ").strip()

    novo_dado = {"nome": nome, "idade": idade, "cidade": cidade}
    dados.append(novo_dado)

# Escreve tudo no arquivo (sobrescreve o conteúdo)
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)

print(f'Dados salvos em {caminho_arquivo}')

# Lê e imprime o conteúdo do arquivo JSON
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
    dados_lidos = json.load(arquivo_json)

print(dados_lidos)