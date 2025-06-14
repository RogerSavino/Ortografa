import pyttsx3
import random
import time
import os

#-----------------------------------------------------------PALAVRAS---------------------------------------------------------------------------
# Lista de palavras difíceis
palavras_dificeis = [
    # Palavras originais
    'cessão', 'circuito', 'analisador', 'dificuldade', 'zoológico', 
    'transição', 'associação', 'obscuro', 'conhecimento', 'licença', 
    'exceção', 'necessário', 'cachorrice', 'reconhecimento', 'sussurro',
    'abissal', 'acessório', 'acidente', 'adequação', 'afinidade', 
    'assassínio', 'atuação', 'avaliação', 'balança', 'barragem', 
    'cabelereiro', 'cachorro', 'caminhão', 'canalização', 'caminho',
    'característica', 'censura', 'cerâmica', 'cicatriz', 'circulação', 
    'civilização', 'concessão', 'confusão', 'conquista', 'constituição',
    'contradição', 'convivência', 'coração', 'crescimento', 'curiosidade',
    'deficiência', 'distorção', 'divisão', 'emergente', 'encenação', 
    'energia', 'engenharia', 'enunciado', 'ensino', 'entendimento', 
    'escolar', 'especificação', 'estabilidade', 'exigência', 'exploração',
    'extensão', 'fascinação', 'fenômeno', 'filosofia', 'formação',
    'fraqueza', 'freguesia', 'fundamental', 'geometria', 'governança',
    'gravidade', 'herança', 'incapacidade', 'implicação', 'inclusão',
    'indicação', 'inflação', 'inflexão', 'informação', 'instrução',
    'interessante', 'intolerância', 'introdução', 'invencibilidade',
    'irregularidade', 'limitação', 'necessidade', 'obsessão', 'observação',
    'ofensa', 'opção', 'organização', 'oposição', 'possibilidade', 
    'própria', 'quarteirão', 'relevância', 'reflexão', 'renascimento', 
    'repressão', 'revisão', 'sensacional', 'silêncio', 'simplificação',
    'situação', 'socialização', 'sofisticação', 'suficiência', 
    'superação', 'suspensão', 'transmissão', 'unificação', 'verificação', 
    'vigilância', 'violência', 'zoologia', 'zecaterezinha', 'zona',
    'zonzo', 'zumbido', 'aerossol', 'aguentar', 'além', 'antigamente',
    'aparelho', 'assédio', 'atende', 'atualizar', 'bacilo', 'balança',
    'cabo', 'cachorrada', 'câmara', 'carnê', 'cativar', 'cemitério',
    'censurado', 'certeza', 'cidadão', 'cidade', 'condição', 'conserto',
    'consideração', 'corrigir', 'correto', 'decorrer', 'definição',
    'demonstrar', 'descrição', 'desenvolvimento', 'diferente', 'dilema',
    'dicionário', 'embora', 'exigente', 'evolução', 'fácil', 'falecido',
    'fantástico', 'febre', 'ficar', 'físico', 'futuro', 'gênero', 'governo',
    'guerra', 'hábito', 'horizonte', 'ignorância', 'importante',
    'inscrição', 'iniciar', 'inteligente', 'lembrete', 'líder', 'lógico',
    'luta', 'máquina', 'matéria', 'melhor', 'minoria', 'nação',
    'obrigado', 'ocorrência', 'orçamento', 'preocupação', 'privilégio',
    'projeto', 'quarto', 'recibos', 'reconhecer', 'rejeição', 'resposta',
    'revolução', 'rodízio', 'ruim', 'separação', 'seriedade', 'simplificar',
    'sucesso', 'suficiente', 'tolerância', 'tornar', 'tradição', 'triste',
    'tropical', 'unidade', 'vencer', 'vigilante', 'vulnerabilidade',
    'você', 'xícara', 'zero',
    # Palavras novas
    'abdução', 'abolição', 'absorção', 'abstenção', 'aclamação', 'acolhimento',
    'admissão', 'aflição', 'aglomeração', 'alucinação', 'ampliação',
    'animação', 'aparição', 'apreensão', 'aproximação', 'ascensão',
    'autorização', 'celebração', 'clarificação', 'classificação', 'coerção',
    'colisão', 'colocação', 'comissão', 'compreensão', 'conclusão', 'condução',
    'confecção', 'conjunção', 'consolidação', 'construção', 'consulta',
    'contenção', 'contratação', 'contribuição', 'convenção', 'conversão',
    'correção', 'criação', 'declaração', 'dedução', 'deflexão',
    'deliberação', 'demonstração', 'denominação', 'denúncia', 'depreciação',
    'descrença', 'destruição', 'determinação', 'difamação', 'diminuição',
    'discussão', 'disposição', 'distração', 'educação', 'eliminação',
    'emissão', 'encriptação', 'enfermidade', 'enfraquecimento', 'enriquecimento',
    'escassez', 'escravidão', 'estagnação', 'exaltação', 'expropriação',
    'extinção', 'falsificação', 'ficção', 'flutuação', 'formatação',
    'formulação', 'frustração', 'generosidade', 'glorificação',
    'gratificação', 'honestidade', 'identificação', 'ilustração', 'imposição',
    'iniciação', 'inovação', 'inquietação', 'insatisfação', 'instalação',
    'integração', 'intenção', 'interrupção', 'introspecção', 'justificação',
    'legislação', 'liquidação', 'localização', 'manifestação', 'medicação',
    'menção', 'mobilização', 'modificação', 'motivação', 'mudança',
    'multiplicação', 'mutação', 'negociação', 'notificação', 'nutrição',
    'obrigação', 'omissão', 'orientação', 'oxidação', 'paralisação',
    'participação', 'percepção', 'pergunta', 'perseguição', 'perturbação',
    'pessimismo', 'precaução', 'precipitação', 'predição', 'prescrição',
    'pressuposição', 'prevenção', 'proibição', 'promoção', 'proporção',
    'prossecução', 'proteção', 'provocação', 'radiação', 'realização',
    'recepção', 'recompensação', 'recuperação', 'redação', 'redução',
    'reformulação', 'regeneração', 'regulação', 'relutância', 'renovação',
    'resolução', 'ressurreição', 'restrição', 'retenção', 'retribuição',
    'reunião', 'reutilização', 'revogação', 'satisfação', 'selecção',
    'simulação', 'solidificação', 'solução', 'substituição', 'supervisão',
    'suposição', 'tentação', 'transformação', 'transgressão',
    'transportação', 'ultrapassagem', 'utilização', 'valorização',
    'vibração', 'visitação', 'vocação', 'votação', 'zoação'
]

