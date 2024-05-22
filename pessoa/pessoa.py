#classe é uma forma onde pode ser criado varios objetos a partir dela.
class Pessoa():
    #atributos são variaveis.
    def __init__(self, nome: str, idade: int, peso: float, comendo = False, falando = False):
    #  ATRIBUTOS -- ARGUMENTOS
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = comendo
        self.falando = falando

    #métodos são ações. (funções)
    def comer(self, alimento):
        #Só posso comer se não estiver comendo.
        if self.comendo == False:
            print(f'{self.nome} está comendo. {alimento}')
            self.comendo = True
        else:
            print(f'{self.nome} já estava comendo.')

    def pararDeComer(self):
        #Só posso parar de comer se estiver comendo.
        if self.comendo == True:
            print(f'{self.nome} parou de comer.')
            self.comendo = False

    def andar(self):
        #Só posso andar se não estiver comendo.
        if self.comendo == False:
            print(f'{self.nome} está andando.')
        else:
            print(f'{self.nome} não pode andar pois esta comendo.')
        #Só posso andar se não estiver falando.
        if self.falando == False:
            print(f'{self.nome} está andando.')
        else:
            print(f'{self.nome} não pode andar pois está falando')


    def falar(self,frase):
        #Só posso falar se não estiver comendo.
        if self.comendo == False:
            print(f'{self.nome} está falando. {frase}')
        else:
            print(f'{self.nome} não pode falar agora pois ele esta comendo.')