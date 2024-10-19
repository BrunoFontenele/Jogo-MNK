def eh_tabuleiro(arg):
        '''
        A função analisa se o argumento é um tabuleiro, ou seja, se é um tuplo de tuplos com tamanho válido de linhas e colunas,
        e responde com um booleano indicando se é ou não.
        Apenas permite tabuleiro com linhas e colunas entre 2 e 100 e
        posições (inteiros) entre -1 e 1.
        '''
        if type(arg) == tuple:
            if not (2<=len(arg)<=100):
                return False
            # 1o caso
            if type(arg[0]) == tuple:
                num_colunas = len(arg[0])
            else:
                return False
            # resto das linhas
            for i in range(len(arg)):
                if type(arg[i]) != tuple or len(arg[i]) != num_colunas:
                    return False
                if not (2<=len(arg[i])<=100):
                    return False
                for j in range(len(arg[i])):
                    if type(arg[i][j]) != int or not (-1<=arg[i][j]<=1):
                        return False
            return True
        else:
            return False


def eh_posicao(arg):
    '''
    A função verifica se recebe um argumento válido (um int)
    e se a posição está no intervalo permitido (entre 1 e 10000), utilizando um booleano para indicar isto.
    '''
    if type(arg) == int:
        if 1<=arg<=10000:
            return True
        else:
            return False
    else:
        return False    
    

def obtem_dimensao(tab):
    '''
    Recebe um argumento que é verificado se é válido pela função eh_tabuleiro e,
    em seguida, devolve a contagem de linhas pelo número de subtuplos no tuplo principal (len(tab))
    e de colunas pelas entradas do subtuplos (len(tab[0])).
    '''
    if eh_tabuleiro(tab):
        return (len(tab), len(tab[0])) #como sabemos que é tabuleiro, todas as linhas terão a mesma quantidade de colunas, assim sendo necessário contar apenas as entradas do primeiro subtuplos.
 

def obtem_valor(tab,pos):
    '''
    A função recebe um tabuleiro e uma posição, ambos válidos, e retorna a entrada nessa posição,
    sendo entre -1 ou 1.
    '''
    if eh_tabuleiro(tab) and eh_posicao(pos):
        pos = pos - 1
        contador = 0
        colunas = len(tab[0])
        if pos>=colunas:
            while pos>=colunas: 
                pos -= colunas #reduzindo até uma posição dentro do número de colunas
                contador +=1 #analisando qual linha queremos
            return tab[contador][pos]
        return tab[0][pos]

def obtem_coluna(tab, pos):
    '''
    A função recebe um tabuleiro e uma posição, ambos válidos, e 
    devolve um tuplo com todas as posições que formam a 
    coluna em que esta posição está contida.
    '''
    if eh_tabuleiro(tab) and eh_posicao(pos):
            dimensao = obtem_dimensao(tab)
            posicao_max = dimensao[0]*dimensao[1]
            num_colunas = len(tab[0])
            resultado = ()
            if pos>num_colunas:
                while pos>num_colunas:
                    pos -= num_colunas
                while pos <= posicao_max:
                    resultado += (pos,)
                    pos += num_colunas
                return resultado
            else:
                while pos <= posicao_max:
                    resultado += (pos,)
                    pos += num_colunas
                return resultado


def tab_para_pos(tab):
    '''
    Recebe um tabuleiro válido e retorna um tuplo com subtuplos
    contendo cada posição do tabuleiro em ordem crescente.
    '''
    if eh_tabuleiro(tab):
        contador = 1
        n = 1
        resultado = ()
        tuplo = ()
        num_colunas = len(tab[0])
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                tuplo += (contador,)
                if contador == num_colunas*n:
                    resultado += (tuplo,)
                    n += 1
                    tuplo = ()
                contador += 1
        return resultado
    
