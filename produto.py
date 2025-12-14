class Produto:
    def __init__(self, nome, preco_base, estoque_ini):
        self.nome = nome
        self.preco_base = preco_base
        self.__estoque = estoque_ini

    def ver_estoque(self):
        return self.__estoque

    def repor_estoque(self, qntd):
        if qntd > 0:
            self.__estoque += qntd
            print(f"Estoque de {self.nome} aumentou em {qntd} unidades")
        else:
            print("Quantidade inválida para reposição.")

    def _baixar_estoque(self, qntd):
        if qntd <= self.__estoque:
            self.__estoque -= qntd
            return True
        else:
            return False