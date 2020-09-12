#http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm
import string
import random
import sys

def poloativo():

    while True:
        print('Digite "pj" ou "pf" para responder:')
        tipopautora = input('A parte autora é Pessoa Jurídica ou Pessoa Física? ')

        if tipopautora == 'pj' :
            tipopautora = 'Pessoa Jurídica'
            print('Documentos necessários à propositura da ação como Pessoa Jurídica:')
            print('Petição Inicial; Procuração assinada por representante;')
            print('Contrato Social; Documentos necessários à sustentação do Pedido (art. 434 do CPC).')
            print('As formalidades de redação da petição inicial podem ser verificadas nos artigos 319 e 320 do CPC.')
            print('Para fins de noção de modelo de petição inicial, o Google pode ser uma boa ferramenta.')
            return ('Tudo ok com os documentos de protocolo para {}, certo?'.format(tipopautora))

        elif tipopautora == 'pf' :
            tipopautora = 'Pessoa Física'
            print('Documentos necessários à propositura da ação como Pessoa Física:')
            print('Petição Inicial; Procuração assinada pela parte;')
            print('Documento Identificação da parte; Documentos necessários à sustentação do Pedido (art. 434 do CPC).')
            print('As formalidades de redação da petição inicial podem ser verificadas nos artigos 319 e 320 do CPC.')
            print('Para fins de noção de modelo de petição inicial, o Google pode ser uma boa ferramenta.')
            return ('Tudo ok com os documentos de protocolo para {}, certo?'.format(tipopautora))

        else:
            print('Digite somente as letras "pj" ou "pf" e aperte "enter"')

def procedimentoprotocoloinicial():

    print('Hora de protocolar a petição inicial!')
    print('Digite "1" para protocolar a petição inicial com pedido liminar, e "0" para protocolar sem pedido liminar')

    while True:
        inicial = input('Protocolo petição inicial: ')

        try:
            tipoinicial = int(inicial)
            if tipoinicial == 1:
                print('Você protocolou a inicial com pedido liminar')
                liminar = 1
                return liminar

            elif tipoinicial == 0:
                print('Você protocolou a inicial sem pedido liminar')
                liminar = 0
                return liminar

            else:
                print('Erro, favor inserir valor "1" para liminar, e "0" para sem liminar')

        except:
            print('Erro, favor inserir valor numérico 1 para liminar, e 0 para sem liminar')