def obtem_linha(tab,pos):
    '''
    A função recebe um tabuleiro e uma posição, ambos válidos, e 
    devolve um tuplo com as posições contidas na linha em que essa posição
    se encontra.
    '''
    if eh_tabuleiro(tab) and eh_posicao(pos):
        posicoes = tab_para_pos(tab)
        for linha in range(len(posicoes)):
            for entrada in posicoes[linha]:
                if entrada == pos:
                    break
            if entrada == pos:
                    break
        return posicoes[linha]

def obtem_antidiagonal(tab,pos):
    '''
    A função recebe um tabuleiro e uma posição, ambos válidos, e retorna
    as posições correspondentes a antidiagonal (ascendente da esquerda para a direita) em que 
    a posição está contida.
    '''
    if eh_posicao(pos) and eh_tabuleiro(tab):
        posicoes = tab_para_pos(tab)
        linha_pos = obtem_linha(tab,pos)
        coluna_pos = obtem_coluna(tab,pos)
        num_linhas = len(tab) - 1
        num_colunas = len(tab[0]) - 1
        resultado = ()
        for coluna in range(len(linha_pos)): #iteramos a linha dessa posição para descobrir o índice da coluna em que está contida.
            if linha_pos[coluna] == pos:
                break
        for linha in range(len(coluna_pos)):  #iteramos a coluna dessa posição para descobrir o índice da linha em que está contida.
            if coluna_pos[linha] == pos:
                break
        while linha < num_linhas and coluna > 0: #vamos em direção ao começo da anticoluna, sabendo que a posição inicial estará na primeira coluna e não ultrapassará o número de linhas do tabuleiro.
            coluna -= 1
            linha += 1
        resultado += (posicoes[linha][coluna],) #guardamos a posição final
        while linha>0 and coluna<num_colunas: #vamos na direção contrária, aumentando as linhas e diminuindo as colunas, assim guardando as posições da antidiagonal.
            coluna += 1
            linha -= 1
            resultado += (posicoes[linha][coluna],)
        return resultado

def obtem_diagonais(tab,pos):
    '''
    A função recebe um tabuleiro e uma posição, ambos válidos, e retorna
    a diagonal (descendente da esquerda para a direita) e antidiagonal 
    (ascendente da esquerda para a direita) em que a posição está contida
    como subtuplos de um tuplo.
    '''
    if eh_posicao(pos) and eh_tabuleiro(tab):
        '''
        O processo dessa função é o mesmo da antidiagonal, apenas vamos diminuindo os índices
        das linhas e das colunas até chegar no começo da diagonal, assim percorrendo na ordem
        contrária em seguida.
        '''
        posicoes = tab_para_pos(tab)
        linha_pos = obtem_linha(tab,pos)
        coluna_pos = obtem_coluna(tab,pos)
        num_linhas = len(tab) - 1
        num_colunas = len(tab[0]) - 1
        resultado = ()
        for coluna in range(len(linha_pos)): 
            if linha_pos[coluna] == pos:
                break
        for linha in range(len(coluna_pos)):
            if coluna_pos[linha] == pos:
                break
        while coluna>0 and linha>0:
            coluna -= 1
            linha -= 1
        resultado += (posicoes[linha][coluna],)
        while coluna < num_colunas and linha < num_linhas:
            coluna += 1
            linha += 1
            resultado += (posicoes[linha][coluna],)
        return (resultado, obtem_antidiagonal(tab,pos))    

def tabuleiro_para_str(tab):
    '''
    A função recebe um tabuleiro válido, e devolve
    uma cadeia de caracteres que o representa de uma forma de mais fácil
    visualização.
    '''
    if eh_tabuleiro(tab):
        resultado = ""
        contador = 1
        contador2 = 0
        espaco = ((len(tab[0])-1) * "|   ") + "|" #assim sabemos quantos espaços vamos ter que dar
        for linha in tab:
            for entrada in linha:
                if entrada == 1: #mudamos 1 para X
                    resultado += "X"
                elif entrada == 0: #mudamos 0 para +
                    resultado += "+" 
                else:
                    resultado += "O" #mudamos -1 para O
                if contador != len(linha): #enquanto o contador for diferente do número de colunas (não chegou no fim da linha), adicionaremos espaçamento
                    resultado += "---"
                contador+=1
            contador2 += 1
            if contador2 != len(tab): #adicionamos espaçamento enquanto não chegarmos na última linha
                resultado += f"\n{espaco}\n" 
            contador = 1 #reiniciamos o contador para repetir o mesmo processo anterior
    return resultado

