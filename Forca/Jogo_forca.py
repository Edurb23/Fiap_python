import dicionario

def cria_segredo(word):
    resp = ""
    i = 0
    while i < len(word):
        resp = resp + "_ "
        i = i + 1
    return resp

def update_segredo(word, c, secret):
    resp = ""
    i = 0
    while i < len(word):
        if word[i] == c:
            resp = resp + c + " "
        else:
            resp = resp + secret[2*i] + " "
        i = i + 1
    return resp



#palavra = dicionario.sorteio().upper()
palavra = "SOUTH DAKOTA".upper()
qtd_erros = 0
segredo = cria_segredo(palavra)

while qtd_erros < 6 and "_" in segredo:
    print(segredo)
    print("erros:", qtd_erros)
    
    letra = input("Informe uma letra: ")
    letra = letra.upper()

    if not letra in palavra:
        qtd_erros = qtd_erros + 1
    else:
        segredo = update_segredo(palavra, letra, segredo)    

if qtd_erros < 6:
    print("Parabéns, você encontrou", segredo)
else:    
    print("Você perdeu, a palavra era", palavra)
