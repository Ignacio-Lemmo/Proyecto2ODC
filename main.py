#Funcion principal del proyecto:
def main():

    #Importar todas las funciones del documento functions:
    import functions

    #Ofrecerle al usuario las opciones disponibles:
    option = input("""
        Bienvenido a nuestra tienda de historietas ComicWorld!
        Ingresa el numero de la accion que desee realizar:
        
        1. Registrar una nueva historieta.
        2. Consultar las historietas registradas.
        3. Comprar una historieta.
        4. Reabastecer el stock de alguna historieta.
        5. Eliminar una historieta del inventario.
        6. Actualizar el inventario.
        7. Salir.
        
        """)

    #Validar la opcion ingresada:
    option = functions.check_option(option)

    #Dependiendo del valor de la opcion se llama a una funcion:
    if (option == "1"):
        new_comic = function.register()
    elif (option == "2"): 
        function.consult()
    elif (option == "3"):
        function.buy()
    elif (option == "4"):
        function.restock()
    elif (option == "5"):
        function.delete()
    elif (option == "6"):
        function.update()
    elif (option == "7"):
        exit()

if __name__ == "__main__":
    main()