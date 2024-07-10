class Usuarios():
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def getTel(self):
        return self.tel
    
    def setTel(self, tel):
        self.tel = tel

    def info_usuario(self):
        print(f"Nombre: {self.getNombre()}, Direccion: {self.getDireccion()}, Telefono: {self.getTel()}")
    
class Clientes(Usuarios):
    def __init__(self, nombre, direccion, tel, num_cliente):
        super().__init__(nombre, direccion, tel)
        self.__num_cliente = num_cliente

    def getNumCliente(self):
        return self.__num_cliente
    
    def setNumCliente(self, num_cliente):
        self.__num_cliente = num_cliente
    
    def info_usuario(self):
        print(f"Nombre: {self.getNombre()}, Direccion: {self.getDireccion()}, Telefono: {self.getTel()}, Numero de cliente: {self.getNumCliente()}")

class Empleados(Usuarios):
    def __init__(self, nombre, direccion, tel, _salario, _num_empleado, _tipo):
        super().__init__(nombre, direccion, tel)
        self._salario = _salario
        self._num_empleado = _num_empleado
        self._tipo = _tipo

    def getSalario(self):
        return self._salario

    def setSalario(self, _salario):
        self._salario = _salario

    def getNumEmpleado(self):
        return self._num_empleado

    def setNumEmpleado(self, _num_empleado):
        self._num_empleado = _num_empleado

    def getTipo(self):
        return self._tipo
    
    def setTipo(self, _tipo):
        self._tipo = _tipo

    def info_usuario(self):
        print(f"Nombre: {self.getNombre()}, Direccion: {self.getDireccion()}, Telefono: {self.getTel()}, Salario: {self.getSalario()}, Numero de empleado: {self.getNumEmpleado()}, Tipo: {self.getTipo()}")   