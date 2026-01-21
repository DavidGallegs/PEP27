from abc import ABC, abstractmethod

# Clase principal abstracta
class Producto(ABC):
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precios = precio

    @abstractmethod
    def calcular_precio_final(self):
        pass

    @property
    def nombre(self):
        return self.nombre
    
    @property
    def precio(self):
        return self.precio
    
    @precio.setter
    def add_precio(self, precio):
        if not isinstance(precio, float):
            raise TypeError("El precio debe ser un número")
        if precio  < 0:
            raise ValueError("El precio debe ser un número mayor que 0")
        self.precio = precio

# Clase Hija
class DiscoDuro(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def calcular_precio_final(self):
        return 
    


# Clase Hija 2
class Memoria(Producto):
    def __init__(self, nombre, precio, capacidad):
        super().__init__(nombre, precio)
        self.capacidad = capacidad

    def calcular_precio_final(self):
        return 

    