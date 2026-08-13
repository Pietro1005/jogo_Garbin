import random


# ==========================================================
# THE BLACKWOOD HOUSE
# JOGO DE TERROR SLASHER
# PARTE 1
# ==========================================================


# ==========================================================
# ESTADO DO JOGADOR
# ==========================================================

state = {
    "vida": 5,
    "inventario": [],
    "assassino_alertado": False,
    "gerador_ligado": False,
    "sobrevivente_salvo": False
}


# ==========================================================
# FUNÇÃO PARA FAZER ESCOLHAS
# ==========================================================

def escolher(mensagem, opcoes):

    while True:

        resposta = input(mensagem).strip().lower()

        if resposta in opcoes:
            return resposta

        print("\n⚠️ Opção inválida. Tente novamente.")


# ==========================================================
# INVENTÁRIO
# ==========================================================

def pegar(item):

    if item not in state["inventario"]:

        state["inventario"].append(item)

        print(f"\n🎒 Você encontrou: {item}!")

    else:

        print(f"\nVocê já possui {item}.")


def mostrar_inventario():

    print("\n========== INVENTÁRIO ==========")

    if len(state["inventario"]) == 0:

        print("Seu inventário está vazio.")

    else:

        for item in state["inventario"]:
            print(f"- {item}")

    print("================================")


# ==========================================================
# STATUS
# ==========================================================

def mostrar_status():

    print("\n================================")
    print(f"❤️ Vida: {state['vida']}/5")

    if state["inventario"]:

        print("🎒 Itens:", ", ".join(state["inventario"]))

    else:

        print("🎒 Itens: Nenhum")

    print("================================")


# ==========================================================
# DANO
# ==========================================================

def receber_dano(valor):

    state["vida"] -= valor

    print(f"\n💥 Você perdeu {valor} ponto(s) de vida!")

    if state["vida"] <= 0:

        state["vida"] = 0

        return True

    return False


# ==========================================================
# USAR KIT MÉDICO
# ==========================================================

def usar_kit():

    if "kit medico" not in state["inventario"]:

        print("\nVocê não possui um kit médico.")

        return False

    if state["vida"] >= 5:

        print("\n❤️ Sua vida já está cheia.")

        return False

    state["inventario"].remove("kit medico")

    state["vida"] += 2

    if state["vida"] > 5:
        state["vida"] = 5

    print("\n🩹 Você utilizou o kit médico.")

    print(f"❤️ Vida atual: {state['vida']}/5")

    return True


# ==========================================================
# EVENTOS ALEATÓRIOS
# ==========================================================

def evento_terror():

    numero = random.randint(1, 8)

    if numero == 1:

        print("""
👣 Você escuta passos atrás de você.

Quando se vira...

Não há ninguém.
""")

    elif numero == 2:

        print("""
💡 As luzes piscam três vezes.

Depois tudo volta ao normal.
""")

    elif numero == 3:

        print("""
🔪 Você encontra uma faca cravada em uma porta.

Alguém esteve aqui recentemente.
""")

    elif numero == 4:

        print("""
📻 Um rádio distante começa a transmitir uma voz.

"Ele está atrás de você..."
""")

    elif numero == 5:

        print("""
🪟 Uma janela bate violentamente por causa do vento.

Você leva um susto.
""")

    elif numero == 6:

        print("""
😨 Um objeto cai no chão em outro cômodo.

Você não está sozinho.
""")

    elif numero == 7:

        print("""
🩸 Você percebe pequenas marcas no chão.

Elas parecem levar até o porão.
""")

    else:

        print("""
🤫 Por alguns segundos, a mansão fica completamente silenciosa.

Esse silêncio é ainda mais assustador.
""")


# ==========================================================
# INTRODUÇÃO
# ==========================================================

def inicio():

    print("""
============================================================
                 THE BLACKWOOD HOUSE
============================================================

23:47.

Uma tempestade cai sobre a estrada.

Você está voltando para casa quando seu carro para
repentinamente.

O motor morreu.

Você tenta ligar novamente.

Nada.

Seu celular também não possui sinal.

Então você percebe uma enorme mansão no alto de uma
colina.

Uma única luz está acesa em uma das janelas.

Você decide procurar ajuda.

Ao entrar na mansão...

                *CLAC*

A porta se fecha atrás de você.

Você tenta abri-la.

Está trancada.

Um trovão ilumina o corredor através das janelas.

Por uma fração de segundo, você vê uma pessoa usando
uma máscara parada no segundo andar.

Quando o próximo relâmpago acontece...

Ela desapareceu.

Você percebe que está segurando a respiração.

Agora começa sua luta para sobreviver.
""")

    input("\nPressione ENTER para continuar...")


    print("""
Você precisa encontrar uma saída.

Talvez exista um telefone.

Talvez exista alguma chave.

Ou talvez alguém ainda esteja vivo dentro desta casa.
""")

    input("\nPressione ENTER para continuar...")

    return "hall"


# ==========================================================
# HALL PRINCIPAL
# ==========================================================

def hall():

    evento_terror()

    mostrar_status()

    print("""
============================================================
                    HALL PRINCIPAL
============================================================

Você está no enorme hall de entrada.

Uma escadaria leva ao segundo andar.

Existem várias portas ao redor.

Você consegue identificar:

1 - Cozinha
2 - Biblioteca
3 - Banheiro
4 - Escritório
5 - Escadas
6 - Ver inventário
7 - Usar kit médico
""")

    escolha = escolher(
        "\nO que você deseja fazer? ",
        ["1", "2", "3", "4", "5", "6", "7"]
    )


    if escolha == "1":

        return "cozinha"


    elif escolha == "2":

        return "biblioteca"


    elif escolha == "3":

        return "banheiro"


    elif escolha == "4":

        return "escritorio"


    elif escolha == "5":

        return "escadas"


    elif escolha == "6":

        mostrar_inventario()

        input("\nPressione ENTER para continuar...")

        return "hall"


    elif escolha == "7":

        usar_kit()

        input("\nPressione ENTER para continuar...")

        return "hall"


