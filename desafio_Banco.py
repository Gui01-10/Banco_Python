menu ="""
Ingresse o que deseja fazer hoje: 

[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair

=>"""

saldo = 1500
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(f"Hola, por favor me diga seu nome:")
nome = input()
print(f"\n{nome}, Bem Vinda ao melhor Banco do mundo!!")

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input(f"{nome}, ingrese o valor do seu Depósito: R$ "))

        if valor >0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito feito com sucesso")
        else:
            print("Valor inválido")    

    elif opcao == "S":
        valor = float(input(f"{nome}, ingrese o valor do seu Saque: R$"))

        if valor > limite:
            print ("Valor máximo permitido por saque é R$500.00")

        elif valor > saldo:
           print (f"\n{nome}, Saldo insuficiente mas peça para o maridão que ele resolve.") 

        elif numero_saques >= LIMITE_SAQUES:
            print(f"\n{nome}, Limite de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque feito com sucesso")

        else:
            print("Valor inválido")
        

    elif opcao == "E":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")


    elif opcao == "X":
        print("Até mais, Lindona! Obrigado por usar o melhor banco do mundo. 💖")
        break
    else:
        print("Operacao inválida, por favor selecione novamenta a operacao desejada.")


"""
menu = \n
Ingrese la operación que desea realizar hoy:

  [D] Depositar
  [R] Retirar
  [E] Ver Extracto
  [S] Salir

=>

saldo = 1500
limite = 1000
extracto = ""
numero_retiros = 0
LIMITE_RETIROS = 3

print("Hola, por favor, indíqueme su nombre:")
nombre = input()
print(f"\n{nombre}, ¡Bienvenid@ al mejor banco del mundo!")

while True:
    opcion = input(menu).upper()

    if opcion == "D":
        valor = float(input(f"{nombre}, ingrese el monto a depositar: $ "))

        if valor > 0:
            saldo += valor
            extracto += f"Depósito: $ {valor:.2f}\n"
            print("\nDepósito realizado con éxito.")
        else:
            print("Monto inválido.")

    elif opcion == "R":
        valor = float(input(f"{nombre}, ingrese el monto a retirar: $ "))

        if valor > limite:
            print("El monto máximo permitido por retiro es de $500.00.")
        elif valor > saldo:
            print(f"\n{nombre}, saldo insuficiente. Por favor, verifique su cuenta.")
        elif numero_retiros >= LIMITE_RETIROS:
            print(f"\n{nombre}, ha excedido el número máximo de retiros permitidos.")
        elif valor > 0:
            saldo -= valor
            extracto += f"Retiro: $ {valor:.2f}\n"
            numero_retiros += 1
            print("\nRetiro realizado con éxito.")
        else:
            print("Monto inválido.")

    elif opcion == "E":
        print("\n========== EXTRACTO ==========")
        print(extracto if extracto else "No se han realizado movimientos.")
        print(f"\nSaldo actual: $ {saldo:.2f}")
        print("==============================")

    elif opcion == "S":
        print("¡Hasta luego! Gracias por utilizar el mejor banco del mundo. 💖")
        break

    else:
        print("Operación inválida. Por favor, seleccione nuevamente la operación deseada.")






from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, cuenta):
        pass

class Deposito(Operacion):
    def ejecutar(self, cuenta):
        valor = float(input(f"{cuenta.nombre}, ingrese el monto a depositar: $ "))
        if valor > 0:
            cuenta.saldo += valor
            cuenta.extracto.append(f"Depósito: $ {valor:.2f}")
            print("\nDepósito realizado con éxito.")
        else:
            print("Monto inválido.")

class Retiro(Operacion):
    def ejecutar(self, cuenta):
        valor = float(input(f"{cuenta.nombre}, ingrese el monto a retirar: $ "))
        if valor > cuenta.limite:
            print("El monto máximo permitido por retiro es de $500.00.")
        elif valor > cuenta.saldo:
            print(f"\n{cuenta.nombre}, saldo insuficiente. Por favor, verifique su cuenta.")
        elif cuenta.numero_retiros >= cuenta.LIMITE_RETIROS:
            print(f"\n{cuenta.nombre}, ha excedido el número máximo de retiros permitidos.")
        elif valor > 0:
            cuenta.saldo -= valor
            cuenta.extracto.append(f"Retiro: $ {valor:.2f}")
            cuenta.numero_retiros += 1
            print("\nRetiro realizado con éxito.")
        else:
            print("Monto inválido.")

class VerExtracto(Operacion):
    def ejecutar(self, cuenta):
        print("\n========== EXTRACTO ==========")
        if cuenta.extracto:
            for movimiento in cuenta.extracto:
                print(movimiento)
        else:
            print("No se han realizado movimientos.")
        print(f"\nSaldo actual: $ {cuenta.saldo:.2f}")
        print("==============================")

class OperacionFactory:
    @staticmethod
    def crear_operacion(opcion):
        operaciones = {
            "D": Deposito(),
            "R": Retiro(),
            "E": VerExtracto()
        }
        return operaciones.get(opcion.upper(), None)








class EntradaUsuario:
    def obtener_opcion(self):
        pass

class ConsolaAdapter(EntradaUsuario):
    def obtener_opcion(self):
        menu = \n
Ingrese la operación que desea realizar hoy:

  [D] Depositar
  [R] Retirar
  [E] Ver Extracto
  [S] Salir

=>
        return input(menu).upper()






class EstrategiaValidacion(ABC):
    @abstractmethod
    def validar(self, cuenta, valor):
        pass

class ValidacionRetiro(EstrategiaValidacion):
    def validar(self, cuenta, valor):
        if valor > cuenta.limite:
            print("El monto máximo permitido por retiro es de $500.00.")
            return False
        elif valor > cuenta.saldo:
            print(f"\n{cuenta.nombre}, saldo insuficiente. Por favor, verifique su cuenta.")
            return False
        elif cuenta.numero_retiros >= cuenta.LIMITE_RETIROS:
            print(f"\n{cuenta.nombre}, has excedido el número máximo de retiros permitidos.")
            return False
        elif valor <= 0:
            print("Monto inválido.")
            return False
        return True





class Cuenta:
    LIMITE_RETIROS = 3

    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 1500
        self.limite = 1000
        self.extracto = []
        self.numero_retiros = 0


def main():
    nombre = input("Hola, por favor, indíqueme su nombre: ")
    cuenta = Cuenta(nombre)
    entrada = ConsolaAdapter()

    print(f"\n{cuenta.nombre}, ¡Bienvenid@ al mejor banco del mundo!")

    while True:
        opcion = entrada.obtener_opcion()
        if opcion == "S":
            print("¡Hasta luego! Gracias por utilizar el mejor banco del mundo. 💖")
            break

        operacion = OperacionFactory.crear_operacion(opcion)
        if operacion:
            operacion.ejecutar(cuenta)
        else:
            print("Operación inválida. Por favor, seleccione nuevamente la operación deseada.")

if __name__ == "__main__":
    main()
"""