def concl1semlim():

    while True:

        print('Autos conclusos para despacho.')
        print('Dessa conclusão, o juízo pode decidir por:')
        print('a) Improcedência liminar do pedido - art. 332 caput e §1º (prescrição ou decadência) do CPC')
        print('b) Determinação de emenda à inicial - art. 321 do CPC')
        print('c) Indeferimento da petição inicial - art. 330 e 321, §1º, do CPC')
        print('d) Determinação da citação de réu(s), e designação de audiência de conciliação ou mediação* - art. 334 do CPC')
        Conclusão1 = input('Para explorar cada uma das alternativas, digite a letra correspondente: ')

        try:
            Conclusão1 = int(Conclusão1)
            print('Erro, favor inserir valor na forma das letras "a", "b", "c", ou "d",')
            print('para escolher entre as opções de alternativas da primeira conclusão.')

        except:
            if Conclusão1 == "a":
                print('Que coisa ruim, foi decidido pela improdedência liminar do pedido da parte {}'.format(pautora))
                print('Discutivelmente, essa é o pior retorno para uma petição nesse momento processual.')
                print('Da improcedência liminar do pedido cabe apelação, nos termos deo art. 332, § 2º do CPC')
                print('O indeferimento liminar do pedido nada mais significa que o indeferimento na condição de')
                print('inaudita altera pars, ou seja, sem que se escute a parte contrária.')
                print('Os motivos pelos quais a improcedência liminar do pedido estão previstos nos incisos do')
                print('caput do art. 332 do CPC, na forma de rol taxativo.')
                print('Como cabe recurso (de apelação) da decisão, e temos a situação de rol taxativo,')
                print('interessante observar a aplicação (ou erro de aplicação) dos dispositivos alternativos.')
                print('O juízo que proferiu a decisão de improcedência liminar do pedido pode')
                print('se retratar no prazo de 5 dias, nos termos do $3º do art. 332 do CPC.')
                print('Interessante notar que, caso o juízo a quo não se retrate, a citação do réu ocorre')
                print('para contrarrazoar no recurso, nos termos do art. 332 §4º do CPC.')
                print('Essa opção chegou em momento recursal, as funções recursais serão definidas')
                print('posteriormente no presente projeto.')
                return Conclusão1

            elif Conclusão1 == "b":
                print('Paciência, o juízo mandou emendar a inicial protocolada em nome de {}'.format(pautora))
                print('A determinação de emenda à inicial ocorre quando não são cumpridos os artigos 319 e 320 do CPC,')
                print('aqueles mesmos artigos que verificamos pouco tempo após indicar se estamos representando uma')
                print('pessoa física ou pessoa jurídica.')
                print('De fato, dessa decisão, a atitude mais simples de ser tomada pelo advogado é a de emendar a inicial,')
                print('como uma decisão da qual existem discussões sobre o cabimento de Agravo de')
                print('Instrumento (art. 1.021 do CPC), você não terá dificuldades de encontrar discussões')
                print('doutrináras e jurisprudenciais sobre o assunto.')
                print('No entanto, tenha em mente que existem jurisprudências deferindo agravos para esse fim,')
                print('uma pesquisa rápida por "recurso contra decisão que manda emendar a inicial" pode demonstrar isso.')
                print('Apesar disso, aqui vamos considerar que a petição foi emendada.')
                print('Cuidado, passar mais de uma vez por esse caminho em nosso programa, pode acarretar em')
                print('indeferimento da inicial (opção "c" desse menu), ou seja, na prática, pelo não cumprimento da ordem')
                print('de emenda da inicial, a petição deve ser indeferida.')

            elif Conclusão1 == "c":
                print('Que pena, foi indeferida a petição inicial de {}'.format(pautora))
                print('Do indeferimento da petição inicial, cabe apelação, nos termos do art. 331 do CPC.')
                print('Da mesma forma que para a improcedência, cabe retratação do juízo a quo no caso de')
                print('protocolo de apelação, no prazo de 5 dias (art. 331 caput do CPC).')
                print('Interessante notar que, caso o juízo a quo não se retrate, a citação do réu ocorre')
                print('para responder ao recurso, nos termos do art. 331 §1º do CPC.')
                print('Apesar de lidar com um deselvolvimento de rol taxativo (incisos do caput do art. 330) somado')
                print('à conceituação de inépcia (incisos do § 1º do art 330), se deve pensar nas formalidades')
                print('de adequação da decisão do juízo a quo ao rol taxativo, da mesma forma que no caso de')
                print('improcedência, para fins de redação do recurso de apelação.')
                print('Essa opção chegou em momento recursal, as funções recursais serão definidas')
                print('posteriormente no presente projeto.')
                return Conclusão1

            elif Conclusão1 == "d":
                print('Parabéns, a petição inicial em nome de {} foi recebida e foi ordenada a citação'.format(pautora))
                print('do pólo passivo!')
                print('Isso não significa que você tenha tido qualquer tipo de vitória processual, mas meramente que você')
                print('passou pelos outras três possibilidades de "contratempos/óbices" processuais.')
                print('A citação do pólo passivo (o/a/os/as réu/ré/réus/rés) segue as formalidades dos')
                print('arts 238 ao 259 do CPC.')
                return Conclusão1

            else:
                print('Erro, favor inserir valor em na forma das letras "a", "b", "c", ou "d",')
                print('para escolher entre as opções de alternativas da primeira conclusão.')

