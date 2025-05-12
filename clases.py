#Gomez Lopez Sergio
class armamento:
    def __init__ (self, daño, tipo, calidad): #se define la funcion 
        self.daño = daño
        self.tipo = tipo
        self.calidad = calidad
melee = armamento("120", "cuerpo a cuerpo", "Legendario") #se colocan los valores de cada clase
rango = armamento("100", "daño a distancia", "Despiadado")
mago = armamento("70", "magia", "Roto")
invocador= armamento("25", "invocacion", "Mitico")

#se manda un print que pondra todos los atributos que se nombraron anteriormente
print(melee.tipo)
print(rango.daño)
print(mago.calidad)
print(invocador.daño)