palavras_grupo1 = [
    # Palavras originais
    'seção', 'circuito', 'analisador', 'dificuldade', 'zoológico', 
    'transição', 'associação', 'obscuro', 'conhecimento', 'licença',   
]

palavras_grupo2 = [
    # Palavras originais
    'exceção', 'necessário', 'cachorrice', 'reconhecimento', 'sussurro',
    'abissal', 'acessório', 'acidente', 'adequação', 'afinidade', 
    'assassínio', 'atuação', 'avaliação', 'balança', 'barragem', 
    'cabelereiro', 'cachorro', 'caminhão', 'canalização', 'caminho',   
]

palavras_grupo3 = [
    # Palavras originais
    'característica', 'censura', 'cerâmica', 'cicatriz', 'circulação', 
    'civilização', 'concessão', 'confusão', 'conquista', 'constituição',
    'contradição', 'convivência', 'coração', 'crescimento', 'curiosidade',
    'deficiência', 'distorção', 'divisão', 'emergente', 'encenação', 
    'energia', 'engenharia', 'enunciado', 'ensino', 'entendimento', 
    'escolar', 'especificação', 'estabilidade', 'exigência', 'exploração',   
]

palavras_grupo_s = [
    
    # S entre vogais (som de z)
        "casa", "mesa", "coisa", "vaso", "uso", "riso", "caso", "museu", "acusar", "pesar",
        "desejo", "casar", "nascido", "usar", "miséria", "pesquisa", "camisa", "tesoura",
        "surpresa", "música", "rosa", "gasolina", "fusível", "prazeroso", "frase", "risada",
        "paisagem", "aviso", "improviso", "análise", "crise", "empresa", "presença", "rastro",
        "peso", "prazer", "lesão", "resíduo", "razão", "tese", "resenha", "base", "fase",
        "causa", "misógino", "caso", "visar", "liso", "piso", "desenho", "desenrolar",
        "desarmar", "desatar", "desgaste", "desleixo", "deslizar",

        # Verbos derivados de radicais com S (mantêm o S)
        "analisar", "avisar", "improvisar", "alisar", "pisar", "pesquisar",
        "revisar", "causar", "pesar", "visar", "brilhar", "amassar", "passar", "cansar",
        "abusar", "abusar", "dispensar", "desistir", "assistir", "avisar", "expressar",

        # Adjetivos/substantivos terminados em -oso/-osa (som de z)
        "gostoso", "vistoso", "saboroso", "melindroso", "curioso", "talentoso",
        "famoso", "precioso", "duvidoso", "venenoso", "perigoso", "generosa",
        "vaidosa", "corajosa", "vitoriosa", "religiosa", "nervosa", "glamourosa",
        "desonesto", "desumano", "desleal", "hospedoso", "formoso", "amoroso",

        # Substantivos e adjetivos terminados em -ese/-esa (com s)
        "português", "portuguesa", "francês", "francesa", "inglesa",
        "japonês", "japonesa", "senegalês", "senegalesa", "escocês", "escocesa",
        "camponês", "camponesa", "burguês", "burguesa",

        # Palavras homófonas com Z (forma com S)
        "coser", "nós", "trás", "riscar", "pesar", "despesa", "respirar", "possível", "respeito",
        "risco", "resistir", "resina", "resumo", "restar", "resenha", "resposta", "rasgar", "raspador",

        # Outros comuns com s e som z
        "desenho", "desdobrar", "desligar", "desmazelo", "despejar", "desprezar",
        "disse", "disso", "dissecar", "desse", "desses", "disseminar", "dissecação"  
]

