# Case 2 - Bemobi

Para esse case foi desenvolvido um *script* analisador de logs, que recebe como entrada um arquivo de log de um novo serviço da Bemobi e devolve como saída um arquivo resposta com dados sumarizados.

## Entrada
Cada linha do arquivo de log contêm um identificador de usuário e seu *status* ("cancelado" ou "assinado") dentro do serviço. No repositório em questão há quatro logs de exemplo:

* log1.txt: Onde há um log válido;
* log2.txt: Onde há um log válido com dados diferentes de log1.txt;
* log3_invalido.txt: Onde há um log com algumas linhas inválidas referentes ao identificador (falha proposital);
* log4_invalido.txt: Onde há um log com algumas linhas inválidas referentes ao *status* (falha proposital);

Note que a extensão é txt, mas poderia ser modificada de acordo com eventuais requisitos.

## Saídas

Para cada entrada lida, será gerado um arquivo com o final <nome-entrada>_saida.txt. Por exemplo, se a entrada for log1.txt, a saída será log1_saida.txt. O conteúdo do arquivo serão os dados sumarizados do log:

O primeiro campo é referente ao país, o segundo campo é referente a quantidade de usuários naquele país ("assinados" + "cancelados") e o terceiro campo é referente ao número de usuários com o *status* "assinado"
```
Brasil, 2, 0

Chile, 2, 1

México, 1, 1
```

## Execução

O *script* foi feito em Python na versão 3.9. Por isso, verifique se a sua máquina possui a versão apropriada da linguagem.

Para a sua execução realize um clone deste repositório via interface gráfica ou via terminal, utilizando o comando:

```
git clone https://github.com/gabteixeira/case2.git
```

Após realizar o clone, entre na pasta onde se encontra os arquivos *analisador_logs.py* e *biblioteca_logs.py*. Após isso, no terminal execute:

```
python analisador_logs.py
```

Após isso, o script estará em execução, siga as orientações apresentadas e realize a análise demandada. Você poderá testar com os arquivos exemplos disponíveis como log1.txt, log2.txt, log3_invalido.txt e log4_invalido.txt
