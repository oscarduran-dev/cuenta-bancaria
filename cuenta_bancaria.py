#cuenta bancaria
#creanod la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo):
        #inicializando la cuenta con titular y saldo inicial
        self.titular = titular
        self.saldo = saldo
    
    #función que simula depositar una cantidad positiva y muestra el saldo actualizado
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Deposito confirmado. Su nuevo saldo es: ${self.saldo}\n----------------------------")
        else:
            print("El monto debe ser mayor que cero.\n----------------------------")
        
    #función que simula realizar un retiro de efectivo si el saldo disponible es suficiente    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Lo siento. No cuentas con el saldo suficiente para realizar esta transacción. \n----------------------------")
        else:
            if cantidad > 0:
                self.saldo -= cantidad
            else:
                print("El monto debe ser mayor que cero.\n----------------------------")
            print(f"Operación realizada con éxito. Tu saldo restante es de: ${self.saldo}\n----------------------------")
           
    #función que muestra el saldo diponible            
    def mostrar_saldo(self):
        print(f"Tu saldo actual es de: ${self.saldo}\n----------------------------")
        

#solicitando datos iniciales del usuario        
titular = input("Ingresa tu nombre: ")
saldo = float(input("Ingresa tu saldo: "))

#instanciando la clase CuentaBancaria
cuenta1 = CuentaBancaria(titular,saldo)

#creando un bucle para operar la cuenta hasta que el usuario seleccione la opción de salir
while True:
    try:
        opcion = int(input("""Selecciona la operación que quieres realizar.
          1. Para depositar
          2. Para Retirar
          3. Mostrar Saldo
          4. Salir
          """))
    except ValueError:
        print("Por favor ingresa un número del 1 al 4.\n----------------------------")
        continue
    if opcion == 1:
        try:
            cantidad = float(input("Ingrese el monto a depositar: "))
            cuenta1.depositar(cantidad)
        except ValueError:
            print("Por favor ingresa un número válido.\n----------------------------")
    elif opcion == 2:
        try:
            cantidad = float(input("Ingrese el monto a retirar: "))
            cuenta1.retirar(cantidad)
        except ValueError:
            print("Por favor ingresa un número válido.\n----------------------------")
    elif opcion == 3:
        cuenta1.mostrar_saldo()
    elif opcion == 4:
        print(f"Has seleccionado la opcion de salir. Hata luego, {titular}, ten un buen día. ")
        break
    else:
        print("Ingrese un valor correcto: \n----------------------------")