# ==========================================================
# COZINHA
# ==========================================================

def cozinha():

    evento_terror()

    print("""
============================================================
                       COZINHA
============================================================

A cozinha está completamente abandonada.

Pratos quebrados estão espalhados pelo chão.

A geladeira faz um barulho estranho.

Existe uma enorme faca sobre a bancada.

Você também encontra um armário antigo.
""")

    print("""
1 - Procurar nas gavetas
2 - Abrir a geladeira
3 - Procurar no armário
4 - Voltar ao hall
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4"]
    )


    # ------------------------------------------------------
    # GAVETAS
    # ------------------------------------------------------

    if escolha == "1":

        if "faca" not in state["inventario"]:

            pegar("faca")

            print("""
🔪 Você encontrou uma faca de cozinha.

Ela pode ser útil caso precise se defender.
""")

        else:

            print("\nAs gavetas estão vazias.")

        return "cozinha"


    # ------------------------------------------------------
    # GELADEIRA
    # ------------------------------------------------------

    elif escolha == "2":

        print("""
Você abre lentamente a geladeira.

Não há comida.

Porém, escondido atrás de algumas caixas,
existe um pequeno kit médico.
""")

        if "kit medico" not in state["inventario"]:

            pegar("kit medico")

        else:

            print("\nVocê já pegou o kit médico.")

        return "cozinha"


    # ------------------------------------------------------
    # ARMÁRIO
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
O armário está emperrado.

Você força a porta.

Dentro existe uma pequena lanterna.
""")

        if "lanterna" not in state["inventario"]:

            pegar("lanterna")

            print("""
🔦 A lanterna ainda funciona.

Você decide guardá-la.
""")

        else:

            print("\nO armário está vazio.")

        return "cozinha"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "hall"


# ==========================================================
# BIBLIOTECA
# ==========================================================

def biblioteca():

    evento_terror()

    print("""
============================================================
                     BIBLIOTECA
============================================================

A biblioteca é enorme.

As estantes chegam até o teto.

Uma camada grossa de poeira cobre os livros.

No centro existe uma mesa.

Sobre ela há um diário antigo.
""")

    print("""
1 - Ler o diário
2 - Procurar nas estantes
3 - Abrir a gaveta da mesa
4 - Voltar ao hall
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4"]
    )


    # ------------------------------------------------------
    # DIÁRIO
    # ------------------------------------------------------

    if escolha == "1":

        if "diario" not in state["inventario"]:

            pegar("diario")

            print("""
📖 Você começa a ler o diário.

A última página chama sua atenção.

"Se alguém encontrar este diário,
não confie no homem da máscara.

Ele conhece todos os caminhos da casa.

A única forma de escapar é encontrar
a chave da garagem."

A página seguinte foi arrancada.
""")

        else:

            print("\nVocê já leu o diário.")

        return "biblioteca"


    # ------------------------------------------------------
    # ESTANTES
    # ------------------------------------------------------

    elif escolha == "2":

        print("""
Você procura entre os livros.

Um deles parece diferente.

Ao puxá-lo, uma pequena passagem secreta
se abre na parede.
""")

        if "chave enferrujada" not in state["inventario"]:

            pegar("chave enferrujada")

            print("""
🔑 Você encontrou uma chave enferrujada.

Talvez ela abra alguma porta antiga.
""")

        else:

            print("\nVocê já encontrou a chave.")

        return "biblioteca"


    # ------------------------------------------------------
    # GAVETA
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
A gaveta está trancada.

Você tenta puxá-la.

Nada acontece.

Talvez seja necessário encontrar uma ferramenta.
""")

        return "biblioteca"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "hall"
# ==========================================================
# PARTE 2
# OUTRAS CENAS DA MANSÃO
# ==========================================================


# ==========================================================
# BANHEIRO
# ==========================================================

def banheiro():

    evento_terror()

    print("""
============================================================
                       BANHEIRO
============================================================

O banheiro está completamente escuro.

A torneira pinga lentamente.

*PING...*

*PING...*

O espelho está quebrado e existem manchas estranhas
nas paredes.

Você vê um armário, uma pia e uma pequena janela.
""")

    print("""
1 - Abrir o armário
2 - Examinar o espelho
3 - Procurar na pia
4 - Tentar abrir a janela
5 - Voltar ao hall
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4", "5"]
    )


    # ------------------------------------------------------
    # ARMÁRIO
    # ------------------------------------------------------

    if escolha == "1":

        if "pilhas" not in state["inventario"]:

            pegar("pilhas")

            print("""
🔋 Você encontrou duas pilhas novas.

Elas podem ser utilizadas na lanterna.
""")

        else:

            print("\nO armário está vazio.")

        return "banheiro"


    # ------------------------------------------------------
    # ESPELHO
    # ------------------------------------------------------

    elif escolha == "2":

        print("""
Você olha para o espelho quebrado.

Por um instante, você vê uma pessoa atrás de você.

Você se vira rapidamente.

Não existe ninguém.

Quando olha novamente para o espelho...

A figura desapareceu.
""")

        state["assassino_alertado"] = True

        return "banheiro"


    # ------------------------------------------------------
    # PIA
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
Você procura dentro da pia.

Entre alguns objetos enferrujados,
encontra uma pequena chave.
""")

        if "chave pequena" not in state["inventario"]:

            pegar("chave pequena")

        else:

            print("\nVocê já pegou a chave.")

        return "banheiro"


    # ------------------------------------------------------
    # JANELA
    # ------------------------------------------------------

    elif escolha == "4":

        print("""
Você tenta abrir a janela.

Ela está emperrada.

Depois de alguns segundos, consegue abri-la.

A janela dá para um pequeno jardim.

Talvez seja uma possível rota de fuga.
""")

        return "jardim"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "hall"


