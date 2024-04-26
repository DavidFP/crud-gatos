class animal:
    def __init__(self, nombre=None, edad=None, color=None, peso=None):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad=edad
        if color:
            self.color=color
        if peso:
            self.peso=peso