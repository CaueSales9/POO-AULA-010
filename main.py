from revista import Revista
from eletronico import Eletronico



catalogo = []

def buscar_produto(nome_busca):
    for i in catalogo:
        if i.nome == nome_busca:
            return i
    return None

while True:
    print("\nGESTÃO DA BANCA")
    print("1 - Cadastrar Produto")
    print("2 - Gerenciar Produto")
    print("3 - Sair")
    
    opcao_menu = input("Escolha: ")

    if opcao_menu == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        qtd = int(input("Estoque: "))
        tipo = input("\nTipo:\n1-Revista\n2-Eletrônico\n ")

        if tipo == "1":
            prod = Revista(nome, preco, qtd)
            print(f"Revista '{nome}' cadastrada!")
        else:
            prod = Eletronico(nome, preco, qtd)
            print(f"Eletrônico '{nome}' cadastrado!")
        
        catalogo.append(prod)

    elif opcao_menu == "2":
        nome_prod = input("Nome do produto: ")
        produto_sele = buscar_produto(nome_prod)

        if produto_sele:
            while True:
                print(f"\nGerenciando: {produto_sele.nome}")
                print(f"Preço: R$ {produto_sele.preco_base:.2f}")
                print("1 - Ver Estoque Atual")
                print("2 - Realizar Venda")
                print("3 - Repor Estoque (Aumentar Estoque)")
                print("4 - Voltar ao Menu Principal")
                
                acao = input("Opção: ")

                if acao == "1":
                    print(f"Estoque atual: {produto_sele.ver_estoque()} unidades")

                elif acao == "2":
                    qtd_venda = int(input("Quantidade para vender: "))
                    valor_final = produto_sele.calcular_preco_final(qtd_venda)

                    if valor_final != -1:
                        print(f"Venda realizada!")
                        print(f"Valor total a pagar: R$ {valor_final:.2f}")
                    else:
                        print("Estoque insuficiente")

                elif acao == "3":
                    qtd_repo = int(input("Quantidade: "))
                    produto_sele.repor_estoque(qtd_repo)

                elif acao == "4":
                    break
                else:
                    print("Opção inválida")
        else:
            print("Produto não encontrado")

    elif opcao_menu == "3":
        print("Fechada")
        break
    else:
        print("Opção inválida")