palavras_grupo_z = [

    # Substantivos comuns com Z
    "zebra", "zero", "zíper", "zagueiro", "zona", "zumbi", "zelo", "ziguezague", "zangado", "zanga",
    "zumba", "zodíaco", "zepelim", "zoeira", "zoológico", "zumbido", "zircônio", "zinco", "zênite",

    # Adjetivos com Z
    "zeloso", "zonzo", "zangado", "zombeteiro", "zombador", "zulu", "zombado",

    # Verbos com Z
    "zelar", "zangar", "zumbar", "ziguezaguear", "zoar", "zumbir", "zarpar", "zerar", "zombar",

    # Palavras com Z no meio
    "beleza", "natureza", "riqueza", "firmeza", "certeza", "rapidez", "gentileza", "destreza",
    "esperteza", "dureza", "aspereza", "tristeza", "frieza", "clareza", "moleza", "nobreza",

    # Palavras terminadas em -ez ou -eza (sempre com Z)
    "rapidez", "solidez", "timidez", "lucidez", "pequenez", "insensatez", "estupidez",
    "altivez", "sensatez", "honradez",

    # Palavras com sufixo -izar (formadas a partir de adjetivos ou substantivos)
    "civilizar", "atualizar", "realizar", "modernizar", "popularizar", "organizar", "oficializar",
    "fiscalizar", "socializar", "generalizar", "moralizar", "finalizar", "legalizar",

    # Palavras de origem estrangeira com Z
    "pizza", "blitz", "jazz", "quiz", "quizumba", "freezer", "lazer", "diesel", "bronze"
]

#-------------------------------------------------------------------------------------------------------------------------------------------
# Função para limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fala a palavra
def falar_palavra(palavra):
    engine = pyttsx3.init()
    engine.say(palavra)
    engine.runAndWait()

# Verifica ortografia
def verificar_ortografia(correta, digitada):
    return correta == digitada


#-----------------------------------------------------------JOGO---------------------------------------------------------------------------
# Loop principal do jogo
def jogar_total():
    cont = 0
    while True:
        palavra = random.choice(palavras_dificeis)
        limpar_tela()
        print(f"\nNível: {cont}")
        print("Ouça a palavra...\n")
        falar_palavra(palavra)
        
        tentativa = input("Digite a palavra que você ouviu: ").strip().lower()
        
        if verificar_ortografia(palavra, tentativa):
            cont += 1
            print("✔️  Correto! Parabéns!\n")
            time.sleep(1)
        else:
            print("❌  Errado! A palavra correta era:")
            print(f"\n ---> {palavra} <---\n")
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            limpar_tela()
            print(f"\n🔚 Fim de jogo. Sua pontuação foi: {cont}\n")
            break
            