def citreu():

    print('A fase de citação é a fase a partir da qual o réu passa a fazer parte do processo,')
    print('a citação é o ato de chamá-lo para tanto.')

    while True:
        print('Digite "pj" ou "pf" para responder:')
        tipopre = input('A parte ré é Pessoa Jurídica ou Pessoa Física? ')

        if tipopre == 'pj' :
            tipopre = 'Pessoa Jurídica'
            print('Vamos então à citação!')
            print('No CPC, a citação é definida no art. 238, sendo o texto do artigo, literalmente:')
            print('"Citação é o ato pelo qual são convocados o réu, o executado ou o interessado para integrar')
            print('a relação processual."')
            print('A citação, na prática como no presente programa, só ocorre quando não há indeferimento, ou')
            print('improcedência liminar do pedido.')
            print('A citação é formalizada entre o artigo citado [238], e o artigo 259 no CPC.')
            print('O instituto da citação é de extrema importância para o estudo do Processo Civil,')
            print('não só por motivo de discussões sobre nulidade processual, mas também porque')
            print('conhecer esse instituto pode fazer diferença, por exemplo, no momento em que')
            print('não se consegue citar o réu pela via inicialmente eleita (normalmente correio), ou')
            print('para que sejam tomadas medidas para garantir que se encontre o réu em tempo hábil')
            print('para o cumprimento de decisões liminares.')
            return ('Réu {} citado'.format(tipopre))

        elif tipopre == 'pf' :
            tipopre = 'Pessoa Física'
            print('Vamos então à citação!')
            print('No CPC, a citação é definida no art. 238, sendo o texto do artigo, literalmente:')
            print('"Citação é o ato pelo qual são convocados o réu, o executado ou o interessado para integrar')
            print('a relação processual."')
            print('A citação, na prática como no presente programa, só ocorre quando não há indeferimento, ou')
            print('improcedência liminar do pedido.')
            print('A citação é formalizada entre o artigo citado [238], e o artigo 259 no CPC.')
            print('O instituto da citação é de extrema importância para o estudo do Processo Civil,')
            print('não só por motivo de discussões sobre nulidade processual, mas também porque')
            print('conhecer esse instituto pode fazer diferença, por exemplo, no momento em que')
            print('não se consegue citar o réu pela via inicialmente eleita (normalmente correio), ou')
            print('para que sejam tomadas medidas para garantir que se encontre o réu em tempo hábil')
            print('para o cumprimento de decisões liminares.')
            return ('Réu {} citado'.format(tipopre))

        else:
            print('Digite somente as letras "pj" ou "pf" e aperte "enter".')

def concioumed():

    print('A autocomposição, denominada "mediação", ou "conciliação",')
    print('é definida no art. 334 do CPC.')
    print('Chamaremos "mediação", e "conciliação" de autocomposição, para fins')
    print('práticos da presente função.')
    print('É hora de a parte autora {} e a parte ré {} decidirem sobre'.format(pautora, pre))
    print('autocomposição.')
    print('A nossa função para definir essa fase lida com três situações diferentes:')
    print('a) Partes manifestam o desinteresse em autocomposição (art. 334, §4º, I)')
    print('b) A causa não admite autocomposição (art. 334, §4º, II)')
    print('c) Ocorrência de audiência de conciliação (art. 334)')
    print('Lembre-se: a autocomposição, nos termos do inciso V do art. 139 do CPC,')
    print('pode ocorrer a qualquer momento no processo!')


    while True:
        autocompos = input('Insira a letra da opção que você deseja explorar: ')

        if autocompos == "a":
            autocompos = 'nem querem conversar'
            print('Note que é necessário considerar que as partes cumpriram com as')
            print('formalidades de manifestação do art. 334, §5º, tanto para parte autora')
            print('quanto para ré.')
            return autocompos

        elif autocompos == "b":
            autocompos = 'não é possível conversar'
            print('As causas que não admitem autocomposição são as que lidam com')
            print('direitos indisponíveis, que são literalmente direitos os quais o')
            print('direito brasileiro não permite disposição, não permite negociar:')
            print('(vida, liberdade, saúde e dignidade)')
            return autocompos

        elif autocompos == "c":
            print('Aqui acontece audiência de conciliação ou mediação!')
            print('Dessa audiência, pode ser decidido por conciliar ou não conciliar.')
            print('Para decidir pela autocomposição, digite "1". Caso contrário, digite "0"')

            while True:
                audienciaautocompos = input ('Você deseja conciliar? ')

                try:
                    audienciaautocompos = int(audienciaautocompos)

                    if audienciaautocompos == 1:
                        autocompos = 'Conversamos, deu certo!'
                        print('O processo teve resolução na forma de autocomposição!')
                        print('A partir desse momento, o processo vai concluso para homologação')
                        print('dos termos da autocomposição, e quando homologado, o processo é extinto')
                        print('com resolução do mérito (que significa: julgando a causa, e não por motivos formais),')
                        print('nos termos do art. 487, III do CPC')
                        return autocompos
                        
                    elif audienciaautocompos == 0:
                        autocompos = 'Conversamos, mas não deu certo.'
                        print('Quando não ocorre a autocomposição, o processo prossegue.')
                        return autocompos

                    else:
                        print('Erro, para decidir pela autocomposição, digite valor "1". Caso contrário, digite "0"')
                        
                except:
                    print('Erro, para decidir pela autocomposição, digite valor numérico "1". Caso contrário, digite "0"')

        else:
            print('Erro, favor inserir valor em na forma das letras "a", "b" ou "c",')
            print('para escolher entre as opções de alternativas sobre autocomposição.')

