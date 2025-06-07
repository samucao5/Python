class retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.altura * self.largura
        print(f"{self.largura} * {self.altura} = {area}")

largura_1 = int(input("digite a largura: "))
altura_1 = int(input("digite a altura: "))

area_1 = retangulo(largura_1,altura_1)
area_1.calcular_area()