def eh_posicao_valida(tab, pos):
    '''
    A função recebe um tabuleiro e uma posição, ambos válidos, e devolve 
    um booleano (True ou False) indicando se a posição corresponde
    a uma posição da tabuleiro.
    '''
    if eh_tabuleiro(tab) and eh_posicao(pos):
        tab_pos = tab_para_pos(tab)
        for linha in tab_pos:
            if pos in linha: 
                return True
        return False
    else:
        raise ValueError("eh_posicao_valida: argumentos invalidos")
    
def eh_posicao_livre(tab, pos):
    '''
    A função recebe um tabuleiro e uma posição, ambos válidos, e devolve 
    um booleano (True ou False) indicando se a posição é livre, ou seja,
    não está ocupada por pedras.
    '''
    if eh_tabuleiro(tab) and eh_posicao(pos):
        if eh_posicao_valida(tab, pos):
            tab_pos = tab_para_pos(tab)
            for linha in range(len(tab_pos)):
                for entrada in range(len(tab_pos[linha])):
                    if tab_pos[linha][entrada] == pos: #percorremos o tuplo das posições até encontrar a pedida, assim guardando os índices de sua linha e coluna
                        break
                if tab_pos[linha][entrada] == pos:  
                    break
            if tab[linha][entrada] == 0: #verificamos se é uma posição livre no tabuleiro original
                return True
            else:
                return False
        else:
            raise ValueError('eh_posicao_livre: argumentos invalidos')
    else:
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    


def obtem_posicoes_livres(tab):
    '''
    A função recebe um tabuleiro válido e retorna um tuplo
    contendo todas as posições livres do tabuleiro ordenadas de forma
    crescente.
    '''
    if eh_tabuleiro(tab):
        resultado = ()
        tab_pos = tab_para_pos(tab)
        for linha in range(len(tab_pos)):
            for entrada in range(len(tab_pos[linha])):
                if eh_posicao_livre(tab, tab_pos[linha][entrada]): #verificamos quando o elemento do tuplo das posições é livre
                    resultado += (tab_pos[linha][entrada],)
        return resultado
    else:
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    
def obtem_posicoes_jogador(tab, jog):
    '''
    A função recebe um tabuleiro válido e um jogador (sendo 1 para os "X" e -1 para os "O") retorna um tuplo
    contendo todas as posições ocupadas por esse jogador ordenadas de forma crescente.
    '''
    if not (eh_tabuleiro(tab) and jog in (-1,1) and type(jog) == int):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    tab_pos = tab_para_pos(tab)
    resultado = ()
    for linha in range(len(tab)):
        for entrada in range(len(tab[linha])):
            if jog == 1 and tab[linha][entrada] == 1: #Verificamos quando aparece uma peça do jogador 1
                resultado += (tab_pos[linha][entrada],) #Colocamos o elemento de mesmo índice do tabuleiro das posições no resultado
            elif jog == -1 and tab[linha][entrada] == -1: #Mesmo processo anterior para o jogador -1
                resultado += (tab_pos[linha][entrada],)
    return resultado


