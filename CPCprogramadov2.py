#python CPCprogramadov2.py
import string
import random
import sys

def poloativo():

    while True:
        print('Digite "pj" ou "pf" para responder:')
        tipopautora = input('A parte autora é Pessoa Jurídica ou Pessoa Física? ')

        if tipopautora == 'pj' :
            print('Documentos necessários à propositura da ação como Pessoa Jurídica:')
            print('Petição Inicial; Procuração assinada por representante;')
            print('Contrato Social; Documentos necessários à instrução do Pedido')
            print('As formalidades de redação da petição inicial podem ser verificadas nos artigos 319 e 320 do CPC')
            print('Para fins de noção de modelo de petição inicial, o Google pode ser uma boa ferramenta.')
        elif tipopautora == 'pf' :
            print('Documentos necessários à propositura da ação como Pessoa Física:')
            print('Petição Inicial; Procuração assinada pela parte;')
            print('Documento Identificação da parte; Documentos necessários à instrução do Pedido')
            print('As formalidades de redação da petição inicial podem ser verificadas nos artigos 319 e 320 do CPC')
            print('Para fins de noção de modelo de petição inicial, o Google pode ser uma boa ferramenta.')
        else:
            print('Digite somente as letras "pj" ou "pf" e aperte "enter"')
            continue

        break

def procedimentoprotocoloinicial():

    while True:
        inicial = input('Protocolo petição inicial: ')

        try:
            tipoinicial = int(inicial)
            while inicial != 'Protocolada':
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
                    inicial = input('Protocolo petção inicial: ')
                    try:
                        tipoinicial = int(inicial)
                        continue
                    except:
                        print('Erro, favor inserir valor numérico "1" para liminar, e "0" para sem liminar')
                        continue
            break
        except:
            print('Erro, favor inserir valor numérico 1 para liminar, e 0 para sem liminar')
            continue

def concl1semlim():

    while True:

        print('Autos conclusos para despacho')
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
            continue

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
                print('Cuidado, passar mais de uma vez por esse caminho em nosso programa, pode gerar')
                print('indeferimento da inicial (opção "c" desse menu) na prática, pelo não cumprimento da ordem')
                print('de emenda da inicial.')
                continue
            elif Conclusão1 == "c":
                print('Que pena, foi indeferida a petição inicial de {}'.format(pautora))
                print('Do indeferimento da petição inicial, cabe apelação, nos termos do art. 331 do CPC.')
                print('Da mesma forma que para a improcedência, cabe retratação do juízo a quo no caso de')
                print('protocolo de apelação, no prazo de 5 dias (art. 331 caput do CPC)')
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
                continue

print('**Bem vindo ao {}**'.format(sys.argv[0]))
print('Desse ponto em diante, a sigla "CPC" indica "Código de Processo Civil"')

pautora = input('Digite o nome da parte autora: ')
print('Olá representante legal da parte autora {}'.format(pautora))
print('Antes de começar, vamos verificar os documentos necessários à propositura da ação!')

poloativo()

print('Tudo ok com os documentos, certo?')
print('Hora de protocolar a petição inicial!')
print('Digite "1" para protocolar a petição inicial com pedido liminar, e "0" para protocolar sem pedido liminar')

liminar = procedimentoprotocoloinicial()

if liminar == 1:
    print('Autos conclusos para despacho')
    print('Agora começa o que chamaremos de "jogo da decisão liminar"')
if liminar == 0:
    Despacho1 = concl1semlim ()
    if Despacho1 == 'd':
        print('Agora deve ocorrer a citação do réu! Uma das funções que fica para o póximo episódio =D')
    else:
        print('Aguardando definição de funções da fase recursal')

print('Em desenvolvimento =D')
