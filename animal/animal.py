class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'{self.nome} foi comer...')

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f'{self.nome} diz miau...')

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f'{self.nome} está latindo...')

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def pular(self):
        print(f'{self.nome} está pulando...')

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f'{self.nome} diz Muuuuuuuuu...')