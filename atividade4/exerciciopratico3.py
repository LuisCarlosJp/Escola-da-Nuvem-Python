import string
import getpass

def verifica_senha():
    while True:
        #senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        senha = getpass.getpass("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == 'sair':
            print("Programa encerrado")
            break

        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres")
        
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um número")
            continue
        
        if not any(caractere.isupper() for caractere in senha):
            print("Senha fraca: deve conter pelo menos uma letra maiúscula.")
            continue

        if not any(caractere.islower() for caractere in senha):
            print("Senha fraca: deve conter pelo menos uma letra minúscula.")
            continue

        if not any(caractere in string.punctuation for caractere in senha):
            print("Senha fraca: deve conter pelo menos um caractere especial.")
            continue

        print("Senha forte!")
        break

verifica_senha()