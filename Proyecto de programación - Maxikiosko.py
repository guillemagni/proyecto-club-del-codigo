'''
    Protecto de programación: Maxikiosco
    Autor: Magni, Guillermo
    Fecha: 3/11/2020
    Club del Código
'''
import os
import sys

'''
    Variables:
    -productos: una lista general que se va a encargar de guardar todos los productos cargados en el sistema
    -ventas: una lista general que se va a encargar de guardar todas las ventas realizadas en el sistema
'''

productos = []
ventas = []


def menu_general():
    os.system('cls')
    op = None
    while op != 3:
        print('### Maxikiosko ###')
        print('-'*20)
        print('1. Administrar productos')
        print('2. Administrar ventas')
        print('3. Salir')
        print('-'*20)
        op = int(input('Cargue una opción: '))
        while op < 1 and op > 3:
            print()
            print('ERROR! -> Se cargo un valor que no es válido!')
            op = int(input('Cargue una opción(entre 1 y 3): '))
        
        #Control de opción y ejecución
        if op == 1:
            menu_productos()
        elif op == 2:
            pass
        else:
            print()
            print('Fin del programa. ¡Gracias por trabajar con nosotros!')
            sys.exit() #Cerrar el programa
            print()


def menu_productos():
    os.system('cls')
    op = None
    while op != 3:
        print('### Administrar productos ###')
        print('-'*20)
        print('1. Cargar un producto nuevo')
        print('2. Listar productos cargados')
        print('3. Actualizar stock de un producto')
        print('4. Modificar un producto')
        print('5. Dar de baja un producto')
        print('6. Volver al menú principal')
        print('-'*20)
        op = int(input('Ingrese una opción: '))
        while op < 1 and op > 6:
            print()
            print('ERROR! -> Se cargo un valor que no es válido!')
            op = int(input('Cargue una opción(entre 1 y 6): '))
        
        #Control de opción y ejecución
        if op == 1:
            cargar_producto()
        elif op == 2:
            mostrar_productos_cargados()
        elif op == 3:
            actualizar_stock_producto()
        elif op == 4:
            modificar_producto()
        elif op == 5:
            dar_baja_producto()
        else:
            menu_general()

def cargar_producto():
    os.system('cls')
    op = None
    print('### Carga de producto ###')
    print('-'*20)
    print('1. Cargar producto')
    print('2. Volver a la pantalla anterior')
    print('-'*20)
    op = int(input('Ingrese una opción: '))
    while op < 1 and op > 2: 
        print()
        print('ERROR! -> Se cargo un valor que no es válido!')
        op = int(input('Cargue una opción(entre 1 y 2): '))
    
    if op == 1:
        os.system('cls')
        cantidad_a_cargar = int(input('¿Cuántos productos desea cargar?: '))
        for i in range(cantidad_a_cargar):
            print('-'*20)
            print(f'Carga de procuto - N° {i+1}')
            print()
            nombre = input('Ingrese el nombre del producto: ')
            precio = float(input('Ingrese el precio del producto: '))
            stock = int(input('Ingrese la cantidad de stock disponible: '))
            descripcion = input('Ingrese la descripción del producto (opcional): ')
            nuevo_producto = [nombre.lower(), precio, stock, descripcion]
            productos.append(nuevo_producto)
        print()
        print('¡Producto/s cargado/s con éxito!')
        input('Aprete enter para volver al menú anterior...')
        menu_productos()
    else:
        menu_productos()

def mostrar_productos_cargados():
    os.system('cls')
    print('### Listado de productos cargados ###')
    for codigo in range(len(productos)):
        print('-'*20)
        print(f'Producto N° {codigo}:')
        print(f'Nombre: {productos[codigo][0].title()}')
        print(f'Precio: ${productos[codigo][1]}')
        print(f'Stock disponible: {productos[codigo][2]}')
        print(f'Descripción del producto: {productos[codigo][3]}')
    print('### Fin del listado de productos ###')
    input('Presione enter para volver a la pantalla anterior')
    menu_productos()

