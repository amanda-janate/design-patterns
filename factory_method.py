"""
Factory method é um padrao de criação que permite definir uma interface
(classe abstrata) para criar objetos, mas permite que as subclasses
decidam quais objetos criar.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro luxo busca cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular busca cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto busca cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class VeiculoFactoryNorte(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        raise ValueError(f"Tipo de veículo desconhecido: {tipo}")


class VeiculoFactorySul(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        # if tipo == 'luxo':
        #     return CarroLuxo()
        # if tipo == 'moto':
        #     return Moto()
        raise ValueError(f"Tipo de veículo desconhecido: {tipo}")


if __name__ == '__main__':
    from random import choice
    veiculos_disp_norte = ['luxo', 'popular', 'moto']
    veiculos_disp_sul = ['popular']

    print('Norte')
    for i in range(10):
        carro = VeiculoFactoryNorte(choice(veiculos_disp_norte))
        carro.buscar_cliente()

    print()

    print('Sul')
    for i in range(10):
        carro2 = VeiculoFactorySul(choice(veiculos_disp_sul))
        carro2.buscar_cliente()
