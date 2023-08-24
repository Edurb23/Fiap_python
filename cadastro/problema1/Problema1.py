def contar_letras(string):
    # Criar um dicionário para armazenar a contagem de letras
    contagem = {}

    # Iterar sobre cada caractere na string
    for caractere in string:
        if caractere.isalpha():  # Verificar se o caractere é uma letra
            caractere = caractere.lower()  # Converter para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
            if caractere in contagem:
                contagem[caractere] += 1
            else:
                contagem[caractere] = 1

    return contagem

# Solicitar ao usuário que insira uma string
entrada = input("Digite uma string: ")

# Chamar a função para contar as letras na string
resultado = contar_letras(entrada)

# Exibir a contagem de ocorrências de cada letra
for letra, contagem in resultado.items():
    print(f"A letra '{letra}' apareceu {contagem} vez(es)")