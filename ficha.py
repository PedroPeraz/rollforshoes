#Dicionario = {'nome'= nome,'experiencia' = 0,'habilidades'= []}

jogadores = [{'Nome': 'asd','Experiencia': 0,'Habilidades': [{'Fazer qualquer coisa': 1},{'asd': 2},{'qwe': 3}]}]



def mostrar_jogadores():
    

while True:
    acao = input()

    if acao == '1':
        nome = input('Insira o nome do seu personagem: ')
        jogador = {'nome': nome,'experiencia': 0,'habilidades': [{'Fazer alguma coisa': 1}]}
        jogadores.append(jogador)

        mostrar_jogadores()

    if acao == '2':
        mostrar_jogadores()

        escolha = int(input('Digite o número do Jogador que gostaria de inserir experiência: '))
        a = jogadores[escolha-1]
        a['experiencia'] += 1

        mostrar_jogadores()

    if acao == '3':
        mostrar_jogadores()

        num_jogador = int(input('Digite o número do Jogador que gostaria de inserir habilidade: '))

        posicao = jogadores[num_jogador-1]
        posicao_interna = posicao['habilidades']
        
        habilidade = input('Insira o nome da habilidade: ')
        nivel = int(input('Insira o nível dessa variável: '))
        nova_habilidade = {habilidade: nivel}
        posicao_interna.append(nova_habilidade)

        mostrar_jogadores()

    if acao == '4':
        c = 0

        mostrar_jogadores()
        
        escolha = int(input('Digite o número do Jogador que gostaria de usar sua habilidade: '))
        posicao = jogadores[escolha-1]
        posicao_interna = posicao['habilidades']
        for x in posicao_interna:
            for i in x:
                c += 1
                print(f'{c} = [{x[i]}] {i}')

        num_habilidade = int(input('Digite o número correspondente a habilidade: '))
        habilidade_escolhida = posicao_interna[num_habilidade-1]
        lista_habilidade = list(habilidade_escolhida)
        chave_habilidade = lista_habilidade[0]
        dado_habilidade = habilidade_escolhida[chave_habilidade]
        
