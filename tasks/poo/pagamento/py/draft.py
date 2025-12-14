from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("Valor inválido para pagamento")

    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descricao}")

    @abstractmethod
    def processar(self):
        pass


class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero_cartao, titular, limite_disponivel):
        super().__init__(valor, descricao)
        self.numero_cartao = numero_cartao
        self.titular = titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        if self.valor > self.limite_disponivel:
            raise Exception(
                f"Limite insuficiente no cartão {self.numero_cartao}"
            )
        self.limite_disponivel -= self.valor
        print(
            f"Pagamento aprovado no cartão {self.titular}. "
            f"Limite restante: {self.limite_disponivel}"
        )


class Pix(Pagamento):
    def __init__(self, valor, descricao, chave_pix, banco):
        super().__init__(valor, descricao)
        self.chave_pix = chave_pix
        self.banco = banco

    def processar(self):
        print(
            f"PIX enviado via {self.banco} usando a chave {self.chave_pix}"
        )


class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras, vencimento):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")


class Fiado(Pagamento):
    def __init__(self, valor, descricao, cliente, limite_fiado):
        super().__init__(valor, descricao)
        self.cliente = cliente
        self.limite_fiado = limite_fiado

    def processar(self):
        if self.valor > self.limite_fiado:
            raise Exception(
                f"Fiado negado para {self.cliente}: limite insuficiente"
            )
        self.limite_fiado -= self.valor
        print(
            f"Compra no fiado registrada para {self.cliente}. "
            f"Limite restante: R$ {self.limite_fiado}"
        )


def processar_pagamento(pagamento: Pagamento):
    try:
        pagamento.validar_valor()
        pagamento.resumo()
        pagamento.processar()
    except Exception as erro:
        print(f"Erro: {erro}")


pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"), Pix(0, "Café", "senna@ufc.com", "Banco POO"),
    CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500), Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700), Fiado(2999, "Notebook Gamer", "David Senna", 3000)
]

for pagamento in pagamentos:
    processar_pagamento(pagamento)

