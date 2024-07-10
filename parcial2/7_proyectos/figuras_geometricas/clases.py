class Figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    visible = None

    def estaVisible(self, visible):
        pass
    
    def mostrar(self):
        pass

    def ocultar(self):
        pass

    def mover():
        pass

    def calcularArea():
        pass

    def getEstaVisible(self):
        return self.visible
    
    def setEstaVisible(self, visible):
        self.visible = visible
    
    def getInfo(self):
        pass

class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho

    def getAlto(self):
        return self.alto
    
    def setAlto(self, alto):
        self.alto = alto
    
    def getAncho(self):
        return self.ancho
    
    def setAncho(self, ancho):
        self.ancho = ancho

    area = 0
    def calcularArea(self, alto, ancho, area):
        area = alto * ancho
        self.area = float(area)
        return self.area 
    
    def getCalcularArea(self):
        return self.area
    
    def setCalcularArea(self, area):
        self.area = area

    def getInfo(self):
        print(f"Alto = {self.getAlto()}, Ancho = {self.getAncho()}, Area = {self.getCalcularArea()}")

class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.radio = radio
    
    def getRadio(self):
        return self.radio
    
    def setRadio(self, radio):
        self.radio = radio

    def getInfo(self):
        print(f"Radio = {self.getRadio()}")