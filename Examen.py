import random
import csv
import statistics
import math

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def asignar_sueldos():
    sueldos = []
    for i in range(10):
        sueldos.append(random.randint(300000, 2500000))
    return sueldos

def clasificar_sueldos(sueldos):
    sueldos_menores = []
    sueldos_intermedios = []
    sueldos_mayores = []
    for i in range(10):
        if sueldos[i] < 800000:
            sueldos_menores.append((trabajadores[i], sueldos[i]))
        elif 800000 <= sueldos[i] <= 2000000:
            sueldos_intermedios.append((trabajadores[i], sueldos[i]))
        else:
            sueldos_mayores.append((trabajadores[i], sueldos[i]))
    print("\nSueldos menores a $800.000 TOTAL: " + str(len(sueldos_menores)))
    print("\nNombre empleado Sueldo")
    for nombre, sueldo in sueldos_menores:
        print(f"{nombre}      ${sueldo}")
    print("\nSueldos entre $800.000 y $2.000.000 TOTAL: " + str(len(sueldos_intermedios)))
    print("\nNombre empleado Sueldo")
    for nombre, sueldo in sueldos_intermedios:
        print(f"{nombre}      ${sueldo}")
    print("\nSueldos superiores a $2.000.000 TOTAL: " + str(len(sueldos_mayores)))
    print("\nNombre empleado Sueldo")
    for nombre, sueldo in sueldos_mayores:
        print(f"{nombre}      ${sueldo}")
    print("\nTOTAL SUELDOS: $" + str(sum(sueldos)))
    print(" ")

def ver_estadisticas(sueldos):
    print("Sueldo más alto: $" + str(max(sueldos)))
    print("Sueldo más bajo: $" + str(min(sueldos)))

def ver_estadisticas(sueldos):
    print(" ")
    print("Sueldo más alto: $" + str(max(sueldos)))
    print("Sueldo más bajo: $" + str(min(sueldos)))
    print("Promedio de sueldos: $" + str(statistics.mean(sueldos)))
    print("Media geométrica: $" + str(math.prod(sueldos) ** (1/len(sueldos))))
    print(" ")

def reporte_sueldos(sueldos):
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        for i in range(10):
            descuento_salud = sueldos[i] * 0.07
            descuento_afp = sueldos[i] * 0.12
            sueldo_liquido = sueldos[i] - descuento_salud - descuento_afp
            writer.writerow([trabajadores[i], sueldos[i], descuento_salud, descuento_afp, sueldo_liquido])

def main():
    sueldos = []
    while True:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            sueldos = asignar_sueldos()
        elif opcion == 2:
            clasificar_sueldos(sueldos)
        elif opcion == 3:
            ver_estadisticas(sueldos)
        elif opcion == 4:
            reporte_sueldos(sueldos)
        elif opcion == 5:
            print("Finalizando programa…")
            print("Desarrollado por Benjamin Mella")
            print("RUT 21.938.278-2")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()