# ==========================================================
# ESCRITÓRIO
# ==========================================================

def escritorio():

    evento_terror()

    print("""
============================================================
                      ESCRITÓRIO
============================================================

O escritório parece ter pertencido ao antigo dono
da mansão.

Existe uma grande escrivaninha.

Um computador antigo está sobre ela.

Nas paredes existem fotografias da família Blackwood.
""")

    print("""
1 - Examinar a escrivaninha
2 - Ler documentos
3 - Ligar o computador
4 - Examinar as fotografias
5 - Voltar ao hall
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4", "5"]
    )


    # ------------------------------------------------------
    # ESCRIVANINHA
    # ------------------------------------------------------

    if escolha == "1":

        if "cartao seguranca" not in state["inventario"]:

            pegar("cartao seguranca")

            print("""
💳 Você encontrou um cartão de segurança.

Talvez ele abra alguma área restrita.
""")

        else:

            print("\nA escrivaninha está vazia.")

        return "escritorio"


    # ------------------------------------------------------
    # DOCUMENTOS
    # ------------------------------------------------------

    elif escolha == "2":

        print("""
Você encontra documentos antigos.

Eles mencionam diversos desaparecimentos.

Todos aconteceram dentro da mansão.

A última anotação diz:

"Não deixe o assassino chegar ao porão."
""")

        return "escritorio"


    # ------------------------------------------------------
    # COMPUTADOR
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
O computador pede uma senha.

Você não sabe a senha.

Talvez exista alguma pista em outro cômodo.
""")

        return "escritorio"


    # ------------------------------------------------------
    # FOTOGRAFIAS
    # ------------------------------------------------------

    elif escolha == "4":

        print("""
Você examina as fotografias.

Em uma delas aparece um homem usando
uma máscara muito parecida com a que você viu.

No verso está escrito:

"Michael Blackwood - 1987"
""")

        return "escritorio"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "hall"


# ==========================================================
# GARAGEM
# ==========================================================

def garagem():

    evento_terror()

    print("""
============================================================
                       GARAGEM
============================================================

Você encontra uma grande garagem.

Há uma caminhonete antiga estacionada.

Também existem caixas, ferramentas e um armário.

Se conseguir fazer o veículo funcionar,
talvez consiga escapar da mansão.
""")

    print("""
1 - Examinar caminhonete
2 - Procurar ferramentas
3 - Procurar gasolina
4 - Abrir armário
5 - Voltar
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4", "5"]
    )


    # ------------------------------------------------------
    # CAMINHONETE
    # ------------------------------------------------------

    if escolha == "1":

        if "gasolina" in state["inventario"]:

            print("""
Você encontrou o tanque da caminhonete.

Parece que existe combustível suficiente.

Mas a bateria está descarregada.

Talvez seja necessário encontrar uma forma
de restaurar a energia.
""")

        else:

            print("""
A caminhonete está sem combustível.

Você precisará encontrar gasolina.
""")

        return "garagem"


    # ------------------------------------------------------
    # FERRAMENTAS
    # ------------------------------------------------------

    elif escolha == "2":

        if "machado" not in state["inventario"]:

            pegar("machado")

            print("""
🪓 Você encontrou um machado.

Ele pode ser usado para quebrar obstáculos
ou se defender.
""")

        else:

            print("\nAs ferramentas já foram examinadas.")

        return "garagem"


    # ------------------------------------------------------
    # GASOLINA
    # ------------------------------------------------------

    elif escolha == "3":

        if "gasolina" not in state["inventario"]:

            pegar("gasolina")

            print("""
⛽ Você encontrou um galão de gasolina.

Agora talvez consiga fazer a caminhonete funcionar.
""")

        else:

            print("\nVocê já possui gasolina.")

        return "garagem"


    # ------------------------------------------------------
    # ARMÁRIO
    # ------------------------------------------------------

    elif escolha == "4":

        if "fusivel" not in state["inventario"]:

            pegar("fusivel")

            print("""
🔌 Você encontrou um fusível antigo.

Ele pode ser útil para restaurar a energia.
""")

        else:

            print("\nO armário está vazio.")

        return "garagem"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "hall"


# ==========================================================
# PORÃO
# ==========================================================

def porao():

    evento_terror()

    print("""
============================================================
                        PORÃO
============================================================

Você desce as escadas.

A temperatura cai rapidamente.

A luz do teto pisca.

Você encontra um gerador antigo.

Também existe uma porta de metal com um painel
eletrônico.
""")

    print("""
1 - Examinar gerador
2 - Examinar porta de metal
3 - Procurar objetos
4 - Subir
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4"]
    )


    # ------------------------------------------------------
    # GERADOR
    # ------------------------------------------------------

    if escolha == "1":

        if "fusivel" not in state["inventario"]:

            print("""
O gerador está quebrado.

Está faltando um fusível.
""")

        else:

            if not state["gerador_ligado"]:

                print("""
Você coloca o fusível no gerador.

Depois de algumas tentativas...

BRUUUUM!

O gerador começa a funcionar.

💡 A energia da mansão voltou!
""")

                state["gerador_ligado"] = True

            else:

                print("\nO gerador já está funcionando.")

        return "porao"


    # ------------------------------------------------------
    # PORTA DE METAL
    # ------------------------------------------------------

    elif escolha == "2":

        if "cartao seguranca" in state["inventario"]:

            print("""
Você aproxima o cartão do painel.

BEEP!

A porta se abre.

Atrás dela existe uma pequena sala de segurança.
""")

            return "seguranca"

        else:

            print("""
O painel pede um cartão de segurança.

Você ainda não possui um.
""")

        return "porao"


    # ------------------------------------------------------
    # OBJETOS
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
Você encontra uma caixa de madeira.