def obtem_posicoes_adjacentes(tab, pos):
    if eh_tabuleiro(tab) and eh_posicao(pos):
        if eh_posicao_valida(tab,pos):
            '''
            A função recebe um tabuleiro e uma posição, ambos válidos, e devolve
            as posições adjacentes a posição recebida, sendo essas as que distanciam 1 dessa posição.
            '''
            tab_pos = tab_para_pos(tab)
            resultado = ()
            for linha in range(len(tab)):
                for coluna in range(len(tab[0])): #para descobrir em que linha e em que coluna a posição se encontra
                    if tab_pos[linha][coluna] == pos:
                        break
                if tab_pos[linha][coluna] == pos:
                        break
            diagonais = obtem_diagonais(tab, tab_pos[linha][coluna])
            for pos_diag in range(len(diagonais[0])):#para descobrir em que local da diagonal a posição se encontra
                if diagonais[0][pos_diag] == pos:
                    break
            for pos_anti in range(len(diagonais[1])):#para descobrir em que local da antidiagonal a posição se encontra
                if diagonais[1][pos_anti] == pos:
                    break
            if linha-1 >= 0 and coluna-1 >= 0: #diagonal cima esquerda
                resultado += (diagonais[0][pos_diag-1],)
            if linha-1 >= 0: #cima
                resultado += (tab_pos[linha-1][coluna],)
            if linha-1 >= 0 and coluna+1 < len(tab[0]): #diagonal cima direita
                resultado += (diagonais[1][pos_anti+1],)
            if coluna-1 >= 0: #esquerda
                resultado += (tab_pos[linha][coluna-1],)
            if coluna+1 < len(tab[0]): #direita
                resultado += (tab_pos[linha][coluna+1],)
            if linha+1 < len(tab) and coluna-1 >= 0: #diagonal baixo esquerda
                    resultado += (diagonais[1][pos_anti-1],)
            if linha+1 < len(tab): #baixo
                resultado += (tab_pos[linha+1][coluna],)
            if linha+1 < len(tab) and coluna+1 < len(tab[0]): #diagonal baixo direita
                    resultado += (diagonais[0][pos_diag+1],)
            return resultado
        else:  
            raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    else:
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')


def coordenadas_pos(tab,pos):
    '''
    A função recebe um tabuleiro de posições e uma posição, ambos validados na função que for utilizado, e devolve
    as coordenadas da posição recebida. A origem das coordenadas é a posição 1, com coordendas (0,0).
    '''
    for linha in range(len(tab)):
        for coluna in range(len(tab[0])): #para descobrir em que linha e em que coluna a posição se encontra
            if tab[linha][coluna] == pos:
                break
        if tab[linha][coluna] == pos:
            break
    return (linha, coluna)
        