def jogar1():
    cont = 0
    while True:
        palavra = random.choice(palavras_grupo1)
        limpar_tela()
        print(f"\nNível: {cont}")
        print("Ouça a palavra...\n")
        falar_palavra(palavra)
        
        tentativa = input("Digite a palavra que você ouviu: ").strip().lower()
        
        if verificar_ortografia(palavra, tentativa):
            cont += 1
            print("✔️  Correto! Parabéns!\n")
            time.sleep(1)
        else:
            print("❌  Errado! A palavra correta era:")
            print(f"\n ---> {palavra} <---\n")
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            limpar_tela()
            print(f"\n🔚 Fim de jogo. Sua pontuação foi: {cont}\n")
            break

def jogar2():
    cont = 0
    while True:
        palavra = random.choice(palavras_grupo2)
        limpar_tela()
        print(f"\nNível: {cont}")
        print("Ouça a palavra...\n")
        falar_palavra(palavra)
        
        tentativa = input("Digite a palavra que você ouviu: ").strip().lower()
        
        if verificar_ortografia(palavra, tentativa):
            cont += 1
            print("✔️  Correto! Parabéns!\n")
            time.sleep(1)
        else:
            print("❌  Errado! A palavra correta era:")
            print(f"\n ---> {palavra} <---\n")
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            limpar_tela()
            print(f"\n🔚 Fim de jogo. Sua pontuação foi: {cont}\n")
            break