Dentro existe um rádio antigo.
""")

        if "radio" not in state["inventario"]:

            pegar("radio")

        else:

            print("\nA caixa está vazia.")

        return "porao"


    # ------------------------------------------------------
    # SUBIR
    # ------------------------------------------------------

    else:

        return "escadas"


# ==========================================================
# SÓTÃO
# ==========================================================

def sotao():

    evento_terror()

    print("""
============================================================
                         SÓTÃO
============================================================

Você sobe até o sótão.

O local está cheio de caixas.

Uma pequena janela deixa entrar a luz da lua.

Você escuta alguém respirando.

Há uma pessoa escondida atrás de algumas caixas.
""")

    print("""
1 - Conversar com a pessoa
2 - Procurar nas caixas
3 - Examinar a janela
4 - Voltar
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4"]
    )


    # ------------------------------------------------------
    # SOBREVIVENTE
    # ------------------------------------------------------

    if escolha == "1":

        if not state["sobrevivente_salvo"]:

            print("""
A pessoa está assustada.

Ela diz:

"Meu nome é Sarah.

Eu estou presa aqui há dois dias.

O assassino conhece todos os cômodos.

Existe uma saída secreta na sala de segurança."

Ela entrega uma chave para você.
""")

            state["sobrevivente_salvo"] = True

            pegar("chave mestra")

        else:

            print("""
Sarah agradece por você não tê-la abandonado.

"Precisamos sair daqui."
""")

        return "sotao"


    # ------------------------------------------------------
    # CAIXAS
    # ------------------------------------------------------

    elif escolha == "2":

        if "fita" not in state["inventario"]:

            pegar("fita")

            print("""
📼 Você encontrou uma fita VHS.

Talvez exista um aparelho para reproduzi-la.
""")

        else:

            print("\nVocê já examinou todas as caixas.")

        return "sotao"


    # ------------------------------------------------------
    # JANELA
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
A janela dá para o telhado.

A queda é muito alta.

Você não pode escapar por aqui.
""")

        return "sotao"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "escadas"


# ==========================================================
# JARDIM
# ==========================================================

def jardim():

    evento_terror()

    print("""
============================================================
                        JARDIM
============================================================

Você sai pela janela do banheiro.

O jardim está completamente abandonado.

Há árvores enormes e uma pequena cabana.

Ao longe existe um portão.

Você percebe uma sombra entre as árvores.
""")

    print("""
1 - Correr até o portão
2 - Ir até a cabana
3 - Esconder-se
4 - Voltar para a casa
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4"]
    )


    # ------------------------------------------------------
    # PORTÃO
    # ------------------------------------------------------

    if escolha == "1":

        if "chave enferrujada" in state["inventario"]:

            print("""
Você coloca a chave no cadeado.

CLIC!

O portão está destrancado.

Você consegue escapar da propriedade!
""")

            return "fim_fuga"

        else:

            print("""
O portão está trancado.

Você precisa encontrar uma chave.
""")

            return "jardim"


    # ------------------------------------------------------
    # CABANA
    # ------------------------------------------------------

    elif escolha == "2":

        print("""
Você entra na pequena cabana.

Dentro existe uma caixa de ferramentas.
""")

        if "pe de cabra" not in state["inventario"]:

            pegar("pe de cabra")

        else:

            print("\nA cabana está vazia.")

        return "jardim"


    # ------------------------------------------------------
    # ESCONDER
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
Você se esconde atrás de uma árvore.

A sombra passa lentamente.

Por sorte, o assassino não percebe você.
""")

        return "hall"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "hall"


# ==========================================================
# FIM DA PARTE 2
# ==========================================================


# ==========================================================
# PARTE 3
# SEGURANÇA, ASSASSINO, PERSEGUIÇÕES E COMBATE
# ==========================================================


# ==========================================================
# SALA DE SEGURANÇA
# ==========================================================

def seguranca():

    print("""
============================================================
                    SALA DE SEGURANÇA
============================================================

Você entra em uma pequena sala escondida no porão.

Existem vários monitores mostrando diferentes partes
da mansão.

Uma mesa possui um rádio.

Na parede existe um painel com vários botões.

Você percebe algo assustador...

Uma das câmeras mostra o assassino caminhando pelo
corredor.

Ele parece estar procurando por você.
""")

    print("""