def ordena_posicoes_tabuleiro(tab,tup):
    '''
    A função recebe um tabuleiro válido e um tuplo contendo posições do tabuleiro. 
    Retorna a distância das posições do tuplo ao centro, sendo a primeira o centro e em seguida na ordem crescente
    de cada distância.
    '''
    if eh_tabuleiro(tab) and type(tup) == tuple:
        if tup != (): 
            for i in tup:
                if not eh_posicao(i):
                     raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
                if not eh_posicao_valida(tab, i):
                    raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos') 
            centro = (len(tab)//2)*len(tab[0])+len(tab[0])//2+1
            tab_pos = tab_para_pos(tab)
            coord_centro = coordenadas_pos(tab_pos, centro)
            distancias = ()
            resultado = ()
            distancia = 0
            for i in tup:
                coord_pos = coordenadas_pos(tab_pos, i)
                dist_centro = max((abs(coord_pos[0] - coord_centro[0])), abs(coord_pos[1] - coord_centro[1])) #cálculo da distancia ao centro baseada na distância de Chebyshev
                distancias += (dist_centro,) #criando um tuplo com as distâncias de cada posição ao centro
            while len(tup) != len(resultado): #se forem do mesmo tamanho, sabemos que já teremos o resultado completo
                for i in range(len(distancias)): 
                    if distancia == distancias[i]: #percorre cada elemento do tuplo das distâncias e escreve por ordem crescente
                        resultado += (tup[i],)
                distancia += 1
            return resultado
        else:
            return ()
    else:
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')


def marca_posicao(tab,pos,jog):
    '''
    A função recebe um tabuleiro válido, uma posição livre (0) e um jogador,
    sendo esse 1 ou -1. Devolve um novo tabuleiro com a posição livre
    substituída por uma pedra do jogador indicado.
    '''
    if eh_tabuleiro(tab) and eh_posicao(pos) and type(jog) == int and jog in (-1,1):
        if eh_posicao_valida(tab, pos):
            if eh_posicao_livre(tab,pos):
                tab_pos = tab_para_pos(tab)
                coordenadas = coordenadas_pos(tab_pos, pos)
                resultado = ()
                contador = 0
                tuplo = ()
                n = 1
                for linhas in range(len(tab)):
                    for colunas in range(len(tab[linhas])):
                        if (linhas,colunas) == (coordenadas[0], coordenadas[1]): #se chegarmos na posição livre, a adicionaremos e saltaremos o resto do loop.
                            tuplo += (jog,) 
                            contador += 1 
                            if contador == len(tab[0])*n:
                                n+=1
                                resultado += (tuplo,)
                                tuplo = ()
                            continue
                        tuplo += (tab[linhas][colunas],) 
                        contador += 1
                        if contador == len(tab[0])*n: #ao chegar no número de colunas do tabuleiro, adicionará essa linha no tabuleiro novo.
                            n += 1
                            resultado += (tuplo,)
                            tuplo = ()
                if contador == len(tab[0])*n:#se a jogada for na posição final, é necessário adicionar o tuplo ao resultado posteriomente
                    resultado += (tuplo,)
                return resultado
            else:
                raise ValueError('marca_posicao: argumentos invalidos')
        else:
            raise ValueError('marca_posicao: argumentos invalidos')
    else:
        raise ValueError('marca_posicao: argumentos invalidos')


def verifica_k_linhas(tab,pos,jog,k):
    '''
    A função recebe um tabuleiro válido, uma posição válida, um jogador (-1 ou 1) e uma inteiro positivo k
    que indica o número de elementos que a sequência das pedras do jogador precisa ter.
    Retorna True se o jogador tiver uma sequência de número k com suas pedras e com a posição válida
    contida nessa numa linha, coluna ou diagonal, e retorna False caso não exista nenhuma sequência
    que cumpra esses requisitos.
    '''
    if eh_tabuleiro(tab) and eh_posicao(pos) and type(jog) == int and jog in (-1,1) and type(k) == int and k>0:
        if not eh_posicao_valida(tab, pos):
            raise ValueError('verifica_k_linhas: argumentos invalidos')
        coluna_pos = obtem_coluna(tab, pos)
        linha_pos = obtem_linha(tab,pos)
        diagonal_pos = obtem_diagonais(tab, pos)
        contador = 0
        tuplo_pos = ()
        tab_pos = tab_para_pos(tab)
        for i in coluna_pos: #coluna
            coordenadas = coordenadas_pos(tab_pos, i)
            if tab[coordenadas[0]][coordenadas[1]] == jog: #se houver a pedra do jogador, começamos a contar a sequência
                contador += 1
                tuplo_pos += (i,) #armazenamos a posição
            else:
                contador = 0 #em caso de não ser a pedra do jogador, a sequência reinicia
            if contador == k: #atingimos a sequência indicada por k
                if pos in tuplo_pos: #apenas será verdadeiro se a posição indicada estiver contida no tuplo das posições
                    return True
                else:
                    tuplo_pos = ()
        contador = 0
        tuplo_pos = ()
        for i in linha_pos: #linha
            coordenadas = coordenadas_pos(tab_pos, i)
            if tab[coordenadas[0]][coordenadas[1]] == jog:
                contador += 1
                tuplo_pos += (i,) 
            else:
                contador = 0 
            if contador == k:
                if pos in tuplo_pos:
                    return True
                else:
                    tuplo_pos = ()
        contador = 0
        tuplo_pos = ()
        for i in diagonal_pos[0]: #diagonal esquerda direita
            coordenadas = coordenadas_pos(tab_pos, i)
            if tab[coordenadas[0]][coordenadas[1]] == jog:
                contador += 1
                tuplo_pos += (i,)
            else:
                contador = 0
            if contador == k:
                if pos in tuplo_pos:
                    return True
                else:
                    tuplo_pos = ()
        contador = 0
        tuplo_pos = ()
        for i in diagonal_pos[1]: #diagonal direita esquerda
            coordenadas = coordenadas_pos(tab_pos, i)
            if tab[coordenadas[0]][coordenadas[1]] == jog:
                contador += 1
                tuplo_pos += (i,)
            else:
                contador = 0
            if contador == k:
                if pos in tuplo_pos:
                    return True
                else:
                    tuplo_pos = ()
        return False
    else:
        raise ValueError('verifica_k_linhas: argumentos invalidos')

def eh_fim_jogo(tab, k):
    '''
    A função recebe um tabuleiro válido e um inteiro positivo k.
    Retorna um booleano (True or False) se o jogo acabou. O jogo acaba ou quando um 
    jogador consegue uma sequência de k peças numa coluna, linha ou diagonal ou
    se não existirem mais posições livres.
    '''
    if eh_tabuleiro(tab) and type(k) == int and k>0:
        tab_pos = tab_para_pos(tab)
        livres = obtem_posicoes_livres(tab)
        if livres == ():
            return True
        for linha in range(len(tab_pos)):
            for entrada in tab_pos[linha]:
                if entrada not in livres:
                    if verifica_k_linhas(tab, entrada, 1, k): #Verifica se o jogador 1 conseguiu uma sequência válida
                        return True 
                    if verifica_k_linhas(tab, entrada, -1, k): #Verifica se o jogador -1 conseguiu uma sequência válida
                        return True
        return False
    else:
        raise ValueError('eh_fim_jogo: argumentos invalidos')

def escolhe_posicao_manual(tab):
    '''
    A função recebe um tabuleiro válido e, ao longo de sua execução, pede ao usuário uma posição
    livre do tabuleiro. Retorna essa mesma posição livre.
    '''
    if eh_tabuleiro(tab):
        i=0
        while i == 0:
            posicao = input("Turno do jogador. Escolha uma posicao livre: ")
            if posicao.isdigit():
                posicao = int(posicao)
                if eh_posicao(posicao):
                    if eh_posicao_valida(tab, posicao):
                        if eh_posicao_livre(tab, posicao):
                            i+=1
        return posicao
    else:
        raise ValueError('escolhe_posicao_manual: argumento invalido')


def jogar_medio(tab, k, jog):
    '''
    A função recebe um tabuleiro, um k, e um jogador, todos já avaliados, e retorna uma simulação
    em que os dois jogadores utilizam a estratégia normal um contra o outro, retornando True se o jogador
    indicado vencer.
    '''
    posicoes_livres_ordenadas = ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))
    posicao_jogada_jogador = ()
    posicao_jogada_adversario = ()
    maximo_jogador = 0
    maximo_adversario = 0
    for posicao in posicoes_livres_ordenadas: #vamos colocar uma pedra em cada espaço livre
        for i in range(k, 0, -1): #o k irá reduzindo, assim teremos o maior que verifica k linhas
            tab_temp1 = marca_posicao(tab, posicao, jog) #marcamos a posição no tabuleiro
            if verifica_k_linhas(tab_temp1, posicao, jog, i) and i>maximo_jogador: #verifica se, para o dado k, existe alguma posicao que verifica k linhas
                posicao_jogada_jogador += ((posicao, i),) #guardaremos o conjunto das posições e seus k
                maximo_jogador = i #se existir um k menor que satisfaz k linhas, não precisaremos o guardar pois já achamos o k mais elevado
            tab_temp2 = marca_posicao(tab, posicao, -jog) #mesmo processo para o outro jogador
            if verifica_k_linhas(tab_temp2, posicao, -jog, i) and i>maximo_adversario:
                posicao_jogada_adversario += ((posicao, i),)
                maximo_adversario = i
        (maximo_jogador, maximo_adversario) = (0,0) #reiniciamos para repetirmos o processo em outra posição livre
    maximo_jogador = posicao_jogada_jogador[0]
    maximo_adversario = posicao_jogada_adversario[0]
    for i in posicao_jogada_jogador: #procurando o par com k mais elevado
        if i[1]>maximo_jogador[1]:
            maximo_jogador = i
    for i in posicao_jogada_adversario: #mesmo processo
        if i[1]>maximo_adversario[1]:
            maximo_adversario = i
    if maximo_jogador[1] == maximo_adversario[1]: #se tiverem k igual (podemos considerar k como L para relacionar com o enunciado)
            return maximo_jogador[0] #jogar na posição que faz o jogador ganhar
    elif maximo_jogador[1] <= maximo_adversario[1]:
        return maximo_adversario[0] #impedir o adversário
    else:
        return maximo_jogador[0] #jogar na melhor posição
    

