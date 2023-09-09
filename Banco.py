class Cuenta:
    def __init__(self, persona, saldo):
        print("----- bienvenido a Bancolombia ------")

        self.titularBancario = f"Hola {persona}, Susaldo es de {saldo}"
        self.saldoCuenta = saldo
        

    def ingresarDinero (self, monto):
        self.saldoCuenta += monto
        print(f"Saldo disponible {self.saldoCuenta}")

    def retirarDinero (self, monto):
        if self.saldoCuenta >= monto:
            self.saldoCuenta -= monto
            print(f"Retiro exitoso, Saldo disponible {self.saldoCuenta}")
        
        else:
             print(f"No tiene saldo suficiente, Su saldo es de {self.saldoCuenta}")

prueba = Cuenta("Sebastian", 12000000)

print(prueba.titularBancario)
print(prueba.ingresarDinero(5000000))
print(prueba.retirarDinero(11000000))