from produto import Produto


class Eletronico(Produto):
    def calcular_preco_final(self, qntd):
        if self._baixar_estoque(qntd):
            total = self.preco_base * qntd
            imposto = total * 0.20
            return total + imposto
        return -1