def simular_medio(tab, k, jog):
    '''
    A função recebe um tabuleiro, um inteiro indicando a sequência para a vitória (k), um jogador, anteriormente 
    avaliados, e simula um jogo em
    que os dois jogadores (robôs) utilizam a estratégia normal um contra o outro.
    Retorna True (booleano) se o jogador indicado ganhar.
    '''
    tab_pos = tab_para_pos(tab)
    dim = obtem_dimensao(tab)
    while not eh_fim_jogo(tab, k):
        posicao_jog = jogar_medio(tab, k, -jog) #turno do jogador
        tab = marca_posicao(tab, posicao_jog, -jog)
        if eh_fim_jogo(tab, k): #a cada turno temos que avaliar se o jogo acabou
            break
        posicao_adv = jogar_medio(tab, k, jog)
        tab = marca_posicao(tab, posicao_adv, jog)
    for i in range(dim[0]): #analisar quem ganhou ou se empatou
        for j in range(dim[1]):
            if tab[i][j] == jog:
                if verifica_k_linhas(tab, tab_pos[i][j], jog, k):
                    return "Vitoria"
                if verifica_k_linhas(tab, tab_pos[i][j], -jog, k):
                    return "Derrota"
    return "Empate"


def escolhe_posicao_auto(tab, jog, k, lvl):
    '''
    A função recebe um tabuleiro válido, um jogador (-1 para O e 1 para X), um número de uma sequência
    que dará a vitória (k) e uma dificuldade, podendo ser "facil", "medio" ou "dificil".
    Devolve a melhor posição para jogar de acordo com a dificuldade escolhida e seguindo as regras
    de cada algoritmo.
    '''
    if eh_tabuleiro(tab) and jog in (-1, 1) and type(jog) == int and type(k) == int and k>0 and lvl in ("facil", "normal", "dificil"):
        if lvl == "facil":
            tuplo = ()
            centro = (len(tab)//2)*len(tab[0])+len(tab[0])//2+1
            pos = obtem_posicoes_jogador(tab, jog)
            posicoes_livres = obtem_posicoes_livres(tab)
            if pos == ():
                return ordena_posicoes_tabuleiro(tab, posicoes_livres)[0]
            for posicoes in pos:
                adjacentes = obtem_posicoes_adjacentes(tab, posicoes)
                for i in adjacentes:
                    if eh_posicao_livre(tab, i):
                        tuplo += (i,)
            if tuplo != ():
                return ordena_posicoes_tabuleiro(tab, tuplo)[0]
            if tuplo == ():
                if centro in posicoes_livres:
                    return centro
                else:
                    return ordena_posicoes_tabuleiro(tab, posicoes_livres)[0]
        if lvl == "normal": 
            return jogar_medio(tab, k, jog)
        if lvl == "dificil":
            pos_livres = ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))
            if pos_livres != ():
                for pos in pos_livres:
                    tab_temp = marca_posicao(tab, pos, jog)
                    if verifica_k_linhas(tab_temp, pos, jog, k):
                        return pos
                    tab_temp = marca_posicao(tab, pos, -jog)
                    if verifica_k_linhas(tab_temp, pos, -jog, k):
                        return pos
            pos_empate = 0
            n = 1
            for pos in pos_livres:
                tab_temp = marca_posicao(tab, pos, jog)
                simulacao = simular_medio(tab_temp, k, jog)
                if simulacao == "Vitoria":
                    return pos
                if simulacao == "Empate" and n == 1:
                    pos_empate = pos
                    n = n-1
            if pos_empate > 0:
                return pos_empate
            return ordena_posicoes_tabuleiro(tab, pos_livres)[0]
    else:
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
                    

