from produto import Produto


class Revista(Produto):
    def calcular_preco_final(self, qntd):
        if self._baixar_estoque(qntd):
            total = self.preco_base * qntd
            return total
        return 1