def manifestacaoreu1():

    print('O momento da primeira manifestação do réu apresenta cinco possíveis situações processuais.')
    print('Apesar disso, só serão apresentadas quatro alternativas como possibilidade de resposta do réu,')
    print('isso porque a opção de arguição de impedimento ou suspeição(arts. 144 a 148 do CPC), não ocorre')
    print('necessariamente nessa fase processual, e será definida posteriormente.')
    print('a) Apresentação de contestação, no prazo de 15 dias, nos termos do art. 335 do CPC;')
    print('b) Apresentação de contestação com reconvenção, nos termos do caput do art. 343 do CPC;')
    print('c) Apresentação de reconvenção sem a apresentação de contestação, nos termos do art. 343, § 6º, do CPC;')
    print('d) A falta de manifestação dentro do prazo, causando revelia, nos termos do art. 344 do CPC')

    while True:
        reacaoreu = input('Insira a letra da opção que você deseja explorar: ')

        if reacaoreu == 'a':
            print('A contestação é, na prática, a mais comum das manifestações de réus no procedimento comum.')
            print('O protocolo da contestação nada mais indica que a primeira manifestação do réu no')
            print('processo em si, ou seja, o primeiro ato do réu de se manifestar no sentido argumentativo de')
            print('intentar decisão judicial em seu favor (ele pode se manifestar antes, mas em situações recursais).')
            print('O protocolo da contestação dá ensejo à intimação do autor para réplica')
            return reacaoreu

        elif reacaoreu == 'b':
            print('A apresentação de contestação em conjunto com reconvenção, é o equivalente ao ato de responder')
            print('ao que o autor e ao mesmo tempo processá-lo nos autos do mesmo processo.')
            print('Isso só pode ser feito quando a pretensão em si, ou os fundamentos de defesa forem')
            print('conexos com o do processo em curso (art. 343, caput, do CPC.')
            print('Para tanto, vamos fazer uso da função de protocolo da petição inicial, note que')
            print('isso se dá também pelo fato de que a reconvenção precisa, além dos quesitos falados,')
            print('cumprir com os requisitos da petição inicial, do art. 319 do CPC.')
            print('Por esse motivo, a reconvenção pode vir com ou sem pedido liminar.')
            print('Importante a anotação de que a reconvenção deve ser protocolada na mesma peça da contestação.')
            reconv = str(procedimentoprotocoloinicial())
            return reacaoreu+reconv
        
        elif reacaoreu == 'c':
            print('A apresentação de reconvenção pode ser feita sem ser acompanhada de contestação.')
            print('Isso só pode ser feito quando a pretensão em si, ou os fundamentos de defesa forem')
            print('conexos com o do processo em curso (art. 343, caput, do CPC.')
            print('Para tanto, vamos fazer uso da função de protocolo da petição inicial, note que')
            print('isso se dá também pelo fato de que a reconvenção precisa, além dos quesitos falados,')
            print('cumprir com os requisitos da petição inicial, do art. 319 do CPC.')
            print('Por esse motivo, a reconvenção pode vir com ou sem pedido liminar.')
            print('Importante a anotação de que a reconvenção deve ser protocolada na mesma peça da contestação.')
            reconv = str(procedimentoprotocoloinicial())
            return reacaoreu+reconv
        
        elif reacaoreu == 'd':
            print('No caso de o réu se tornar revéu, o CPC prevê a aplicação da presunção de veracidade das')
            print('alegações formuladas pelo autor (art. 344 do CPC), excetuando-se os casos dos incisos do')
            print('art. 345 do CPC.')
            print('Caso não tenha constituído representante nos autos, vide art. 346 sobre o funcionamento dos')
            print('prazos para o réu na situação em questão.')
            return reacaoreu

        else:
            print('Erro, favor inserir valor em na forma das letras "a", "b", "c", ou "d",')
            print('para escolher entre as opções de alternativas da primeira manifestação do réu.')