def jogo_mnk(cfg, jog, lvl):
    '''
    A função recebe um tuplo que indica, por ordem, a quantidade de linhas do tabuleiro (m), a quantidade de colunas
    do tabuleiro (n) e quantas peças para ganhar (k), também recebe um jogador (1 para X e -1 para O) e o nível
    de dificuldade, podendo ser "facil", "medio" ou "dificil".
    Retorna um tabuleiro com representação externa com as proporções indicadas 
    e pede uma posição livre para o jogador colocar sua peça. Em seguida, será jogada uma peça
    automaticamente pelo jogador contrário seguindo o algoritmo da dificuldade pedida. O processo se repetirá
    até que não existam mais posições livres ou um jogador marque a sequência indicada no início (k).
    '''
    if type(cfg) == tuple and jog in (-1,1) and type(jog) == int and lvl in ("facil", "normal", "dificil"):
        for i in cfg:
            if type(i) != int:
                raise ValueError("jogo_mnk: argumentos invalidos")
        if not (2<=cfg[0]<=100 and 2<=cfg[1]<=100 and cfg[2] > 0):
            raise ValueError("jogo_mnk: argumentos invalidos")
        tuplo = ()
        n=1
        tab = ()
        for i in range(cfg[0]*cfg[1]+1): #criando o tabuleiro
            if i == cfg[1]*n:
                n += 1
                tab += (tuplo,)
                tuplo = ()
            tuplo += (0,)
        tab_pos = tab_para_pos(tab)
        if jog == 1:
            simbolo = "X"
        else:
            simbolo = "O"
        print(f"Bem-vindo ao JOGO MNK.\nO jogador joga com '{simbolo}'.\n{tabuleiro_para_str(tab)}")
        if jog == 1:
            while not eh_fim_jogo(tab, cfg[2]):
                posicao_jog = escolhe_posicao_manual(tab) #turno do jogador
                tab = marca_posicao(tab, posicao_jog, jog)
                print(tabuleiro_para_str(tab)) 
                if eh_fim_jogo(tab, cfg[2]): #a cada turno temos que avaliar se o jogo acabou
                    break
                print(f"Turno do computador ({lvl}):") #turno do computador
                posicao_bot = escolhe_posicao_auto(tab, -jog, cfg[2], lvl)
                tab = marca_posicao(tab, posicao_bot, -jog)
                print(tabuleiro_para_str(tab))
        if jog == -1:
            while not eh_fim_jogo(tab, cfg[2]):
                print(f"Turno do computador ({lvl}):") #turno do computador
                posicao_bot = escolhe_posicao_auto(tab, -jog, cfg[2], lvl)
                tab = marca_posicao(tab, posicao_bot, -jog)
                print(tabuleiro_para_str(tab))
                if eh_fim_jogo(tab, cfg[2]): #a cada turno temos que avaliar se o jogo acabou
                    break
                posicao_jog = escolhe_posicao_manual(tab) #turno do jogador
                tab = marca_posicao(tab, posicao_jog, jog)
                print(tabuleiro_para_str(tab)) 
        for i in range(cfg[1]): #analisar quem ganhou ou se empatou
            for j in range(cfg[1]):
                if tab[i][j] == jog:
                    if verifica_k_linhas(tab, tab_pos[i][j], jog, cfg[2]):
                        print("VITORIA")
                        return jog       
                if tab[i][j] == -jog:
                    if verifica_k_linhas(tab, tab_pos[i][j], -jog, cfg[2]):
                        print("DERROTA")
                        return -jog
        print("EMPATE")
        return 0
    else:
        raise ValueError('jogo_mnk: argumentos invalidos')