def jogar3():
    cont = 0
    while True:
        palavra = random.choice(palavras_grupo3)
        limpar_tela()
        print(f"\nNível: {cont}")
        print("Ouça a palavra...\n")
        falar_palavra(palavra)
        
        tentativa = input("Digite a palavra que você ouviu: ").strip().lower()
        
        if verificar_ortografia(palavra, tentativa):
            cont += 1
            print("✔️  Correto! Parabéns!\n")
            time.sleep(1)
        else:
            print("❌  Errado! A palavra correta era:")
            print(f"\n ---> {palavra} <---\n")
            tentativa = input("Digite a corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            limpar_tela()
            print(f"\n🔚 Fim de jogo. Sua pontuação foi: {cont}\n")
            break

def jogarS():
    cont = 0
    while True:
        palavra = random.choice(palavras_grupo_s)
        limpar_tela()
        print(f"\nNível: {cont}")
        print("Ouça a palavra...\n")
        falar_palavra(palavra)
        
        tentativa = input("Digite a palavra que você ouviu: ").strip().lower()
        
        if verificar_ortografia(palavra, tentativa):
            cont += 1
            print("✔️  Correto! Parabéns!\n")
            time.sleep(1)
        else:
            print("❌  Errado! A palavra correta era:")
            print(f"\n ---> {palavra} <---\n")
            tentativa = input("Digite a corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            limpar_tela()
            print(f"\n🔚 Fim de jogo. Sua pontuação foi: {cont}\n")
            break

def jogarZ():
    cont = 0
    while True:
        palavra = random.choice(palavras_grupo_z)
        limpar_tela()
        print(f"\nNível: {cont}")
        print("Ouça a palavra...\n")
        falar_palavra(palavra)
        
        tentativa = input("Digite a palavra que você ouviu: ").strip().lower()
        
        if verificar_ortografia(palavra, tentativa):
            cont += 1
            print("✔️  Correto! Parabéns!\n")
            time.sleep(1)
        else:
            print("❌  Errado! A palavra correta era:")
            print(f"\n ---> {palavra} <---\n")
            tentativa = input("Digite a corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            tentativa = input("Digite a palavra corretamente: ").strip().lower()
            limpar_tela()
            print(f"\n🔚 Fim de jogo. Sua pontuação foi: {cont}\n")
            break

#-----------------------------------------------------------REGRAS---------------------------------------------------------------------------

def Regra_s():
    while True:
        limpar_tela()
        print("✅ Regras para o uso do S\n")
        print("1 - Palavras que indicam origem, nacionalidade ou título terminadas em -ês/-esa:")
        print("    Ex.: português, portuguesa, francês, francesa, japonês, japonesa.\n")

        print("2 - Palavras com o prefixo des-:")
        print("    Mesmo quando esse prefixo é seguido por vogais, o S se mantém.")
        print("    Ex.: desamor, desigual, desonra, desunir, desinibido.\n")

        print("3 - Palavras terminadas em -oso/-osa, -ase, -ese, -isa, -ose (geralmente adjetivos):")
        print("    Ex.: gostoso, rosa, brisa, tese, camisa, metamorfose.")
        print("    ⚠️  Exceções com Z: gaze, baliza, doze, gozo, treze, ojeriza.\n")

        print("4 - Formas conjugadas dos verbos “querer” e “pôr” (e derivados):")
        print("    Ex.: quis, pusesse, compuseram, impuseram, propuseram.\n")

        print("5 - Verbos derivados de palavras com S no radical:")
        print("    O S permanece no verbo.")
        print("    Ex.: análise → analisar    aviso → avisar    piso → pisar")
        print("    ⚠️  Atenção: verbos com o sufixo -izar são escritos com Z,")
        print("    como atualizar, organizar, realizar — desde que o radical não tenha S ou I.\n")

        op = input("Deseja voltar? (sim/não): ").strip().lower()
        if op in ['sim', 's']:
            limpar_tela()
            break
        elif op in ['não', 'nao', 'n']:
            print("Ok, permanecendo na tela...")
        else:
            print("Resposta inválida. Tente novamente.")

def Regra_z():
    while True:
        limpar_tela()
        print("✅ Regras para o uso do Z\n")
        
        print("1 - Substantivos abstratos terminados em -ez/-eza:")
        print("    Ex.: avareza, beleza, certeza, nobreza, sensatez, tristeza, estupidez.\n")

        print("2 - Verbos terminados com o sufixo -izar:")
        print("    Usado para formar verbos a partir de substantivos/adjetivos.")
        print("    Ex.: atualizar, realizar, organizar, hostilizar, utilizar.\n")

        print("3 - Substantivos terminados em -ização:")
        print("    Substantivos formados a partir de verbos com -izar.")
        print("    Ex.: atualização, realização, organização, sistematização.\n")

        print("4 - Palavras homófonas com S e Z (mesmo som, escrita diferente):")
        print("    → coser (S): costurar       ×       cozer (Z): cozinhar")
        print("    → nós (S): pronome          ×       noz (Z): semente")
        print("    → trás (S): posição         ×       traz (Z): verbo trazer\n")

        op = input("Deseja voltar? (sim/não): ").strip().lower()
        if op in ['sim', 's']:
            limpar_tela()
            break
        elif op in ['não', 'nao', 'n']:
            print("Ok, permanecendo na tela...")
        else:
            print("Resposta inválida. Tente novamente.")


# Menu principal
def menu():
    while True:
        print("===================================================================")
        print("|                            Ortográfa                            |")
        print("===================================================================")
        print("| 1 - Começar Jogo sem fim                                        |")
        print("| 2 - Começar Jogo com ( 10 palavras )                            |")
        print("| 3 - Começar Jogo com ( 20 palavras )                            |")
        print("| 4 - Começar Jogo com ( 30 palavras )                            |")
        print("|                                                                 |")
        print("| 5 - Regras de quando usar (S)                                   |")
        print("| 6 - Treinar palavras com (S)                                    |")
        print("|                                                                 |")
        print("| 7 - Regras de quando usar (Z)                                   |")
        print("| 8 - Treinar palavras com (Z)                                    |")
        print("|                                                                 |")
        print("| 10 - Sair                                                       |")
        print("===================================================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            jogar_total()
        elif escolha == '2':
            jogar1()
        elif escolha == '3':
            jogar2()
        elif escolha == '4':
            jogar3()
        elif escolha == '5':
            Regra_s()
        elif escolha == '6':
            jogarS()
        elif escolha == '7':
            Regra_z()
        elif escolha == '8':
            jogarZ()
        elif escolha == '10':
            print("Até logo!")
            break

            
        
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)
            limpar_tela()

# Iniciar o programa
if __name__ == "__main__":
    menu()
