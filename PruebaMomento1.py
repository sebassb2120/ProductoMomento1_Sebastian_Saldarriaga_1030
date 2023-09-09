class Usuario:
    def __init__(self, nombre, numeroTarjeta):
        self.nombre = nombre
        self.numeroTarjeta = numeroTarjeta

class CiclasPrestadas:
    def __init__(self, usuario, origen, destino):
        self.usuario = usuario
        self.origen = origen
        self.destino = destino

list_usuario = []
list_ciclasPrestadas = []

def registroUsuario(nombre, numeroTarjeta):
    usuario = Usuario(nombre, numeroTarjeta)
    list_usuario.append(usuario)
    

def usarBicicleta(numeroTarjeta, origen, destino):
    usuario = None
    for u in list_usuario:
        if u.numeroTarjeta == numeroTarjeta:
            usuario = u
            break


    if usuario:
        ciclasPrestada = CiclasPrestadas(usuario, origen, destino)
        list_ciclasPrestadas.append(ciclasPrestada)
        print(f"{usuario.nombre} ha tomado una bicicleta en préstamo de {origen} a {destino}.")
    
    else:
        print("Usuario no encontrado. Verifique el número de tarjeta.")


def consultar_usuario():
    print("listado de usuario")
    for usuario in list_usuario:
        print(f"Nombre: {usuario.nombre}\n Numeroo de Tarjeta: {usuario.numeroTarjeta}")


def consultar_bicicleta():
    print("listado de biciletas prestadas")
    for bicletas in list_ciclasPrestadas:
                print(f"Nombre: {bicletas.usuario.nombre}\n origen: {bicletas.origen}\n destino: {bicletas.destino}")





registroUsuario("sebas", "1234")
usarBicicleta("1234", "gta", "medellin")
consultar_usuario()
consultar_bicicleta()