1 - Ver câmeras
2 - Usar o rádio
3 - Procurar uma saída secreta
4 - Assistir à fita VHS
5 - Voltar ao porão
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4", "5"]
    )


    # ------------------------------------------------------
    # CÂMERAS
    # ------------------------------------------------------

    if escolha == "1":

        print("""
Você observa os monitores.

Câmera 1: Hall principal.
Câmera 2: Cozinha.
Câmera 3: Biblioteca.
Câmera 4: Jardim.
Câmera 5: Segundo andar.

De repente...

A câmera do hall mostra o assassino.

Ele olha diretamente para a câmera.

Depois...

A imagem fica preta.
""")

        state["assassino_alertado"] = True

        return "seguranca"


    # ------------------------------------------------------
    # RÁDIO
    # ------------------------------------------------------

    elif escolha == "2":

        if "radio" not in state["inventario"]:

            print("""
Você não possui um rádio.

Talvez exista um no porão.
""")

            return "seguranca"


        print("""
Você pega o rádio e tenta encontrar uma frequência.

*CHIADO...*

Nada.

Você tenta novamente.

*CHIADO...*

Uma voz responde:

"Se alguém estiver ouvindo...

saia dessa casa imediatamente."

Você pergunta quem está falando.

A resposta é:

"Não importa.

Ele já sabe onde você está."
""")

        print("""
Você possui duas opções:

1 - Pedir ajuda
2 - Perguntar sobre o assassino
""")

        resposta = escolher(
            "\nEscolha: ",
            ["1", "2"]
        )


        if resposta == "1":

            print("""
Você pede ajuda pelo rádio.

A voz responde:

"Continue transmitindo.

A polícia está a caminho."
""")

            state["radio_ajuda"] = True

        else:

            print("""
Você pergunta quem é o assassino.

Depois de alguns segundos...

A voz responde:

"Michael Blackwood."

O rádio desliga.

Você lembra da fotografia encontrada
no escritório.
""")

        return "seguranca"


    # ------------------------------------------------------
    # SAÍDA SECRETA
    # ------------------------------------------------------

    elif escolha == "3":

        if "chave mestra" in state["inventario"]:

            print("""
Você encontra uma porta escondida atrás dos monitores.

A chave mestra funciona.

Você abre a porta.

Atrás dela existe um túnel que leva para fora
da propriedade.

Talvez essa seja sua melhor chance.
""")

            return "tunel"

        else:

            print("""
Você encontra uma porta secreta.

Ela está trancada.

Você precisa de uma chave especial.
""")

            return "seguranca"


    # ------------------------------------------------------
    # FITA VHS
    # ------------------------------------------------------

    elif escolha == "4":

        if "fita" not in state["inventario"]:

            print("""
Você não possui nenhuma fita.
""")

            return "seguranca"


        print("""
Você coloca a fita no aparelho.

A televisão começa a funcionar.

A gravação mostra a mansão muitos anos atrás.

Um homem chamado Michael Blackwood aparece
na gravação.

Ele fala sobre a casa e sobre sua família.

No final da gravação aparece uma mensagem:

"Se você está vendo isso...

ele ainda está aqui."

A televisão desliga.
""")

        state["fita_assistida"] = True

        return "seguranca"


    # ------------------------------------------------------
    # VOLTAR
    # ------------------------------------------------------

    else:

        return "porao"


# ==========================================================
# TÚNEL SECRETO
# ==========================================================

def tunel():

    print("""
============================================================
                     TÚNEL SECRETO
============================================================

Você entra no túnel.

As paredes são antigas.

Depois de alguns metros, encontra duas saídas.

Uma delas leva para a floresta.

A outra parece voltar para a mansão.
""")

    print("""
1 - Ir para a floresta
2 - Voltar para a mansão
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2"]
    )


    if escolha == "1":

        print("""
Você continua pelo túnel.

Depois de alguns minutos...

A luz da lua aparece no final.

Você saiu da propriedade.
""")

        return "fim_tunel"


    return "seguranca"


# ==========================================================
# USAR A LANTERNA
# ==========================================================

def usar_lanterna():

    if "lanterna" not in state["inventario"]:

        print("""
Você não possui uma lanterna.
""")

        return


    print("""
🔦 Você liga a lanterna.

O feixe de luz ilumina o caminho.
""")


    if "pilhas" in state["inventario"]:

        print("""
As pilhas novas aumentam a potência da lanterna.
""")

    else:

        print("""
A luz começa a ficar fraca.

Seria melhor encontrar pilhas.
""")


# ==========================================================
# COMBATE
# ==========================================================

def combate():

    print("""
============================================================
                    CONFRONTO
============================================================

O assassino aparece no final do corredor.

Ele está bloqueando a saída.

Você precisa tomar uma decisão rapidamente.
""")

    print("""
1 - Usar a faca
2 - Usar o machado
3 - Tentar fugir
4 - Se esconder
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4"]
    )


    # ------------------------------------------------------
    # FACA
    # ------------------------------------------------------

    if escolha == "1":

        if "faca" not in state["inventario"]:

            print("""
Você não possui uma arma.

Você tenta escapar.
""")

            return "perseguicao"


        print("""
Você usa a faca para criar uma oportunidade
e consegue escapar do corredor.

O assassino continua atrás de você.
""")

        state["inventario"].remove("faca")

        return "perseguicao"


    # ------------------------------------------------------
    # MACHADO
    # ------------------------------------------------------

    elif escolha == "2":

        if "machado" not in state["inventario"]:

            print("""
Você não possui um machado.
""")

            return "perseguicao"


        print("""
Você segura o machado.

Quando o assassino avança,
você consegue afastá-lo e fugir.

Ele não consegue continuar seguindo você
por alguns instantes.
""")

        state["assassino_alertado"] = False

        return "hall"


    # ------------------------------------------------------
    # FUGIR
    # ------------------------------------------------------

    elif escolha == "3":

        print("""
Você corre pelo corredor.

O assassino começa a persegui-lo.
""")

        return "perseguicao"


    # ------------------------------------------------------
    # ESCONDER
    # ------------------------------------------------------

    else:

        print("""
Você entra rapidamente em um armário.

O assassino passa pelo corredor.

Você segura a respiração.

Depois de alguns segundos...

Ele vai embora.
""")

        return "hall"


# ==========================================================
# PERSEGUIÇÃO
# ==========================================================

