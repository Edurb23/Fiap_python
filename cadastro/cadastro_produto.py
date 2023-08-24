import datetime

def menu():
    print("Escolha uma opção")
    print("1 - cadastra")
    print("2 - altera")
    print("3 - consulta")
    print("4 - apaga")
    print("5 - sair")
    return int (input('escolha: '))

def cadastra():
    p = {}
    aux = input('descricao do produto: ')
    p['descricao'] = aux

    aux = input("fabricante: ")
    p['fabricante'] = aux

    aux = input('peso: ')
    p['peso'] = aux

    aux = input("validade: ")
    data = aux.split("/")
    
    p['validade'] = datetime.datetime(int(data[0]), int(data[1]), int(data[2]))

    aux = int(input("quantidade: "))
    p['quantidade'] = aux
    
    return p

def altera(prod):
    aux = input (f"descricao ({prod['descricao']}):")
    if len(aux) != 0:
        prod['descricao'] = aux

    aux = input(f'fabricante ({prod["fabricante"]}):')        
    if len(aux) != 0:
        prod['fabricante']= aux

    aux = input(f'peso ({prod["peso"]}):')            
    if len(aux) != 0:
        prod['peso']= aux

    aux = input(f'validade ({prod["validade"]}):')        
    if len(aux) != 0:
        dados = aux.split("/")
        data = datetime.datetime(int(dados[0]), int(dados[1]), int(dados[2]))
        prod['validade'] = data
        
    aux = input(f"quantidade ({prod['quantidade']}): ")        
    if len(aux) != 0:
        prod['quantidade'] = int(aux)


#programa principal
produtos = []

escolha = menu()
while escolha != 5:
    
    if escolha == 1:
        prod = cadastra()
        produtos.append(prod)

    elif escolha == 2:
        ind = int(input ('posição do produto a ser atualizado'))
        prod = produtos[ind]
        altera(prod)

    elif escolha == 3: #consulta
        desc = input('descrição do produto: ')
        for info in produtos:
            if info['descricao'] == desc:
                print(info)

    elif escolha == 4: #apaga
        desc = input('descrição do produto: ')
        i = 0
        for i in range(len(produtos)):
            prod = produtos[i]
            if prod['descricao'] == desc:
                produtos.pop(i)
                break

    else:
        print("Escolha invalida!!")
    
    escolha = menu()

