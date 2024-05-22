class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def areaCalcular(self,base,altura):
        self.area = base * altura
        print(f'A area do retângulo é: {self.area}')

    def perimetroCalcular(self,base,altura):
        self.perimetro = 2*(base+altura)
        print(f'O perimetro do retângulo é: {self.perimetro}')

class Triangulo(Forma):
    def __init__(self):
        self.altura = 0
        super().__init__()
        #self.area = 0
        #self.perimetro = 0

    def areaCalcular(self,base,altura):
        self.altura = altura
        self.area = (base * self.altura) / 2
        print(f'A area do triangulo é {self.area}')

    def perimetroCalcular(self,lado):
        self.perimetro = lado*3
        print(f'O perimetro do triangulo é {self.perimetro}')