def perseguicao():

    print("""
============================================================
                     PERSEGUIÇÃO
============================================================

Você corre pelos corredores da mansão.

Os passos do assassino ficam cada vez mais próximos.

Você chega a uma bifurcação.

Esquerda ou direita?
""")

    print("""
1 - Esquerda
2 - Direita
3 - Esconder-se
4 - Usar a lanterna
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4"]
    )


    # ------------------------------------------------------
    # ESQUERDA
    # ------------------------------------------------------

    if escolha == "1":

        resultado = random.randint(1, 3)

        if resultado == 1:

            print("""
Você entra em um quarto e fecha a porta.

O assassino passa direto.

Você conseguiu escapar!
""")

            return "hall"

        elif resultado == 2:

            print("""
Você entra em uma sala sem saída.

O assassino se aproxima.

Você precisa agir!
""")

            return "combate"

        else:

            print("""
Você encontra uma janela.

Consegue escapar para o jardim.
""")

            return "jardim"


    # ------------------------------------------------------
    # DIREITA
    # ------------------------------------------------------

    elif escolha == "2":

        resultado = random.randint(1, 3)

        if resultado == 1:

            print("""
Você entra na cozinha.

O assassino perde seu rastro.
""")

            return "cozinha"

        elif resultado == 2:

            print("""
Você tropeça em alguns objetos.

O assassino se aproxima.

Você perde 1 ponto de vida.
""")

            if receber_dano(1):

                return "fim_morte"

            return "hall"

        else:

            print("""
Você encontra as escadas.

Você sobe rapidamente.
""")

            return "sotao"


    # ------------------------------------------------------
    # ESCONDER
    # ------------------------------------------------------

    elif escolha == "3":

        resultado = random.randint(1, 2)

        if resultado == 1:

            print("""
Você se esconde atrás de uma cortina.

O assassino entra.

Ele procura por alguns segundos...

Depois vai embora.
""")

            return "hall"

        else:

            print("""
O assassino percebe que alguém está escondido.

Você precisa fugir!
""")

            if receber_dano(1):

                return "fim_morte"

            return "hall"


    # ------------------------------------------------------
    # LANTERNA
    # ------------------------------------------------------

    else:

        usar_lanterna()

        print("""
A luz ilumina uma pequena passagem lateral.

Você corre por ela.
""")

        return "biblioteca"


# ==========================================================
# EVENTO ESPECIAL DO ASSASSINO
# ==========================================================

def encontro_assassino():

    print("""
============================================================
                   O ASSASSINO
============================================================

Você caminha pelo corredor.

Uma porta se abre lentamente.

O homem mascarado aparece.

Ele permanece parado por alguns segundos.

Então começa a caminhar na sua direção.
""")

    print("""
Você precisa decidir rapidamente:

1 - Fugir
2 - Enfrentá-lo
3 - Esconder-se
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3"]
    )


    if escolha == "1":

        return "perseguicao"


    elif escolha == "2":

        return "combate"


    else:

        resultado = random.randint(1, 2)

        if resultado == 1:

            print("""
Você se esconde atrás de uma porta.

O assassino passa.

Você teve sorte.
""")

            return "hall"

        else:

            print("""
O assassino percebe você.

Você tenta escapar.
""")

            if receber_dano(1):

                return "fim_morte"

            return "perseguicao"


# ==========================================================
# EVENTO ESPECIAL DO RÁDIO
# ==========================================================

def usar_radio():

    if "radio" not in state["inventario"]:

        print("""
Você não possui um rádio.
""")

        return "hall"


    print("""
📻 Você liga o rádio.

*CHIADO...*

Uma voz aparece:

"Se você ainda estiver dentro da mansão,
vá para a sala de segurança.

Existe uma saída escondida."
""")

    state["radio_ajuda"] = True

    return "seguranca"


# ==========================================================
# EXAMINAR FITA
# ==========================================================

def examinar_fita():

    if "fita" not in state["inventario"]:

        print("""
Você não possui a fita VHS.
""")

        return "hall"


    print("""
📼 Você observa a fita.

Ela contém uma gravação antiga da família Blackwood.

Talvez a sala de segurança tenha um aparelho
capaz de reproduzi-la.
""")

    return "seguranca"


# ==========================================================
# EVENTO DE ENCONTRO ALEATÓRIO
# ==========================================================

def verificar_assassino():

    chance = random.randint(1, 10)

    # O assassino só aparece em algumas situações.
    if chance <= 2:

        return True

    return False


# ==========================================================
# CENA DE ENCONTRO ALEATÓRIO
# ==========================================================

def evento_assassino():

    print("""
============================================================
                 VOCÊ NÃO ESTÁ SOZINHO
============================================================

Um barulho vem do outro lado da sala.

Você olha lentamente.

Uma sombra passa pela porta.

Você percebe a máscara.

O assassino está perto.
""")

    state["assassino_alertado"] = True

    return "perseguicao"


# ==========================================================
# FIM DA PARTE 3
# ==========================================================


# ==========================================================
# PARTE 4
# FINAIS, ESCADAS E LOOP PRINCIPAL
# ==========================================================


# ==========================================================
# ESCADAS
# ==========================================================

