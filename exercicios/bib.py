def cadastra_jogo(lista):
    print("Cadastro do jogo: ")
    tit = input("Título do jogo: ")
    lista.append(tit)
    gen = input("Gênero do jogo: ")
    lista.append(gen)
    preco = float(input("Preço do jogo: "))
    lista.append(preco)
    plat = input("Plataforma: ")
    lista.append(plat)
    fx_eta = int(input("Faixa etária: "))
    lista.append(fx_eta)


def consulta_genero(lista, gen):
    i = 0
    while i < len(lista):
        if lista[i+1] == gen:
            imprime(lista, i)
        i = i + 5

def imprime(lista, pos):
    print("Tit: ", lista[pos])
    print("Gen: ", lista[pos+1]," preco:", lista[pos+2])
    print("Plat: ", lista[pos+3], " - fx eta: ", lista[pos+4])

def consulta_valor(lista, ini, fim):
    i = 0 
    while i < len(lista):
        if ini <= lista[i+2] and lista[i+2] <= fim:
            imprime(lista, i)
        i = i + 5

def altera_jogo(lista, titulo):
    i = 0
    while lista[i] != titulo and i < len(lista):
        i = i + 5
    
    if i >= len(lista):
        print(titulo, "não encotnrado")
    else:
        tit = input(f"Titulo ({lista[i]}): ")
        if tit != "":
            lista[i] = tit
        gen = input(f"Gênero ({lista[i+1]}): ")
        if gen != "":
            lista[i+1] = gen

        prc = input(f"Preço ({lista[i+2]}): ")
        if prc != "":
            lista[i+2] = float(prc)

        plat = input(f"Plataforma ({lista[i+3]}): ")
        if plat != "":
            lista[i+3] = plat

        fx_eta = input(f"Fx etaria ({lista[i+4]}): ")
        if fx_eta != "":
            lista[i+4] = fx_eta

