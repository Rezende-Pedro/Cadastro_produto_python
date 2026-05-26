class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def mostrar(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f}".replace('.',','))
        
def menu_inicial():
    try:
        menu = input("\nSelecione uma das opções abaixo:\n1-Cadastrar produto \n2-Lista de produtos\n3-Comprar produto\n4.Sair\n")
        if len(menu) == 0:
            print("Erro: este campo não pode ficar em branco\n")
            return            
        
        resposta = int(menu)
        if resposta <1 or resposta >4:
            print("Erro: digite uma das opções de 1 a 4\n")
        
        else:
            return resposta
        
    except ValueError:
        print("Erro: digite uma das opções de 1 a 4\n")
        

def produto():
    while True:
        produto = input("\nInforme o nome do produto a cadastrar: ").capitalize().strip()
        if len(produto) == 0:
            print("Erro: este campo não pode ficar em branco \n")
        
        elif not produto[0].isalpha():
            print("Erro: O nome do produto deve começar com uma letra")
            
        elif not produto.replace(' ', '').isalnum():
            print("Erro: Digite letras e numeros")
        
        else:
            return produto
            
def valor_produto(nome):
    while True:
        try:
            valor = float(input(f"digite o valor do produto {nome}: ").replace(',','.'))
            if valor <= 0:
                print("Erro: digite uma valor válido para o produto\n")
            else:
                return valor
        except:
            print("Erro: digite uma valor válido para o produto\n")
        
lista_produtos = []

while True:
    resposta = menu_inicial()                       
        
    if resposta == 4:
        print("Obrigado pelo seu tempo")
        break
    
    if resposta == 1:
        nome_produto = produto()
        valor = valor_produto(nome_produto)
        
        novo_produto = Produto(nome_produto, valor)
        
        lista_produtos.append(novo_produto)
        print(f"Produto {nome_produto} cadastrado com sucesso!")
        
    if resposta == 2:
        print("\n--LISTA DE PRODUTOS--")
        if len(lista_produtos) == 0:
            print("Nenhum produto foi cadastrado\n")
        
        for item in lista_produtos:
            item.mostrar()
        
    if resposta == 3:
        while True:
            if len(lista_produtos) == 0:
                print("Não existe nenhum produto a venda\n")
                break 
            else:
                print("\n--PRODUTOS DISPONÍVEIS--\n")
                for item in lista_produtos:
                    item.mostrar()
            
                escolher = input("\nDigite o produto desejado: ").strip().lower()
                produto_encontra = None
        
                for item in lista_produtos:
                    if item.nome.lower() == escolher:
                        produto_encontra = item  
                        break 
                
                if produto_encontra == None:
                    print("Erro: Produto não encontrado. Tente novamente.\n")
                
                else: 
                    try:
                        quantidade = int(input(f"Digite a quantidade levada de {produto_encontra.nome}: "))
                        if quantidade <= 0:
                            print("Quantidade inválida.")
                            continue
                            
                        total = quantidade * produto_encontra.preco
                        if total >= 100:
                            print("Desconto disponível")
                            desconto = (total / 100) *95
                            print(f"O valor da compra é R${total:.2f}, porém com o desconto o novo valor passa a ser {desconto:.2f}\n".replace(".",","))
                        else:
                            print("Desconto indisponível")
                            print(f"O valor da compra é R${total:.2f}\n".replace(".",","))
            
                        while True:
                            try:
                                forma_pagamento = int(input("Selecione a forma de pagamento: 1.Crédito   2.Débito   3.Pix\n"))
                                if forma_pagamento < 1 or forma_pagamento > 3: 
                                    print("Erro: Selecione uma opção de 1 a 3.\n")
                                else:
                                    print("\n--PAGAMENTO CONCLUÍDO--\n")  
                                    break 
                            except ValueError:
                                print("Erro: Digite um número de 1 a 3.\n")          
                        break 
                        
                    except ValueError:
                        print("Erro: Digite um número válido para a quantidade.\n")