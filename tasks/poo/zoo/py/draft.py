from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    @abstractmethod
    def apresentar(self) -> str:
        pass

    @abstractmethod
    def fazerSom(self) -> str:
        pass

    @abstractmethod
    def mover(self) -> str:
        pass

def apresentar(animal: Animal):
    print(animal.apresentar())
    print(animal.fazerSom())
    print(animal.mover())

