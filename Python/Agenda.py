import pymongo

class Agenda:
    
    def __init__(self,cliente,nombre_bd,nombre_collection):
        self.cliente = cliente
        self.db = self.cliente[nombre_bd]
        self.collection = self.db[nombre_collection]
    
    def insertar_contacto(self,nombre,apellido,telefono,email):
        self.collection.insert_one({
            "nombre":nombre,
            "apellido":apellido,
            "telefono":telefono,
            "email":email
        })

    def eliminar_contacto(self,nombre):
        self.collection.delete_one({"nombre":nombre})

    def modificar(self,nombre,telefono,email):
        self.collection.update_one({"nombre":nombre},{"$set":{"telefono":telefono,"email":email}})

    def buscar(self,nombre):
        return self.collection.find_one({"nombre":nombre})

cliente = pymongo.MongoClient("mongodb://localhost:27017/")    
agenda = Agenda(cliente,'agenda','contactos')
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
    elif opcion == 2:
        nombre = input("Ingrese nombre: ")
        agenda.eliminar_contacto(nombre)
    elif opcion == 3:
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese telefono: ")
        email = input("Ingrese email: ")
        agenda.modificar(nombre,telefono,email)
    elif opcion == 4:
        nombre = input("Ingrese nombre: ")
        print(agenda.buscar(nombre))
    elif opcion == 5:
        break
        
             

