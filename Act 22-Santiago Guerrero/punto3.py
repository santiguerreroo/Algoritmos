"""Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
 Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: &quot;192.168.1.50&quot;) y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos)."""


def cargar():
    direcciones={}
    for i in range(4):
        ip=input(F"Ingrese la direccion IP {i+1} sospechosa:")
        lista=[]
        nomb=input(F"Ingrese el nombre del dispositivo cuya ip es {ip} : ")
        inten=int(input(F"Ingrese la cantidad de intentos fallidos tuvo:"))
        lista.append((nomb,inten))
        direcciones[ip]=lista
    return direcciones

def Imprimir(direcciones):
    print("Listado completo de ips sospechosos:")
    for ip in direcciones:
        print(F"En la direccion ip {ip}" )
        for nomb,inten in direcciones[ip]:
           print(F"El nombre de dispositivo es {nomb} y tiene una cantidad de {inten} intentos fallidos.")

def bloqueo(direcciones):
    print("Las direcciones IP bloqueadas con mas de 5 intentos fallidos son:")
    for ip in direcciones:
        for nomb,inten in direcciones[ip]:
            if inten>5:
                print(F"La IP{ip} fue bloqueada debido a sus mas de 5 intentos fallidos.")
direcciones=cargar()
Imprimir(direcciones)
bloqueo(direcciones) 