def funcjulconfestproc():

    print('A função do julgamento conforme o estado do processo possui três alternativas que se desdobram')
    print('em caminhos diferentes que definem o processo, sendo elas:')
    print('a) A extinção do processo (art. 354 do CPC), que pode ser com ou sem resolução do mérito*;')
    print('b) O julgamento parcial do mérito (art. 356);')
    print('c) O julgamento com resolução do mérito (art. 355)')
    print('d) O despacho saneador (art. 357).')

    while True:
        despachojulconfestproc = input('Insira a letra da opção que você deseja explorar: ')
        
        if despachojulconfestproc == 'a':
            print('A extinção do processo nos termos dessa opção pode ocorrer em duas situações diferentes,')
            print('quando não julgar o mérito (art. 485), e quando julgar o mérito em decorrência de')
            print('decadência ou prescrição,(art. 487, II), ou no caso de homologação das possibilidades')
            print('das alíneas do inciso III do art, 487.')
            print('É importante notar que os casos de extinção do processo se diferenciam do julgamento do')
            print('em decorrência de manifestação das partes no sentido concordância em relação à resolulção')
            print('do mérito, ou seja, quando se trata de uma conclusão natural da situação processual, e não')
            print('de um "julgamento" de fato.')
            print('Desse despacho, podem ocorrer recursos, o fim do processo, ou eventual cumprimento de sentença')
            print('de transações cuja obrigação de alguma das partes não seja cumprida')
            return despachojulconfestproc

        elif despachojulconfestproc == 'b':
            print('O julgamento parcial do mérito, nos termos do art. 356 do CPC, como o próprio nome define,')
            print('é um julgamento que deixa de julgar o processo como um todo (ou o total dos pedidos),')
            print('julgando somente alguns pedidos, ou parcialmente algum pedido em si.')
            print('Sobre essa decisão, é importante notar como os parágrafos do art. 356 definirão o decorrer')
            print('do processo a partir desse ponto, tanto na esfera recursal, como em termos de execução da')
            print('decisão aqui prolatada.')
            print('Nos termos do §2º do art. 356, a obrigação reconhecida nessa decisão pode ser executada')
            print('provisoriamente, independente de caução e apesar de recurso interposto pela parte (caso a')
            print('parte não protocole recurso, a execução será definitiva).')
            print('Em suma, anote-se que a presente opção coloca situação simultânea de continuidade do procedimento')
            print('comum para parte do processo, e início do cumprimento de sentença e fase recursal para outra')
            print('parte do processo (dos pedidos)')
            print('A parte que não foi objeto do julgamento do mérito continuará no procedimento comum, de forma que,')
            print('para os efeitos do presente desenvolvimento, o retorno da presente opção será o mesmo retorno do')
            print('despacho saneador (b). Consulte a opção do despacho no presente código ou o art. 357 do CPC')
            despachojulconfestproc = 'd'
            return despachojulconfestproc

        elif despachojulconfestproc == 'c':
            print('O julgamento antecipado do mérito (o "não parcial", no caso da opção em que estamos), ocorre em')
            print('situações nas quais é possível verificar a falta de necessidade de produção probatória (ou de')
            print('requerimento para tanto), como é possível verificar nos dois incisos do art. 355 do CPC.')
            print('Dessa opção, o processo pode se direcionar para o trânsito em julgado, ou para a fase recursal.')
            return despachojulconfestproc

        elif despachojulconfestproc == 'd':
            print('O despacho saneador é o despacho que serve à "organização" do processo para a construção do contexo')
            print('no qual serão definidas as regras de ônus de prova, resolvidas as questões processuais, delimitadas')
            print('as questões de direito e os meios de prova admitidos, e será designada a audiência de instrução')
            print('caso se faça necessário, tudo de acordo com os incisos do art. 357 do CPC.')
            print('Sobre o despacho saneador, vide as situações do art. 357 1º (sobre solicitação de ajustes e estabilização),')
            print('a possibilidade de apresentação de negociação sobre o saneamento, e a homologação dessa')
            print('negociação (art. 357, §2º), bem como a situação de saneamento na qual ele pode ocorrer por meio de audiência')
            print('(art. 357, §3º e parágrafos seguintes)')
            return despachojulconfestproc

        else:
            print('Erro, favor inserir valor em na forma das letras "a", "b", "c" ou "d"')
            print('para escolher entre as opções de alternativas sobre autocomposição.')

