import random 


print("_________________Login________________________-")

# Base de datos ficticia de usuarios
users_database = [
    {"id": 1, "email": "sebas@gmail.com", "celular": "2307699402", "password": "sebas123"},
    {"id": 2, "email": "camilo@gmail.com", "celular": "2891388", "password": "milo123"},
]



# Función para validar el inicio de sesión

def login():

    #Generador de captcha():
    def funcaptcha():
        captcha = ''.join(random.choices('0123456789', k=6))
        return captcha
    
    print("Bienvenido, Resgistrate")
    input_type = input("Ingrese 'email' o 'celular': ")
    input_value = input("Ingrese su correo o telefono: ")
    input_password = input("Ingrese su contraseña: ")
    input_captcha = input(f"Ingrese el captcha mostrado {funcaptcha()} : ")



    user = None
    for u in users_database:
        if (input_type == 'email' and u['email'] == input_value) or (input_type == 'celular' and u['celular'] == input_value):
            user = u
            break

    if user and user["password"] == input_password and input_captcha == funcaptcha():
        print("¡BIENVENIDO!")
    
    else:
        print("Inicio de sesión incorrecto, Vuelva a intentarlo")
    
login()



############################################ Fin del Login ########################################

######################################### Incio del Menu ########################################

def juego():

    # Jueguito ejercicio

    vidas = 5

    puntos = 0

    while(vidas != 0):

        num=random.randint(0,9)

        if num == 0:
            vidas -=1
            print(f'vidas: {vidas}')
        
        else:
            puntos +=1
            print(f"puntos: {puntos}")


def credito():

    print("Bienvenido a Calcula tu Credito")

    total_compra = float(input("Ingresa el total a pagar: "))
    cuotas = int(input("Ingresa el total cuotas que de seas pagar: "))

    saldo_pendiente = total_compra

    while saldo_pendiente > 0:
        
        monto_cuotas = total_compra / cuotas
        print(f"Debes hacer un abono de {monto_cuotas} por cada cuota")

        disminucion_cuota = monto_cuotas / cuotas

        print("------------------------------------------------------")

        print("Saldo pendiente: $", round(saldo_pendiente, 2))
        print("Cuota mensual: $", round(monto_cuotas, 2))
        print("Disminución de la cuota: $", round(disminucion_cuota, 2))

        saldo_pendiente -= monto_cuotas
        monto_cuotas -= disminucion_cuota

        print('------------------------------------------------')

        print("El saldo ha sido pagado en su totalidad")


def pagar():
      
    print("Bienvenido a la aplicación de pago y servicio.")
    
    pagar_cuenta = input("¿Desea pagar la cuenta? (sí/no): ")

    if pagar_cuenta.lower() == "si":
        incluir_servicio = input("¿Desea incluir el servicio? (sí/no): ")
        if incluir_servicio.lower() == "si":
            monto = float(input("Ingrese el monto de la cuenta: "))
            monto_total = monto * 1.1
            print(f"El monto total con el servicio es: {monto_total}")
        
        else:
            print("El monto de la cuenta no incluye el servicio.")
    else:
        seguir_compra = input("¿Desea comprar algo más? (sí/no): ")
        if seguir_compra.lower() == "si":
            print("¡Disfrute de su compra adicional!")
        else:
            print("Gracias por usar la aplicación.")




def muenu_principal():

    while True:
        print("---- Menu Principal----")
        print("1. Juego")
        print("2. Credito")
        print("3. PagoCuenta")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            juego()

        elif opcion == "2":
            credito()

        elif opcion == "3":
            pagar()

        elif opcion == "4":
                muenu_principal()
            
        else:
            print("Opcion invalida, Seleccione una valida")

muenu_principal()     

