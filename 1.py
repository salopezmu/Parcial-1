class biblioteca:
    def __init__(self,libros,usuarios,categorias):
        self._libros=libros
        self._usuarios=usuarios
        self.categorias=categorias
        
    def menu(self):
        while True:
            print("----------MENU----------")
            print("1.registrar nuevos libros")
            print("2.registrar nuevos usuarios")
            print("3.ver las categorias de libros ")
            print("4.salir")
            select=input("digite el numero de la accion que desea realizar\n")
            if select=="1":
                libros=[]
                l=input("ingrese el nombre de su libro\n")
                libros.append(l)
                print(f"el libro registrado fue {libros}")
            if select=="2":
                usuario=[]
                u=input("ingrese su nombre\n")
                usuario.append(u)
                print(f"el usuario registrado fue {usuario}")
            if select=="3":
                categorias=["accion","fisica","quimica","arte"]
                print(f"las categorias de libros existentes son:")
                c=1
                for i in categorias:
                    print(f"{c}.{categorias[c-1]}")
                    c+=1
            if select=="4":
                break
            else: print("usted no digito el numero de alguna de loas opciones")
biblioteca.menu(biblioteca)
