class Materiales:
    def __init__(self, tipo, cantidad, precio_por_unidad):
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_por_unidad = precio_por_unidad

    def calcular_costo_total(self):
        return self.cantidad * self.precio_por_unidad



class Arena(Materiales):
    def __init__(self, cantidad, precio_por_unidad, uso_arena, tipo_arena, origen_arena):
        super().__init__("Arena", cantidad, precio_por_unidad)
        self.uso_arena = uso_arena
        self.tipo_arena = tipo_arena
        self.origen_arena = origen_arena

    def calcular_costo_total(self):

        return self.cantidad * self.precio_por_unidad * 1.05  # Aplicar un 5% de impuesto

    def __str__(self):
        return f"{self.tipo}: {self.cantidad} unidades, precio por unidad: ${self.precio_por_unidad:.2f}, uso: {self.uso_arena}, tipo: {self.tipo_arena}. origen: {self.origen_arena}"

class Grava(Materiales):
    def __init__(self, cantidad, precio_por_unidad, origen_grava):
        super().__init__("Grava", cantidad, precio_por_unidad)
        self.origen_grava = origen_grava

    def calcular_costo_total(self):

        return self.cantidad * self.precio_por_unidad * 1.08  # Aplicar un 8% de impuesto
    
    def __str__(self):
        return f"{self.tipo}: {self.cantidad} unidades, precio por unidad: ${self.precio_por_unidad:.2f}, origen: {self.origen_grava}"
    

class Ladrillos(Materiales):
    def __init__(self, cantidad, precio_por_unidad, lote, tipo_ladrillo):
        super().__init__("Ladrillos", cantidad, precio_por_unidad)
        self.lote = lote
        self.tipo_ladrillo = tipo_ladrillo

    def calcular_costo_total(self):
        # Override el método para Ladrillos
        return self.cantidad * self.precio_por_unidad
    def __str__(self):
        return f"{self.tipo}: {self.cantidad} unidades, precio por unidad: ${self.precio_por_unidad:.2f}, lote: {self.lote}, tipo: {self.tipo_ladrillo}"

class Cemento(Materiales):
    def __init__(self, cantidad, precio_por_unidad, marca, uso):
        super().__init__("Cemento", cantidad, precio_por_unidad)
        self.marca = marca
        self.uso = uso

    def calcular_costo_total(self):
        # Override el método para Cemento
        return self.cantidad * self.precio_por_unidad * 1.1  # Aplicar un 10% de impuesto
    
    def __str__(self):
        return f"{self.tipo}: {self.cantidad} unidades, precio por unidad: ${self.precio_por_unidad:.2f}, marca: {self.marca}, uso: {self.uso}"
    
    

# Crear objetos
arena1 = Arena(cantidad=100, precio_por_unidad=5.50, uso_arena="cimentacion", tipo_arena="gruesa", origen_arena="desierto")
grava1 = Grava(cantidad=50, precio_por_unidad=8.75, origen_grava="rio")
ladrillos1 = Ladrillos(cantidad=200, precio_por_unidad=0.80, lote="LDR001", tipo_ladrillo="cocido")
cemento1 = Cemento(cantidad=150, precio_por_unidad=3.25, marca="Apasco", uso="Revocado")

# Imprimir los objetos
print(arena1)
print(grava1)
print(ladrillos1)
print(cemento1)

#Costos totales
print(f"Costo total para arena: ${arena1.calcular_costo_total():.2f}")
print(f"Costo total para grava: ${grava1.calcular_costo_total():.2f}")
print(f"Costo total para ladrillos: ${ladrillos1.calcular_costo_total():.2f}")
print(f"Costo total para cemento: ${cemento1.calcular_costo_total():.2f}")

