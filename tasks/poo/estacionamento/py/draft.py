from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, idd: str, entrada: int):
        self.id = idd
        self.entrada = entrada
        self.tipo = self.getTipo()

    @abstractmethod
    def calcularValor(self, saida: int) -> float:
        pass

    @abstractmethod
    def getTipo(self) -> str:
        pass

    def __str__(self) -> str:
        return (
            self.tipo.rjust(10, "_")
            + " : "
            + self.id.rjust(10, "_")
            + " : "
            + str(self.entrada)
        )


class Bike(Veiculo):
    def getTipo(self):
        return "Bike"

    def calcularValor(self, saida: int) -> float:
        return 3.00


class Moto(Veiculo):
    def getTipo(self):
        return "Moto"

    def calcularValor(self, saida: int) -> float:
        return (saida - self.entrada) / 20


class Carro(Veiculo):
    def getTipo(self):
        return "Carro"

    def calcularValor(self, saida: int) -> float:
        return max((saida - self.entrada) / 10, 5.00)


class Estacionamento:
    def __init__(self):
        self.tempo = 0
        self.veiculos: list[Veiculo] = []

    def avancarTempo(self, minutos: int):
        self.tempo += minutos

    def estacionar(self, tipo: str, idd: str):
        if tipo == "bike":
            veiculo = Bike(idd, self.tempo)
        elif tipo == "moto":
            veiculo = Moto(idd, self.tempo)
        elif tipo == "carro":
            veiculo = Carro(idd, self.tempo)
        else:
            print("fail: tipo invalido")
            return

        self.veiculos.append(veiculo)

    def pagar(self, idd: str):
        for veiculo in self.veiculos:
            if veiculo.id == idd:
                valor = veiculo.calcularValor(self.tempo)
                print(
                    f"{veiculo.tipo} chegou {veiculo.entrada} saiu {self.tempo}. "
                    f"Pagar R$ {valor:.2f}"
                )
                self.veiculos.remove(veiculo)
                return
        print("fail: veiculo nao encontrado")

    def show(self):
        for veiculo in self.veiculos:
            print(veiculo)
        print(f"Hora atual: {self.tempo}")


def main():
    estacionamento = Estacionamento()

    while True:
        try:
            line = input()
            print("$" + line)
            args = line.split()

            if args[0] == "end":
                break
            elif args[0] == "tempo":
                estacionamento.avancarTempo(int(args[1]))
            elif args[0] == "estacionar":
                estacionamento.estacionar(args[1], args[2])
            elif args[0] == "pagar":
                estacionamento.pagar(args[1])
            elif args[0] == "show":
                estacionamento.show()
            else:
                print("fail: comando invalido")
        except EOFError:
            break


main()
