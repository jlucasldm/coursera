# Você conhece o jogo do NIM? Nesse jogo, n peças são 
# inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores 
# jogam alternadamente, retirando pelo menos 1 e no máximo m 
# peças cada um. Quem tirar as últimas peças possíveis ganha 
# o jogo.

# Existe uma estratégia para ganhar o jogo que é muito simples: 
# ela consiste em deixar sempre múltiplos de(m+1) peças ao 
# jogador oponente.

# Sejam n o número de peças inicial e m o número máximo de 
# peças que é possível retirar em uma rodada. Para garantir 
# que o computador ganhe sempre, é preciso considerar os dois 
# cenários possíveis para o início do jogo:

# - Se n é múltiplo de(m+1), o computador deve ser "generoso" 
# e convidar o jogador a iniciar a partida com a frase "Você 
# começa"
# - Caso contrário, o computador toma a inciativa de começar o 
# jogo, declarando "Computador começa"

# Uma vez iniciado o jogo, a estratégia do computador para 
# ganhar consiste em deixar sempre um número de peças que seja 
# múltiplo de(m+1) ao jogador. Caso isso não seja possível, 
# deverá tirar o número máximo de peças possíveis.

# Seu trabalho, então, será implementar o Jogo e fazer com que 
# o computador se utilize da estratégia vencedora.

def computador_escolhe_jogada(n, m):
    # Existe uma estratégia para ganhar o jogo que é muito simples: 
    # ela consiste em deixar sempre múltiplos de(m+1) peças ao 
    # jogador oponente.
    it = 0
    while it < n:
        if it%(m+1) == 0:
            maior = it 
        it += 1

    if n-maior > m:
        entrada = m
    else:
        entrada = n-maior

    if entrada == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", entrada, "peças.")

    if n-entrada == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")
    elif n-entrada != 0:
        print("Agora restam", n-entrada," peças no tabuleiro.\n")

    return entrada
    # devolve um inteiro correspondente à próxima jogada do 
    # computador de acordo com a estratégia vencedora

def usuario_escolhe_jogada(n, m):
    entrada = int(input("Quantas peças você vai tirar? "))
    while entrada > m or entrada > n or entrada <= 0:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        entrada = int(input("Quantas peças você vai tirar? "))
    if entrada == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou", entrada, "peças.")

    if n-entrada == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")
    elif n-entrada != 0:
        print("Agora restam", n-entrada," peças no tabuleiro.\n")

    return entrada
    # solicita que o jogador informe sua jogada e verifica se 
    # o valor informado é válido. Se o valor informado for 
    # válido, a função deve devolvê-lo; caso contrário, deve 
    # solicitar novamente ao usuário que informe uma jogada 
    # válida

def partida():
    n = int(input("Quantas peças? ")) 
    m = int(input("Limite de peças por jogada? "))
    
    while m<=0 or n<=0:
        print("\nOops! Entrada inválida! Tente de novo.\n")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

    if n%(m+1) == 0:
        print("\nVoce começa!\n")
        player = 1 # usuario
    else:
        print("\nComputador começa!\n")
        player = 0 # computador

    if player == 1:
        while n>0:
            rem = usuario_escolhe_jogada(n,m)
            n -= rem
            if n <= 0:
                print("Fim do jogo! Você ganhou!\n")
                return 0

            rem = computador_escolhe_jogada(n,m)
            n-=rem
            if n <= 0:
                print("Fim do jogo! O computador ganhou!\n")
                return 1

    if player == 0:
        while n > 0:
            rem = computador_escolhe_jogada(n, m)
            n -= rem
            if n <= 0:
                print("Fim do jogo! O computador ganhou!\n")
                return 1

            rem = usuario_escolhe_jogada(n, m)
            n -= rem
            if n <= 0:
                print("Fim do jogo! Você ganhou!\n")
                return 0

    # e inicia o jogo, alternando entre jogadas do computador 
    # e do usuário (ou seja, chamadas às duas funções 
    # anteriores). A escolha da jogada inicial deve ser feita 
    # em função da estratégia vencedora, como dito 
    # anteriormente. A cada jogada, deve ser impresso na tela 
    # o estado atual do jogo, ou seja, quantas peças foram 
    # removidas na última jogada e quantas restam na mesa. 
    # Quando a última peça é removida, essa função imprime na 
    # tela a mensagem "O computador ganhou!" ou "Você ganhou!" 
    # conforme o caso

def campeonato():
    it = 1
    computador = 0
    humano = 0

    while it <= 3:
        print("**** Rodada", it, "****\n")
        placar = partida()
        if placar == 1:
            computador += 1
        else:
            humano += 1
        it+=1

    print("**** Final do campeonato! ****")
    print("\nPlacar: Você", humano, "X", computador, "Computador\n")
    # uma vez que a função partida esteja funcionando, você 
    # deverá criar uma outra função chamada campeonato. Essa 
    # nova função deve realizar três partidas seguidas do jogo 
    # e, ao final, mostrar o placar dessas três partidas e 
    # indicar o vencedor do campeonato. O placar deve ser 
    # impresso na forma
    # Placar: Você ??? X ??? Computador

while 1 ==1:
    selec = input("Bem-vindo ao jogo do NIM! Escolha: \n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
    if int(selec) == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()
    elif int(selec) == 2:
        print("\nVoce escolheu um campeonato!\n")
        campeonato()
    else:
        quit()
