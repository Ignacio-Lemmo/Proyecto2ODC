import Comics

#Verificar la opcion ingresada:
def check_option(option):
    while (option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7"):
        option = input("Ingrese una opcion valida (1, 2, 3, 4, 5, 6 o 7): ")
    return option

#Verificar serial de la historieta:
def check_serial (serial, serial_list):
    while (len(serial) != 8 or serial in serial_list):
        serial = input("Por favor ingrese un numero serial unico de 8 digitos: ")
    return serial

#Verificar el Titulo de la historieta:
def check_title (title, title_list):
    while (len(title)>40 or len(title)<1):
        title = input("Ingrese un titulo valido para la historieta (maximo 40 caracteres): ")
    return title

#Verificar el precio de la historieta: 
def check_price(price):
    while (len(price)>3 or len(price)<1 or (type(price)!= int and type(price)!=float)):
        price = input("Ingrese un precio valido (maximo 3 digitos): ")
    return price

#Verificar el stock de la historieta: 
def check_stock(stock):
    while (len(stock)>2 or len(stock)<1 or (type(stock)!= int and type(stock)!=float)):
        stock = input("Ingrese un numero de Stock valido (maximo 2 caracteres): ")
    return stock

#Registrar una nueva historieta:
def register():
    #Ingresar y validar serial:
    serial: input("Ingrese el numero serial de la nueva historieta: ")
    serial = check_serial(serial, serial_list)
    #Ingresar y validar titulo:
    title = input("Ingrese el titulo de la nueva historieta: ")
    title = check_title(title, title_list)
    #Ingresar y validar precio:
    price = input("Ingrese el precio de la nueva historieta: ")
    price = check_price(price)
    #Ingresar y validar el stock:
    stock = input("Ingrese el stock de la nueva historieta: ")
    stock = check_stock(stock)
    #Crear nueva historieta:
    new_comic = Comics.Comics(serial, title, price, stock)
    return new_comic

#Consultar inventario de historietas:
def consult():
    pass

#Comprar historietas:
def buy():
    pass

#Reabastecer el inventario:
def restock():
    pass

#Eliminar historieta:
def delete():
    pass

#Actualizar inventario:
def update():
    pass