def escadas():

    evento_terror()

    print("""
============================================================
                       ESCADAS
============================================================

Você está diante da enorme escadaria da mansão.

O andar de cima está completamente escuro.

Você pode ouvir o vento entrando pelas janelas.

Existem três caminhos:

1 - Subir para o sótão
2 - Descer para o porão
3 - Voltar para o hall
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3"]
    )

    if escolha == "1":

        return "sotao"

    elif escolha == "2":

        return "porao"

    else:

        return "hall"


# ==========================================================
# FINAL 1 - FUGA PELO PORTÃO
# ==========================================================

def fim_fuga():

    print("""
============================================================
                    FINAL 1
                 FUGA PELO JARDIM
============================================================

Você corre pelo jardim.

A chuva continua caindo.

Você chega ao enorme portão da propriedade.

Com a chave enferrujada em mãos...

CLIC!

O cadeado se abre.

Você atravessa o portão e corre pela estrada.

Depois de alguns minutos, encontra um carro passando.

O motorista para e chama a polícia.

Quando olha para trás...

A mansão está completamente escura.

Você sobreviveu.

Mas ninguém acredita quando você conta sobre
o homem mascarado.

                    🏆 FINAL BOM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL 2 - FUGA DE CARRO
# ==========================================================

def fim_carro():

    print("""
============================================================
                    FINAL 2
                 FUGA DE CARRO
============================================================

Você retorna para a garagem.

A caminhonete está esperando.

Você coloca a gasolina no tanque.

Depois coloca o fusível no sistema elétrico.

O motor faz um barulho.

*BRUM...*

Você tenta novamente.

*BRUUUM!*

A caminhonete liga.

Você acelera para fora da garagem.

O portão se abre lentamente.

Você olha pelo retrovisor.

O assassino está parado no meio da estrada.

Ele observa você desaparecer na tempestade.

Você conseguiu escapar.

                    🏆 FINAL BOM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL 3 - HERÓI
# ==========================================================

def fim_heroi():

    print("""
============================================================
                    FINAL 3
                   O HERÓI
============================================================

O assassino avança.

Você segura o machado.

Ele tenta impedir sua fuga.

Você consegue afastá-lo e corre para abrir
a saída da mansão.

Antes de fugir, você percebe Sarah escondida
no segundo andar.

Você poderia simplesmente escapar...

Mas decide voltar.

Você encontra Sarah e ajuda os dois a saírem
da mansão juntos.

Horas depois, a polícia chega.

A mansão é investigada.

Sarah finalmente está segura.

Você também.

                    🏆 FINAL BOM
============================================================
""")

    if state["sobrevivente_salvo"]:

        print("""
Você cumpriu sua promessa.

Sarah nunca esquecerá que você voltou para ajudá-la.
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL 4 - TÚNEL
# ==========================================================

def fim_tunel():

    print("""
============================================================
                    FINAL 4
                 O TÚNEL SECRETO
============================================================

Você atravessa o túnel escondido.

Cada passo parece durar uma eternidade.

Finalmente você vê a luz da lua.

Você sai no meio da floresta.

A mansão fica para trás.

Você corre sem olhar para trás.

Depois de horas caminhando, encontra uma estrada.

Um carro da polícia passa pelo local.

Você pede ajuda.

A polícia volta até a propriedade.

Mas quando chegam...

A mansão parece estar completamente abandonada.

Nenhum sinal do assassino.

Nenhuma pista.

Apenas uma máscara encontrada no chão.

                    🏆 FINAL BOM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL 5 - POLÍCIA
# ==========================================================

def fim_policia():

    print("""
============================================================
                    FINAL 5
                O PEDIDO DE SOCORRO
============================================================

Você consegue manter o rádio funcionando.

Uma voz responde:

"Equipe de resgate a caminho."

Você se tranca na sala de segurança.

Minutos depois...

SIRENES.

As portas da mansão são arrombadas.

Policiais entram no prédio.

Você finalmente está seguro.

Mas existe um problema.

O assassino desapareceu.

A polícia encontra apenas uma máscara
em um dos corredores.

O caso continua sem solução.

                    🏆 FINAL BOM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL 6 - VERDADEIRA HISTÓRIA
# ==========================================================

def fim_secreto():

    print("""
============================================================
                  FINAL SECRETO
                 A VERDADE DE BLACKWOOD
============================================================

Você reuniu todas as pistas.

O diário.

A fita VHS.

As fotografias.

Os documentos.

Tudo começa a fazer sentido.

Michael Blackwood não era apenas um assassino.

Ele era o antigo dono da mansão.

Anos atrás, sua família desapareceu.

Depois disso, Michael enlouqueceu e começou
a perseguir qualquer pessoa que entrasse
na propriedade.

A fita revela que ele criou túneis secretos
para observar todos os cômodos da casa.

Você percebe uma última coisa.

A polícia nunca encontrou o corpo dele.

Você pega as provas e consegue escapar.

Dias depois, a investigação é reaberta.

A verdade sobre a família Blackwood finalmente
vem à tona.

A mansão é interditada.

O caso se torna conhecido em todo o país.

E você é a única pessoa que conseguiu sobreviver
e revelar toda a história.

                  🏆 FINAL SECRETO
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL RUIM 1 - MORTE
# ==========================================================

def fim_morte():

    print("""
============================================================
                    FINAL RUIM
                  A ÚLTIMA NOITE
============================================================

Você já não consegue continuar.

Sua visão fica cada vez mais fraca.

Os passos do assassino se aproximam.

Você tenta encontrar uma saída...

Mas é tarde demais.

A mansão volta ao silêncio.

Na manhã seguinte, ninguém sabe
o que aconteceu com você.

A tempestade apaga qualquer sinal.

A casa continua esperando sua próxima vítima.

                    💀 FINAL RUIM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL RUIM 2 - PRESO NA MANSÃO
# ==========================================================

def fim_preso():

    print("""
============================================================
                    FINAL RUIM
                 PRESO PARA SEMPRE
============================================================

Você procura uma saída durante horas.

Cada porta leva a outro corredor.

Cada corredor parece igual.

A mansão parece não ter fim.

Você finalmente percebe que está perdido.

O amanhecer chega.

Mas você continua dentro da casa.

Dias passam.

Ninguém vem.

A mansão permanece em silêncio.

Você nunca consegue encontrar a saída.

                    💀 FINAL RUIM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL RUIM 3 - CARRO SEM SAÍDA
# ==========================================================

def fim_carro_ruim():

    print("""
============================================================
                    FINAL RUIM
                  SEM COMBUSTÍVEL
============================================================

Você consegue chegar até a caminhonete.

Entra rapidamente.

Gira a chave.

Nada.

Você tenta novamente.

Nada.

Então percebe que o tanque está vazio.

Um som surge atrás da garagem.

Passos.

Você olha pelo retrovisor.

A figura mascarada está se aproximando.

Você não tem para onde fugir.

                    💀 FINAL RUIM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL RUIM 4 - ARMADILHA
# ==========================================================

def fim_armadilha():

    print("""
============================================================
                    FINAL RUIM
                   A ARMADILHA
============================================================

Você encontra uma porta que parece levar
para fora da mansão.

Você entra.

A porta fecha automaticamente.

Você tenta abrir.

Está trancada.

As luzes se apagam.

Você percebe que aquilo não era uma saída.

Era uma armadilha.

                    💀 FINAL RUIM
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# FINAL ESPECIAL - SOBREVIVENTE
# ==========================================================

def fim_sobrevivente():

    print("""
============================================================
                  FINAL ESPECIAL
                 DOIS SOBREVIVENTES
============================================================

Você encontrou Sarah no sótão.

Em vez de abandoná-la, decidiu ajudá-la.

Vocês encontram uma passagem escondida.

Depois de uma longa caminhada pelo túnel,
os dois conseguem chegar até a floresta.

Ao amanhecer, uma equipe de resgate encontra vocês.

Sarah conta tudo o que aconteceu.

A polícia investiga a mansão.

Você finalmente está livre.

                    🏆 FINAL ESPECIAL
============================================================
""")

    mostrar_inventario()

    return "fim"


# ==========================================================
# VERIFICAÇÃO DO FINAL SECRETO
# ==========================================================

def verificar_final_secreto():

    itens = [
        "diario",
        "fita",
        "cartao seguranca",
        "chave mestra"
    ]

    for item in itens:

        if item not in state["inventario"]:

            return False

    return True


# ==========================================================
# CENA ESPECIAL DA SAÍDA
# ==========================================================

def saida_final():

    print("""
============================================================
                  POSSÍVEL SAÍDA
============================================================

Você encontrou uma porta que parece levar
para fora da mansão.

Antes de abrir, você percebe algumas coisas
escritas na parede:

"VOCÊ SABE A VERDADE?"

Talvez exista algo que ainda não descobriu.
""")

    print("""
1 - Abrir a porta
2 - Procurar mais pistas
3 - Voltar
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3"]
    )


    if escolha == "1":

        if verificar_final_secreto():

            return "fim_secreto"

        return "fim_fuga"


    elif escolha == "2":

        if verificar_final_secreto():

            print("""
Você percebe que reuniu todas as provas.

Agora entende o que aconteceu nesta casa.
""")

            return "fim_secreto"

        print("""
Você procura por mais pistas.

Mas não encontra nada.
""")

        return "hall"


    else:

        return "hall"


# ==========================================================
# DICIONÁRIO DE CENAS
# ==========================================================

cenas = {

    # Cenas principais
    "inicio": inicio,
    "hall": hall,
    "cozinha": cozinha,
    "biblioteca": biblioteca,
    "banheiro": banheiro,
    "escritorio": escritorio,
    "escadas": escadas,
    "garagem": garagem,
    "porao": porao,
    "sotao": sotao,
    "jardim": jardim,

    # Cenas especiais
    "seguranca": seguranca,
    "tunel": tunel,
    "perseguicao": perseguicao,
    "combate": combate,
    "encontro_assassino": encontro_assassino,
    "evento_assassino": evento_assassino,
    "usar_radio": usar_radio,
    "examinar_fita": examinar_fita,
    "saida_final": saida_final,

    # Finais bons
    "fim_fuga": fim_fuga,
    "fim_carro": fim_carro,
    "fim_heroi": fim_heroi,
    "fim_tunel": fim_tunel,
    "fim_policia": fim_policia,
    "fim_secreto": fim_secreto,
    "fim_sobrevivente": fim_sobrevivente,

    # Finais ruins
    "fim_morte": fim_morte,
    "fim_preso": fim_preso,
    "fim_carro_ruim": fim_carro_ruim,
    "fim_armadilha": fim_armadilha
}


# ==========================================================
# MENU DE UTILIDADES
# ==========================================================

def menu_utilidades():

    print("""
============================================================
                     MENU
============================================================

1 - Ver inventário
2 - Ver status
3 - Usar kit médico
4 - Usar lanterna
5 - Usar rádio
6 - Continuar
""")

    escolha = escolher(
        "\nEscolha: ",
        ["1", "2", "3", "4", "5", "6"]
    )


    if escolha == "1":

        mostrar_inventario()

        input("\nPressione ENTER para continuar...")

        return "menu"


    elif escolha == "2":

        mostrar_status()

        input("\nPressione ENTER para continuar...")

        return "menu"


    elif escolha == "3":

        usar_kit()

        input("\nPressione ENTER para continuar...")

        return "menu"


    elif escolha == "4":

        usar_lanterna()

        input("\nPressione ENTER para continuar...")

        return "menu"


    elif escolha == "5":

        return usar_radio()


    return "continuar"


# ==========================================================
# INÍCIO DO JOGO
# ==========================================================

print("""
============================================================
                  THE BLACKWOOD HOUSE
============================================================

                 🔪 JOGO DE TERROR 🔪

                 Você sobreviverá?
============================================================
""")


input("Pressione ENTER para começar...")


# ==========================================================
# LOOP PRINCIPAL
# ==========================================================

cena = "inicio"


while cena != "fim":

    # ------------------------------------------------------
    # Verificação de vida
    # ------------------------------------------------------

    if state["vida"] <= 0:

        cena = "fim_morte"


    # ------------------------------------------------------
    # Executar cena atual
    # ------------------------------------------------------

    else:

        if cena not in cenas:

            print("\n⚠️ Erro: cena não encontrada:", cena)

            cena = "fim"

        else:

            cena = cenas[cena]()


    # ------------------------------------------------------
    # Verificação de finais
    # ------------------------------------------------------

    if cena == "fim":

        break


print("""
============================================================
                     FIM DE JOGO
============================================================

Obrigado por jogar THE BLACKWOOD HOUSE.

Você conseguiu sobreviver?

Descubra todos os finais para descobrir
toda a história da mansão.

============================================================
""")