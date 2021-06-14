import re

class Paciente:
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __apellido=None
    __nombre=None
    __telefono=None
    __altura=None
    __peso=None
    def __init__(self,apellido,nombre,tel,altura,peso) -> None:
        self.__apellido=self.requerido(apellido, 'Apellido es un valor requerido')
        self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__telefono = self.formatoValidoTel(tel, Paciente.telefonoRegex, 'Teléfono no tiene formato correcto')
        self.__altura=self.formatoValidoNum(altura, 'Altura no tiene formato numerico')
        self.__peso=self.formatoValidoNum(peso, 'Peso no tiene formato numerico')
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def requerido(self,atributo,mensaje):
        if not atributo:
            raise ValueError(mensaje)
        return atributo
    def formatoValidoTel(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor   
    def formatoValidoNum(self, valor, mensaje):
        if not valor or not valor.isnumeric():
            raise ValueError(mensaje)
        return valor   
    def getIMC(self):
        imc=float(float(self.getPeso()) / (((float(self.getAltura()))/100)**2))
        return imc
    def getComposicion(self):
        imc=self.getIMC()
        retorna=None
        if imc<18.5:
            retorna=('Peso inferior al normal')
        elif imc>=18.5 and imc<25:
            retorna=('Peso Normal')
        elif imc>=25.0 and imc<30:
            retorna=('Peso superior al normal')
        elif imc>=30:
            retorna=('Obesidad')
        return retorna
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        apellido=self.__apellido,
                        nombre=self.__nombre,
                        tel=self.__telefono,
                        altura=self.__altura,
                        peso=self.__peso
                        )
                )
        return d