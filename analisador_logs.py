# Feito por Gabriel Viana Teixeira - Case 2: Bemobi
from biblioteca_logs import *

while True:
    nome_entrada = input("Insira o nome do arquivo a ser analisado:\n")
    entrada_arquivo = ler_arquivo(nome_entrada)
  
    # Arquivo válido, então começa a leitura dele
    if(entrada_arquivo):
        saida_arquivo = gerar_arquivo_saida(nome_entrada)
        conteudo = novo_conteudo(['Brasil', 'México','Chile'])
        numeros = []
        status = False
        
        # Percorre cada linha do arquivo de entrada
        for num, linha in enumerate(entrada_arquivo):
            if(len(linha) > 1):
                ddi = extrair_ddi(linha, conteudo.keys())
                numero = extrair_numero(linha)
                situacao = extrair_situacao(linha)

                # Se conseguiu extrair tudo, pode atualizar o conteúdo a ser escrito
                if(ddi and situacao and numero):
                    # Não escreve números repetidos, para evitar estados ambíguos.
                    if(numero not in numeros):
                        numeros.append(numero)
                        status = atualizar_conteudo(conteudo,ddi,situacao)
                    else:
                        print("Atenção, o número encontrado se encontra mais de uma vez: {} na linha {}\n".format(numero,num+1  ))
                else:
                    print("Erro encontrado na linha {}\n".format(num))
                    
        # Se o status alterou, significa que algo pode ser escrito
        if(status):
            escrever_arquivo(saida_arquivo,conteudo)
            fechar_arquivo(entrada_arquivo)
            fechar_arquivo(saida_arquivo)

        while True:
            try:
                print("Selecione uma opção:\n 1 - Ler outro Arquivo \n 2 - Encerrar script analisador")
                opcao = int(input())
                break
            except ValueError:
                print("Ops! Opção Inválida. Tente novamente")
            
        if(opcao == 2):
            break