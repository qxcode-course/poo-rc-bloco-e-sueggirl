from abc import ABC, abstractmethod
from enum import Enum

class Valuable(ABC):
    @abstractmethod
    def getLabel(self) -> str:
        pass

    @abstractmethod
    def getValue(self) -> float:
        pass

    @abstractmethod
    def getVolume(self) -> int:
        pass

class Moeda(Enum):
    M10  = ("M10",  0.10, 1)
    M25  = ("M25",  0.25, 2)
    M50  = ("M50",  0.50, 3)
    M100 = ("M100", 1.00, 4)

    def __init__(self, label, value, volume):
        self._label = label
        self._value = value
        self._volume = volume

    def getLabel(self):
        return self._label

    def getValue(self):
        return self._value

    def getVolume(self):
        return self._volume

    def __str__(self):
        return f"{self._label}:{self._value:.2f}:{self._volume}"

class Item(Valuable):
    def __init__(self, label: str, value: float, volume: int):
        self._label = label
        self._value = value
        self._volume = volume

    def getLabel(self):
        return self._label

    def getValue(self):
        return self._value

    def getVolume(self):
        return self._volume

    def __str__(self):
        return f"{self._label}:{self._value:.2f}:{self._volume}"


class Pig:
    def __init__(self, volumeMax: int):
        self._broken = False
        self._valuables: list[Valuable] = []
        self._volumeMax = volumeMax

    def addValuable(self, valuable: Valuable) -> bool:
        if self._broken:
            print("fail: the pig is broken")
            return False

        if self.getVolume() + valuable.getVolume() > self._volumeMax:
            print("fail: the pig is full")
            return False

        self._valuables.append(valuable)
        return True

    def breakPig(self) -> bool:
        if self._broken:
            return False
        self._broken = True
        return True

    def getCoins(self):
        if not self._broken:
            print("fail: you must break the pig first")
            return []

        coins = [v for v in self._valuables if isinstance(v, Moeda)]
        self._valuables = [v for v in self._valuables if not isinstance(v, Moeda)]
        return coins

    def getItems(self):
        if not self._broken:
            print("fail: you must break the pig first")
            return []

        items = [v for v in self._valuables if isinstance(v, Item)]
        self._valuables = [v for v in self._valuables if not isinstance(v, Item)]
        return items

    def calcValue(self) -> float:
        return sum(v.getValue() for v in self._valuables)

    def getVolume(self) -> int:
        return sum(v.getVolume() for v in self._valuables)

    def getVolumeMax(self) -> int:
        return self._volumeMax

    def isBroken(self) -> bool:
        return self._broken

    def __str__(self):
        content = ", ".join(str(v) for v in self._valuables)
        state = "broken" if self._broken else "intact"
        return f"[{content}] : {self.calcValue():.2f}$ : {self.getVolume()}/{self._volumeMax} : {state}"


def main():
    pig: Pig

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            pig = Pig(int(args[1]))

        elif args[0] == "show":
            print(pig)

        elif args[0] == "addMoeda":
            value = args[1]
            pig.addValuable(Moeda[f"M{value}"])

        elif args[0] == "addItem":
            label = args[1]
            value = float(args[2])
            volume = int(args[3])
            pig.addValuable(Item(label, value, volume))

        elif args[0] == "break":
            pig.breakPig()

        elif args[0] == "extrairCoins":
            moedas = pig.getMoedas()
            if moedas:
                print("[" + ", ".join(str(c) for d in moedas) + "]")

        elif args[0] == "extrairItems":
            items = pig.getItems()
            if items:
                print("[" + ", ".join(str(i) for i in items) + "]")


main()