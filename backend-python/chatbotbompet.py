# -*- coding: utf-8 -*-
"""chatBotBomPet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jrk4Wi01FsddsuayJaFt3Z7Rk_ldxuM1
"""



# projeto_bompet

def sucess_pag():
    print(f'******\n Sua compra foi confirmada com sucesso, qualquer dúvida, entre em contato novamente. Obrigado(a) por escolher a Bom Pet!\n********')
    
def pagamento_pendente():
    print(f'******\nO seu boleto foi enviado para o seu e-mail com o prazo de vencimento de 3 dias úteis:\n ******')

def forma_pagamento():
   print(f'Escolha a forma de pagamento:')
   resposta  = input (f'[1] - Cartão. \n[2] - Boleto. \n[3] - Voltar ao menu anterior.\n')
   if   resposta == '1' :
       cartao  = input (f'Digite o número do seu cartão:')   
       responsavel = input (f'Digite o nome do responsável:') 
       sucess_pag()
   elif resposta == '2' :
       email = input (f'Informe seu email para o envio do boleto')
       pagamento_pendente()
   else:
        print('\n Opção inválida, volte ao menu principal')
        comprar()


def comprar():
     resposta = input(f'[1] - Realizar a compra. \n[2] - Voltar ao menu anterior.\n')
     if   resposta == '1' :
         print('Informe seus dados:')
         nomeCompleto = input('Digite seu nome completo: ')
         cpf = input('CPF: ')
         rua = input('Rua: ')
         numero = input('Número:')
         complemento = input('Complemento:')
         bairro = input('Bairro:')
         cidade = input('Cidade:')
         uf = input('CEP:')
         forma_pagamento()

     elif resposta == '2' :
          fazer_compra()
     else:
        print('\n{nome} Opção inválida, volte ao menu principal')
        fazer_compra()


def fazer_compra():
    print(f'Escolha o produto:')
    resposta = input(f'[1] - BOBINA COM 1000 SAQUINHOS HIGIÊNICOS BIODEGRADÁVEIS \n[2] - SUPORTE PAREDE PRETO COM BOBINA DE SAQUINHOS BIODEGRADÁVEIS\n[3] - SUPORTE PAREDE VERDE COM BOBINA DE SAQUINHOS BIODEGRADÁVEIS\n[4] - SUPORTE BANCADA PRETO COM BOBINA DE SAQUINHOS BIODEGRADÁVEIS\n[5] - SUPORTE BANCADA VERDE COM BOBINA DE SAQUINHOS BIODEGRADÁVEIS\n[6] - CAIXA BIG C/ 6 BOBINAS SAQUINHOS HIGIÊNICOS BIODEGRADÁVEIS\n[7] - Voltar ao menu anterior\n')
    if resposta == '1':
        print(f'\n Medida Bobina: 1.000 Saquinhos\n Medida Bobina : 15×7,5 cm\n Medida Saquinho :25cm X 39,5cm\n Marca: Bompet\n Produto Embalado: 20X20X17\n Peso:1,180 ')
        comprar()    
    elif resposta == '2':
        print(f'\n Modelo: Suporte de Parede\n Medida Bobina: 15×7,5 cm\n Medida Suporte: 26cm x 16cm x 22cm\n Conteúdo da Embalagem: 01 Suporte de Fixação em Parede + 01 Suporte Fixação da Bobina + 01 Bobina + Parafuso Com  Bucha 6mm para Fixação\n Produto Embalado 20X20X17\n Peso:  1.470\n Marca: Bompet')
        comprar()
    elif resposta == '3':
        print(f'\n Modelo: Suporte de Parede\n Medida Bobina 15×7,5 cm\n Medida Suporte : 26cm x 16cm x 22cm\n Conteúdo da Embalagem: 01 Suporte de Fixação em Parede + 01 Suporte Fixação da Bobina + 01 Bobina + Parafuso Com  Bucha 6mm para Fixação\n Produto Embalado 20X20X17   Peso:  1.470\n Marca: Bompet')
        comprar()
    elif resposta == '4':
        print(f'\n Modelo: Suporte de Bancada;Medida Suporte: 24cm x 16cm x 51cm;\nMedida da Bobina: 15 x 7,5cm;\nMedida do Saquinho: 25 x 39,5cm;\nConteúdo da Embalagem: 01 Suporte de Fixação em Bancada + 01 Suporte Fixação Bobina + 01 Bobinas 1.000unid+ Parafuso e Bucha Para Fixação. Produto Embalado 40X20X17   Peso:  1.550\nMarca: Bompet\n')
        comprar()
    elif resposta == '5':
        print(f'\n Modelo: Suporte de Bancada;Medida Suporte: 24cm x 16cm x 51cm;\nMedida da Bobina: 15 x 7,5cm;\nMedida do Saquinho: 25 x 39,5cm;\nConteúdo da Embalagem: 01 Suporte de Fixação em Bancada + 01 Suporte Fixação Bobina + 01 Bobinas 1.000unid+ Parafuso e Bucha Para Fixação.\nProduto Embalado 40X19X17   Peso:  1.550\nMarca: Bompet\n')
        comprar()
    elif resposta == '6':
        print(f'\n Modelo: Bobina 1.000 Saquinhos;\nMedida Bobina: 15×7,5cm;\nMedida Saquinho: 25cm X 39,5cm\nMarca: Bompet\nProduto Embalado: 50X30X17   Peso: 6,920\nConteúdo da Embalagem: 6 Bobinas com 1000 saquinhos cada\n')
        comprar()
    elif resposta == '7':
      start()
    else:
        print('\n Opção inválida, digite novamente')
        fazer_compra()


def  duvidas_sugestoes() :
     print(f'Qual seria sua dúvida ou sugestão?\n')
     resposta = input(f'[1] - Solicitar informações sobre o prazo da compra.\n[2] - O produto não chegou dentro do prazo.\n[3] - O pedido chegou errado.\n[4] - Falar com atendente\n')
     if resposta == '1':
            print(f'Seu pedido chegará em um prazo em até 7 dias úteis após a confirmação do pagamento.') 
     elif resposta == '2':
            mensagem_atendente()
     elif resposta == '3':
            mensagem_atendente()
     elif resposta == '4':
            mensagem_atendente()
     else:
           print('\n Opção inválida, volte ao menu principal')
           start()
      
def mensagem_atendente() :
      print(f'*********************** \nEstou encaminhando seu chamado para um dos nossos atendentes, por favor, aguarde.\n*********************** \n')
      



def start():
    print(f' *********************** \n \n Olá, Seja Bem Vindo a central de atendimento e vendas da Bom Pet!!\n \n ***********************\n')
    print(f'Ao prosseguir com a conversa, você concorda com a nossa comunicação através deste canal, nos termos da Lei 13.709/2018?\n ')
    nome = input('Se a resposta for sim, digite seu primeiro nome: \n')
    resposta = input(f'\nEm que podemos te ajudar?\n[1] - Fazer uma compra.\n[2] - Dúvidas e sugestões.\n')
    
    
    # Processar a resposta enviada

    if resposta == '1':
        fazer_compra()
    elif resposta == '2':
        duvidas_sugestoes()
    else:
        print('Número inválido, digite novamente')
        start()

if __name__ == '__main__':
    start()