def instruc ():

    print('A audiência de instrução (e julgamento) é regida pelos artigos 358 ao artigo 368 do CPC.')
    print('É importante notar que a prova testemunhal, personagem principal da')
    print('audiência de instrução, é regida pelos artigos 442 ao 463 do CPC.')
    print('A sentença pode ser prolatada em audiência, nos termos do art. 367 do CPC, ou')
    print('no prazo de 30 dias, nos termos do art. 226, III do CPC - note-se que esse')
    print('prazo raramente é algo sequer cobrado por qualquer das partes, ever.')
    print('A sentença (arts. 485 e 487) é um elemento de variáveis que será definido no ato de')
    print('desenvolvimento das versões do presente código nas quais serão apresentadas as')
    print('possibilidades e estruturas recursais a partir das sentenças.')
    instruc = 'Processo com sentença!'
    return instruc

print('**Bem vindo ao {}**'.format('CPC Programado V5"'))
print('Desse ponto em diante, a sigla "CPC" indica "Código de Processo Civil"')

pautora = input('Digite o nome da parte autora: ')

pre = input('Digite o nome da parte ré: ')

print('Olá representante legal da parte autora {}.'.format(pautora))
print('Antes de começar, vamos verificar os documentos necessários à propositura da ação!')

print(poloativo())

liminar = procedimentoprotocoloinicial()

try:
    if liminar == 1:
        print('Autos conclusos para despacho.')
        print('Agora começa o que chamaremos de "jogo da decisão liminar"')
        
    if liminar == 0:
        Despacho1 = concl1semlim ()

    if Despacho1 == 'd':
        print('Agora deve ocorrer a citação do réu!')
        print(citreu())
        autocompos = concioumed()
        print('Sobre a autocomposição, as partes manifestaram que', autocompos)
        if autocompos is not 'Conversamos, deu certo!':
            prazoreu1 = 1

    if prazoreu1 == 1:
        manifreu1 = manifestacaoreu1()
        print('Note que essa versão do CPC programado ainda não discute a possibilidade de o réu alegar não ser')
        print('polo passivo legítimo.')
        if manifreu1 != 'b1' and manifreu1 != 'c1':
            limreconv = 0
    
    if limreconv == 0:
        print('Hora de observar o prosseguimento do processo após a juntada da contestação do autor.')
        print('A fase de providências preliminares de saneamento está prevista nos arts. 347 a 353 do CPC.')
        print('O capítulo que versa sobre isso no CPC possui três seções, intituladas, respectivamente:')
        print('Seção I: "Da Não Incidência dos Efeitos da Revelia",')
        print('Seção II: "Do Fato Impeditivo, Modificativo ou Extintivo do Direito do Autor",')
        print('Seção III: "Das Alegações do Réu".')
        print('Em resumo, esse capítulo descreve os casos nos quais se intima o autor para apresentação de')
        print('réplica (arts. 350 e 351), sobre a verificação de vícios ou irregularidades sanáveis, e')
        print('sobre o procedimento de manifestação do autor e do réu quando não se aplicam os efeitos')
        print('da revelia para o réu que não se manifestou tempestivamente nos autos.')
        print('Essa fase processual, por sua vez, necessariamente nos leva à fase intitulada')
        print('DO JULGAMENTO CONFORME O ESTADO DO PROCESSO')
        print('Para tanto, chamaremos a função do julgamento conforme o estado do processo.')
        julconfestproc = funcjulconfestproc()
        
    if julconfestproc == 'd':
        print(instruc())

    print('Em desenvolvimento!')

except:
    print('Em desenvolvimento!')