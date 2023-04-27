class Agenda:
    
    def __init__(self):
        self.contactos=[]
    
    def insertar_contacto(self,nombre,apellido,telefono,email):
        self.contactos.append([nombre,apellido,telefono,email])
    
    def buscar(self,nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                print(contacto)

    def eliminar_contacto(self,nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                self.contactos.remove(contacto)
                print("Se ha eliminado el contacto")
    
    def modificar(self,nombre,telefono,email):
            for contacto in self.contactos:
                if contacto[0] == nombre:
                    contacto[2] = telefono
                    contacto[3] = email
        
agenda = Agenda()
contactos=[]
while True:
    print("------------------------")
    print("1.- Ingresar contacto")
    print("2.- Eliminar contacto")
    print("3.- Modificar contacto")
    print("4.- Buscar contacto")
    print("5.- Salir")
    print("------------------------")
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        telefono = input("Ingrese telefono: ")
        email = input("Ingrese email: ")
        agenda.insertar_contacto(nombre,apellido,telefono,email)
        agenda.buscar(nombre)
    elif opcion == 2:
        nombre = input("Ingrese nombre: ")
        agenda.eliminar_contacto(nombre)
    elif opcion == 3:
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese telefono: ")
        email = input("Ingrese email: ")
        agenda.modificar(nombre,telefono,email)
        agenda.buscar(nombre)
    elif opcion == 4:
        nombre = input("Ingrese nombre: ")
        agenda.buscar(nombre)
    elif opcion == 5:
        break
        