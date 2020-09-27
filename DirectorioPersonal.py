#Elaborar un programa que capture una serie de datos personales: matricula
#La matricula va a ser un entero de 7 posiciones, nombre completo (texto de hasta 40 posiciones),
#Fecha de nacimiento(dd/mm/aaaa), telefono(99-9999-9999) y correo electronico en formato válido.
#Por el momento no hacer validaciones
#Almacenar cada dato en una lista, y al final, cuando ya no se desee capturar más datos,
#mostrar lo capturado de la siguiente manera:
#MATRICULA: (dato)
#NOMBRE: (dato)
#EDAD: (dato)
#CONTACTO: Tel: (dato) Correo: (dato)
matriculas=[]
nombres=[]
fechas_nacimiento=[]
telefonos=[]
emails=[]
while True:
    matricula=[]
    matricula=input("Ingrese su matricula: ")
    matriculas.append(matricula)
    nombre=input("Ingrese su nombre completo: ")
    nombres.append(nombre)
    fecha_nacimiento=input("Ingrese su fecha de nacimiento: ")
    fechas_nacimiento.append(fecha_nacimiento)
    telefono=input("Ingrese su telefono: ")
    telefonos.append(telefono)
    email=input("Ingrese su correo electrónico: ")
    emails.append(email)

    salida=input("Deseas salir? (S/N): ")
    if salida.upper()=="S":
        break

posicion=0
for x in nombres:
    print(x)
    print(matriculas[posicion])
    posicion+=1 #Incrementador
