class Atleta:
    def __init__(self,peso):
        self.aposentado = False
        self.peso = peso
        self.aquecido = False
    def aposentar(self):
        self.aposentado = True
        print(f'O atleta se aposentou.')

    def aquecer(self,tempo):
        if self.aposentado == False:
            self.aquecido = True
            print(f'O atleta está aquecendo {tempo} minutos.')
        else:
            print(f'O atleta não pode aquecer. Ele ja se aposentou.')

class Corredor(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.correndo = False

    def correr(self):
        if self.aposentado == False:
            if  self.aquecido == False:
                print('O atleta está correndo.')
                self.correndo = True
            else:
                print('Não foi possivel correr. O atleta não está aquecido!')
        else:
            print('Não foi possivel correr. O atleta está aposentado!')

    def pararDeCorrer(self):
        if self.correndo == True:
            print('O atleta está parando de correr.')
            self.correndo = False
        else:
            print('O atleta não pode parar pois ele não está correndo.')
class Nadador(Atleta):
    def __init__(self,peso):
        super().__init__(peso)

    def nadar(self):
        print('O atleta está nadando.')


class Ciclista(Atleta):
    def __init__(self,peso):
        super().__init__(peso)

    def pedalar(self):
        print('O atleta está pedalando.')

class Triatleta(Corredor, Nadador, Ciclista):
    print()