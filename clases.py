class armamento:
    def __init__ (self, daño, tipo, calidad):
        self.daño = daño
        self.tipo = tipo
        self.calidad = calidad
melee = armamento("120", "cuerpo a cuerpo", "Legendario")
rango = armamento("100", "daño a distancia", "Despiadado")
mago = armamento("70", "magia", "Roto")
invocador= armamento("25", "invocacion", "Mitico")

print(melee.tipo)
print(rango.daño)
print(mago.calidad)
print(invocador.daño)