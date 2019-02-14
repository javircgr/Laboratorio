class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio

class Medicamento(Producto):
    def __init__(self,nombre, precio, composicion, porcentaje):
        self.nombre = nombre
        self.precio = precio
        self.composicion = composicion
        self.porcentaje = porcentaje

    def informacion(self):
        return self.nombre, self.precio, self.composicion, self.porcentaje



vendas = Producto('vendas', 4)
tiritas = Producto('tiritas', 2)
aspirina = Medicamento('aspirina', 8, 'acido 1', 0.30)
ibuprofeno = Medicamento('ibuprofeno', 6, 'acido2', 0.40)
nombres = []
nombres.append(vendas)
nombres.append(tiritas)
nombres.append(aspirina)
nombres.append(ibuprofeno)

class Laboratorio():
    def __init__(self, laboratorio, prod1, prod2 ,med1, med2):
        self.laboratorio = laboratorio
        self.prod1 = prod1
        self.prod2 = prod2
        self.med1 = med1
        self.med2 = med2
    def informacionlab(self):
        return self.laboratorio, self.prod1, self.prod2 ,self.med1, self.med2

Bayer = Laboratorio('Bayer', nombres[0], nombres[1], nombres[2], nombres[3])
print('En Bayer tienen los siguientes productos: ', Bayer.prod1.nombre, Bayer.prod2.nombre)
print('Ademas de los medicamentos: ', Bayer.med1.nombre, Bayer.med2.nombre)
print( Bayer.med1.nombre, "contiene", Bayer.med1.porcentaje, "de", Bayer.med1.composicion)
print( Bayer.med2.nombre, "contiene", Bayer.med2.porcentaje, "de", Bayer.med2.composicion)
