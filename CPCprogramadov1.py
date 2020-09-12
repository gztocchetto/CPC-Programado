#python CPCprogramadov1.py
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
    print('Em desenvolvimento')
if liminar == 0:
    print('Autos conclusos para despacho')
    print('Dessa conclusão, o juízo pode decidir por:')
    print('a) Improcedência liminar do pedido - art. 332 do CPC')
    print('b) Indeferimento da petição inicial - art. 330 do CPC')
    print('c) Determinação de emenda à inicial - art. 321 do CPC')
    print('d) Determinação da citação de réu(s), e designação de audiência de conciliação ou mediação* - art. 334 do CPC')
    input('Para explorar cada uma das alternativas, digite a letra correspondente: ')
    print('Em desenvolvimento')