'''
    La función permite buscar un producto por su código, si lo encuentra, muestran la información del mismo y pide el nuevo monto.
    Actualiza el valor actual del stock agregando la nueva cantidad ingresada.
'''
def actualizar_stock_producto():
    os.system('cls')
    print('### Actualización de stock de un producto ###')
    control_codigo_producto = False

    r = control_codigo()
    if r == False:
        encontrado = buscar_codigo()
        if encontrado == True:
            control_codigo_producto = True
    else:
        control_codigo_producto =  True

    if control_codigo_producto == True:
        codigo_a_buscar = int(input('Ingrese el código del producto que desea buscar: '))
        for codigo in range(len(productos)):
            if codigo == codigo_a_buscar:
                os.system('cls')
                print('¡Producto encontrado!')
                print('Información:')
                print(f'Producto N° {codigo}:')
                print(f'Nombre: {productos[codigo][0]}')
                print(f'Precio: ${productos[codigo][1]}')
                print(f'Stock disponible: {productos[codigo][2]}')
                print(f'Descripción del producto: {productos[codigo][3]}')
                print('-'*20)
                nuevo_stock = int(input('Ingrese el stock a agregar: '))
                productos[codigo][2] =  productos[codigo][2] + nuevo_stock
                print()
                print(f'¡Stock actualizado con éxito! El nuevo stock disponible es de: {productos[codigo][2]}')
                break #cortamos el for ya que no tendría sentido seguir la búsqueda
    else:
        print()
        print('No se encontró un producto con ese código.')
    input('Presione enter para volver a la pantalla anterior')
    menu_productos()

def modificar_producto():
    os.system('cls')
    print('### Modificar producto ###')
    r = control_codigo()
    control_codigo_producto = False
    if r == False:
        encontrado = buscar_codigo()
        if encontrado == True:
            control_codigo_producto = True
    else:
        control_codigo_producto =  True

    if control_codigo_producto == True:
        codigo_a_buscar = int(input('Ingrese el código del producto que desea buscar: '))
        for codigo in range(len(productos)):
            if codigo == codigo_a_buscar:
                os.system('cls')
                print('¡Producto encontrado!')
                print('Información:')
                print(f'Producto N° {codigo}:')
                print(f'Nombre: {productos[codigo][0]}')
                print(f'Precio: ${productos[codigo][1]}')
                print(f'Stock disponible: {productos[codigo][2]}')
                print(f'Descripción del producto: {productos[codigo][3]}')
                print('-'*20)
                mod = int(input('¿Que dato desea modificar? 1-Nombre, 2-Precio, 3-Descripcion, 4-Salir: '))
                while mod != 4:
                    if mod == 1:
                        nuevo_nombre = input('Ingrese el nuevo nombre del producto: ')
                        productos[codigo][0] = nuevo_nombre
                        print('¡Nombre cambiado con éxito!')
                    elif mod == 2:
                        nuevo_precio = input('Ingrese el nuevo precio del producto: ')
                        productos[codigo][1] = nuevo_precio
                        print('Precio cambiado con éxito!')
                    elif mod == 3:
                        nueva_descripcion = input('Ingrese el nuevo descripción del producto: ')
                        productos[codigo][3] = nueva_descripcion
                        print('¡Descripción cambiada con éxito!')
                    mod = int(input('¿Desea modificar otro valor? 1-Nombre, 2-Precio, 3-Descripcion, 4-Salir: '))
                input('Presione enter para volver al menú anterior')
                menu_productos()

         
def dar_baja_producto():
    os.system('cls')
    print('### Dar de baja un producto ###')
    r = control_codigo()
    control_codigo_producto = False
    if r == False:
        encontrado = buscar_codigo()
        if encontrado == True:
            control_codigo_producto = True
    else:
        control_codigo_producto =  True

    if control_codigo_producto == True:
        codigo_a_buscar = int(input('Ingrese el código del producto que desea buscar: '))
        codigo_encontrado = False
        for codigo in range(len(productos)):
            if codigo == codigo_a_buscar:
                codigo_encontrado = True
                break
        if codigo_encontrado:
            eliminado = productos.pop(codigo_a_buscar)
            print(f'El elemento cuyo código es {eliminado} fue dado de baja de la lista de productos!')
        else:
            print('No se encontró un producto con el código solicitado')


def control_codigo():
    r = input('¿Cónoce el código del producto al que desea actualizar el stock? [s/n]: ')
    while r != 's' and r != 'n':
        print()
        print('ERROR! -> Se cargo un valor que no es válido!')
        r = input('Cargue una opción("s" o "n"): ')
    if r == 's': return True
    else: return False

