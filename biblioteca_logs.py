# Feito por Gabriel Viana Teixeira - Case 2: Bemobi
import sys 

# Função que lê arquivos de log (leitura apenas).
def ler_arquivo(nome_entrada):
    try:
        arquivo =  open(nome_entrada)
        return arquivo
    except:
        print("O arquivo inserido não existe ou não está no mesmo diretório do script.")
        return False

# Função que gera o arquivo de saída
def gerar_arquivo_saida(nome_entrada):
    nome_saida = nome_entrada.split('.')[0] + "_saida."+nome_entrada.split('.')[1] 
    saida_arquivo = open(nome_saida,'w')
    return saida_arquivo

# Função que fecha os arquivos de leitura e escrita.
def fechar_arquivo(arquivo):
    try:
        arquivo.close()
    except OSError:
        print("Falha ao fechar o arquivo. Tente novamente\n Erro: {}".format(OSError))
    except:
        print("Um erro inesperado ocorreu ao fechar o arquivo.\n Erro:{}".format(sys.exc_info()[0]))

# Função que recebe uma linha de arquivo como parâmetro e uma lista de ddi aceitos. Extrai o ddi encontrado.
def extrair_ddi(linha, ddi_paises):
    lista_ddi = ddi_paises
    ddi = linha[0:2]
    if(ddi in lista_ddi):
        return ddi
    else:
        print("DDI {} não identificado, verifique o seu arquivo. Valor Ignorado.".format(ddi))
        return False

# Função que recebe uma linha de arquivo como parâmetro. Extrai o número encontrado.
def extrair_numero(linha):
    try:
        numero = linha[0:14]
        return numero
    except:
        print("Um erro inesperado ao ler o arquivo.\n Erro:{}".format(sys.exc_info()[0]))
        return False
    
# Função que recebe uma linha de arquivo como parâmetro e extrai a situação encontrada.
def extrair_situacao(linha):
    lista_situacao = ["assinado", "cancelado"]
    situacao = linha.split()[1]
    if(situacao.strip() in lista_situacao):
        return situacao
    else:
        print("Situação: {}, não foi identificada, verifique o seu arquivo. Valor Ignorado.".format(situacao))
        return False

# Função que escreve no arquivo de saída de acordo com o ddi e valores recebidos.
def escrever_arquivo(arquivo,conteudo):
    try:
        for ddi, valores in conteudo.items():
            if(int(ddi) == 52):
                arquivo.write("México, {}, {}\n\n".format(valores[0],valores[1]))
            elif(int(ddi) == 55):
                arquivo.write("Brasil, {}, {}\n\n".format(valores[0],valores[1]))
            elif(int(ddi) == 56):
                arquivo.write("Chile, {}, {}\n\n".format(valores[0],valores[1]))
        print("O arquivo com a análise do log foi escrito com sucesso, verifique seu diretório.\n")
    except OSError:
        print("Falha ao escrever no arquivo. Tente Novamente.\n Erro: {}".format(OSError))
    except:
        print("Um erro inesperado ocorreu ao escrever o arquivo.\n Erro:{}".format(sys.exc_info()[0]))
    finally:
        return
        
# Função que gera um dicionário com o conteúdo a ser escrito no arquivo de saída.
def novo_conteudo(lista_paises):
    paises_conhecidos = ["Brasil","Chile", "México"]
    paises_sort = sorted(lista_paises)
    conteudo = {}

    for pais in paises_sort:
        if(pais.capitalize() in paises_conhecidos):
            conteudo[retorna_ddi(pais)] = [0,0]
    return conteudo

# Função que retorna o ddi de acordo com o nome do país.
def retorna_ddi(pais):
    if(pais.capitalize() == "Brasil"):
        return "55"
    elif(pais.capitalize() == "Chile"):
        return "56"
    elif(pais.capitalize() == "México"):
        return "52"

# Função que atualiza o conteúdo a ser escrito no arquivo
def atualizar_conteudo(conteudo, ddi, situacao):
    conteudo[ddi][0] +=1
    if(situacao == "assinado"):
        conteudo[ddi][1] +=1
    return True