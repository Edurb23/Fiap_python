import bib

dados = []
opcao = 0
while opcao != 5:
    print("1) cadastro do jogo")
    print("2) consulta por gênero")
    print("3) consulta por valor")
    print("4) altera jogo")
    print("5) sair")
    opcao = int(input("escolha: "))
    if opcao == 1:
        #print("coleto as informacoes do jogo e armazeno na lista")
        bib.cadastra_jogo(dados)

    elif opcao == 2:
        #print("usuário informa um gênero, percorro a lista com os jogos")
        #print("mostrando aqueles que possuem o mesmo genero")    
        genero = input("Gênero: ")
        bib.consulta_genero(dados, genero)

    elif opcao == 3:
        #print("usuário informa valor ini e fim e mostro os jogos ...")
        ini = float(input("valor inicial: "))
        fim = float(input("valor final: "))
        bib.consulta_valor(dados, ini, fim)

    elif opcao == 4:
        #print("usuario informa o titulo e após isso, eu edito todas os dado")
        titulo = input("informe o titulo: ")
        bib.altera_jogo(dados, titulo)
    elif opcao == 5:
        print("saindo do sistema!")    
