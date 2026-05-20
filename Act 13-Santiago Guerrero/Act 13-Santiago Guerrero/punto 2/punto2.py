#2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada
#cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe
#finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un
#programa que lea los datos de las cuentas corrientes e informe:
#● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo,
#sabiendo que:
#○ Estado de la cuenta:
#○ “Acreedor” si el saldo es > 0.
#○ “Deudor” si el saldo es < 0.
#○ “Nulo” si el saldo es = 0.
#● b) La suma total de los saldos acreedores.

estadoDeCuenta=""
numeroDeCuenta=1
suma=0
while numeroDeCuenta>0:
    numeroDeCuenta=int(input("Ingrese el numero de cuenta, numero negativo para terminar"))
    saldoActual=int(input("Ingrese el sueldo actual"))

    if saldoActual>0:
        estadoDeCuenta="Acredor"

    if saldoActual<0:
            estadoDeCuenta="Deudor"

    if saldoActual==0:
            estadoDeCuenta="Nulo"

    if estadoDeCuenta=="Acredor":
          suma+=saldoActual

    print("Numero de cuenta: ", numeroDeCuenta, "Estado de cuenta: ", estadoDeCuenta)
print("El total de saldo de acredores es: ", suma)