def buscar_codigo():
    buscar = input('Ingrese el producto que desea buscar: ')
    buscar = buscar.lower()
    encontrado = False
    resultados_busqueda = []
    codigo_seleccionado = None
    
    while encontrado != True:
        for i in range(len(productos)):
            if buscar in productos[i][0]:
                resultados_busqueda.append([productos[i][0],i])
                encontrado = True
        if encontrado == False:
            print()
            print('No se encontró ningún producto con alguna similitud.')
            r = input('¿Desea intentar de nuevo? [s/n]: ')
            while r != 's' and r != 'n':
                print()
                print('ERROR! -> Se cargo un valor que no es válido!')
                r = input('Cargue una opción("s" o "n"): ')
            if r == 's':
                buscar = input('Ingrese el producto que desea buscar: ')
                buscar = buscar.lower()
            else: break
    
    if encontrado == True:
        os.system('cls')
        print('### Resultados de la busqueda ###')
        for i in range(len(resultados_busqueda)):    
            print(f'{i+1}) Nombre del producto: {resultados_busqueda[i][0]} - Código: {resultados_busqueda[i][1]}') 
        print('-'*20)
        print()
        input('Precione enter para continuar')
        
    return encontrado

'''Seccion de venta'''
def menu_venta():
    os.system('cls')
    op = None
    while op != 3:
        print('### Menú de venta ###')
        print('-'*20)
        print('1. Registrar venta')
        print('2. Mostrar total recaudado')
        print('3. Volver al menú principal')
        print('-'*20)
        op = int(input('Ingrese una opción: '))
        while op < 1 and op > 3:
            print()
            print('ERROR! -> Se cargo un valor que no es válido!')
            op = int(input('Cargue una opción(entre 1 y 2): '))
        
        #Control de opción y ejecución
        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            menu_general()
        elif op == 4:
            pass
        elif op == 5:
            pass
        
def registrar_venta():
    os.system('cls')
    op = None
    while op != 3:
        print('### Registrar venta ###')
        print('-'*20)
        print('1. Registrar venta')
        print('2. Buscar un producto')
        print('3. Volver al menú anterior')
        print('-'*20)
        op = int(input('Ingrese una opción: ')
        while op < 1 and op > 3:
            print()
            print('ERROR! -> Se cargo un valor que no es válido!')
            op = int(input('Cargue una opción(entre 1 y 2): '))
        
        if op == 1:
            venta_terminada = False
            carga = True
            saldo = 0
            descripcion_venta = '### Productos vendidos:\n'
            while carga != False:
                 producto = int(input('Ingrese el código del producto que desea sumar a la venta: ')
                 print(f'Producto: {productos[producto][0]} - Precio: ${productos[producto][1]} - Stock: {productos[producto][2]}
                 cantidad = int(input('Ingrese la cantidad a vender: ')
                 while cantidad > productos[producto][2]:
                       print('ERROR! -> No puede ingresar una cantidad mayor al stock!')
                       cantidad = int(input(f'Ingrese la cantidad a vender (un valor menor a {productos[producto][2]} : ')
                 saldo += productos[producto][1] * cantidad #Acumulamos el costo por los productos
                 descripcion_venta = descripcion_venta + productos[producto][0] + ' - Cantidad: ' + str(cantidad) +'\n' #Armamos una descripcióin de la venta
                 productos[producto][2] = productos[producto][2] - cantidad #actualizamos el stock del producto
                 print()
                 print('¡Producto cargado a la venta!')
                 r = input('¿Desea cargar otro producto a la venta? [s/n]: ')
                 while r != 's' and r != 'n':
                    print()
                    print('ERROR! -> Se cargo un valor que no es válido!')
                    op = input('Cargue una opción(entre "s" o "n"): ')
                 if r == 'n':
                    carga = False
            #Registramos la venta                          
            nueva_venta = [descripcion_venta, saldo]
            ventas.append(nueva_venta)
         print()
         print('!Venta registrada!')
         input('Presione enter para volver a la pantalla anterior')
         menu_venta()
                 
def mostrar_total_recaudado():
    os.system('cls')
    recaudado = 0
    for i in range(len(ventas)): recaudado += ventas[i][1]
    print(f'El total recaudado por ventas hasta el momento es de: ${recaudado}')
    print()
    input('Presione enter para volver a la pantalla anterior')
    menu_venta()               

def mostrar_ventas_realizadas():
    os.system('cls')
    print('### Ventas realizadas hasta el momento')                                      
    for i in range(len(ventas)):
        print(f'')                                        
    

    

        
    
'''bloque principal'''
menu_general()
            


    

    



