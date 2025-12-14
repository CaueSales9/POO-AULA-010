# Sistema de Precificação de Eletrônicos
Este repositório contém a implementação da classe Eletronico, uma extensão da classe base Produto. O código segue a regra de usar os 4 pilares de POO.

Funcionalidades
A classe Eletronico possui as seguintes características:

- Herança: Herda atributos e métodos da classe genérica Produto.
- Cálculo de Imposto: Aplica uma taxa fixa de 20% sobre o valor total dos produtos.
- Controle de Estoque: Integra-se com o método protegido _baixar_estoque da classe pai para garantir a disponibilidade do produto antes da venda.
- Tratamento de Erro: Retorna -1 caso não haja estoque suficiente para a quantidade solicitada.

Lógica do Método:
calcular_preco_final(self, qntd)
Este método realiza as seguintes operações:

1 - Recebe a quantidade (qntd) desejada.
2 - Chama self._baixar_estoque(qntd) para tentar reservar os itens.
Se houver estoque:
- Calcula o total (Preço Base × Quantidade)
- Calcula o imposto (20% do total)
- Retorna a soma (total + imposto)

Se não houver estoque:
- Retorna -1 (Deu erro)

Exemplo de Uso:

# Exemplo da Classe Pai
```

class Produto:
    def __init__(self, nome, preco_base, estoque):
        self.nome = nome
        self.preco_base = preco_base
        self.estoque = estoque

   def _baixar_estoque(self, qntd):
        if self.estoque >= qntd:
            self.estoque -= qntd
            return True
        return False

# Classe Eletronico
class Eletronico(Produto):
    def calcular_preco_final(self, qntd):
        if self._baixar_estoque(qntd):
            total = self.preco_base * qntd
            imposto = total * 0.20
            return total + imposto
        return -1
```

# Execução:

Criando um notebook com preço base de R$ 3000 e 5 unidades em estoque
notebook = Eletronico("Notebook Gamer", 3000.0, 5)

Tentando comprar 2 unidades
quantidade = 2
preco_final = notebook.calcular_preco_final(quantidade)

if preco_final != -1:
    print(f"Compra realizada com sucesso!")
    print(f"Produto: {notebook.nome}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor Final (com 20% de imposto): R$ {preco_final:.2f}")
else:
    print("Estoque insuficiente.")
    
# Pré-requisitos
Python 3.x
