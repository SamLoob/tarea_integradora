#Samuel David Soto Jojoa
#TAREA INTEGRADORA #1:
#Código de seguridad
codigo = input("Código de estudiante: ")
if codigo.startswith("A00"):
    print("Verificación exitosa")
    
    #Opciones del sistema (menú)
    print("Bienvenido al Sistema de Detección y Reparación de Código.")
    print("Seleccione una opción para continuar:")
    print("1. Calibrar núcleo del sistema.")
    print("2. Validar coordenadas de restauración.")
    print("3. Ejecutar diagnóstico completo.")
    print("4. Análisis de estabilidad del sistema.")
    print("5. Escaneo de Anomalías.")
    print("6. Salir.")
    opcion = input("Ingrese el número de la opción deseada: ")
    
    #1.Calibrar núcleo del sistema
    if opcion == "1":
        n_e = int(input("Ingrese un número entero: ")) 
        if n_e > 0:
            print("Núcleo estable")
        elif n_e < 0:
            print("Núcleo inestable: se recomienda recalibración")
        elif n_e == 0:
            print("Sistema en punto neutro: monitoreo requerido")
            
    #2.Validar coordenadas de restauración
    if opcion == "2":
        n_x = float(input("Ingrese coordenada X: "))
        n_y = float(input("Ingrese coordenada Y: "))
        if n_x % 2 == 0 and n_y % 2 == 0:
            print("Coordenadas óptimas para restauración")
        elif n_x % 2 != 0 and n_y % 2 != 0:
            print("Coordenadas inestables: riesgo de error")
        elif n_x % 2 == 0 or n_y % 2 == 0 and n_x % 2 != 0 or n_y % 2 != 0:
            print("Coordenadas en zona gris: precaución")
            
    #3.Cálculo del Índice de Estabilidad del Algoritmo (IEA)
    if opcion == "3":
        n_1 = float(input("Ingrese número 1: "))
        n_2 = float(input("Ingrese número 2: "))
        IEA = [(n_1**2)+(n_2**2)]-[(n_1*n_2)]/(n_1+n_2+1)
        if IEA < 10:
            print("Estabilidad baja: riesgo de colapso inminente")
        elif 10 <= IEA <= 50:
            print("Estabilidad moderada: ajustes recomendados")
        elif IEA > 50:
            print("Sistema estable y funcional")
            
    #4.Análisis de estabilidad del sistema
    if opcion == "4":
        n_i = float(input("Ingrese un número: "))
        if n_i > 100:
            print("Sistema en sobrecarga: riesgo alto")
        elif 50 < n_i < 100:
            print("Sistema en estado óptimo")
        elif n_i < 50:
            print("Sistema en bajo rendimiento: optimización recomendada")
            
    #5.Escaneo de Anomalías
    if opcion == "5":
        frase = input("Ingrese una frase: ")
        falla_1 = 'Error'
        falla_2 = 'Corrupto'
        if falla_1 in frase:
            print("Error")
        elif falla_2 in frase:
            print("Error")
        else:
            print("El código está limpio")
            
    #6.Salir
    if opcion == "6":
        salir = input("Escribe 'salir' para finalizar: ")
        if salir == salir:
            print("El programa ha terminado")          
else:
    print("Error")