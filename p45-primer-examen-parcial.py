'''Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: 
Tipo de usuario, paquete y cantidad.
• Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
• Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900
Se debe calcular un subtotal de la venta sumando el precio del tipo de usuario más el precio de tipo de paquete,
y multiplicando por la cantidad solicitada.
Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de acuerdo a lo siguiente
• Es Alumno 20%
• Es Trabajador y un 10%
• Es Docente y un 5%
Al final mostrar un resumen con los datos calculados de la venta.
Al terminar de procesar las ventas mostrar el total de ventas del día:'''

import os; os.system("Cls")

total_ventas = 0  
print("Universidad Patito SA de CV\nSistema de Inscripción Congreso de Sistemas")

while True:
    
    while True:
        usuario = int(input("\n[1] Alumno $100\n[2] Trabajador $200\n[3] Docente $500\n¿Qué tipo de usuario eres?: "))
        if usuario == 1 or usuario == 2 or usuario == 3: break  
        else:
            print("\nOpción no válida, por favor selecciona [1], [2] o [3].")
    
    while True:
        paquete = int(input("\n[1] Solo conferencia $600\n[2] Con evento social $800\n[3] Con kit de acceso $900\n¿Qué paquete deseas? "))
        if paquete == 1 or paquete == 2 or paquete == 3: break  
        else:
            print("\nOpción no válida, por favor selecciona [1], [2] o [3].")
    
    while True:
        cantidad = int(input("\nCantidad: "))
        if cantidad > 0:  break  
        else:
            print("\nLa cantidad debe ser mayor a 0.")

    alumno = 100
    trabajador = 200
    docente = 500

    if usuario == 1:  
        if paquete == 1:
            tipaque = "Solo conferencias"
            total = (alumno + 600) * cantidad
        elif paquete == 2:
            tipaque = "Con eventos sociales"
            total = (alumno + 800) * cantidad
        elif paquete == 3:
            tipaque = "Con kit de acceso"
            total = (alumno + 900) * cantidad

        if total >= 5000:
            descuento = total * 0.2  
            total_con_descuento = total - descuento
            print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: {tipaque}")
            print(f"Subtotal: ${total:.2f}, Con un descuento de: ${descuento:.2f} (20%)")
        else:
            total_con_descuento = total
            print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Alumno, Tipo de paquete: {tipaque}")
            print("No se aplica descuento")
        print(f"Total a pagar: ${total_con_descuento:.2f}")
        total_ventas += total_con_descuento
        if input("\n¿Deseas continuar (S/N)?: ").upper().startswith("N"): break

    if usuario == 2:  
        if paquete == 1:
            tipaque = "Solo conferencias"
            total = (trabajador + 600) * cantidad
        elif paquete == 2:
            tipaque = "Con eventos sociales"
            total = (trabajador + 800) * cantidad
        elif paquete == 3:
            tipaque = "Con kit de acceso"
            total = (trabajador + 900) * cantidad

        if total >= 5000:
            descuento = total * 0.1  
            total_con_descuento = total - descuento
            print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: {tipaque}")
            print(f"Subtotal: ${total:.2f}, Con un descuento de: ${descuento:.2f} (10%)")
        else:
            total_con_descuento = total
            print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Trabajador, Tipo de paquete: {tipaque}")
            print("No se aplica descuento")
        print(f"Total a pagar: ${total_con_descuento:.2f}")
        total_ventas += total_con_descuento
        if input("\n¿Deseas continuar (S/N)?: ").upper().startswith("N"): break

    if usuario == 3:  
        if paquete == 1:
            tipaque = "Solo conferencias"
            total = (docente + 600) * cantidad
        elif paquete == 2:
            tipaque = "Con eventos sociales"
            total = (docente + 800) * cantidad
        elif paquete == 3:
            tipaque = "Con kit de acceso"
            total = (docente + 900) * cantidad

        if total >= 5000:
            descuento = total * 0.05  
            total_con_descuento = total - descuento
            print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: {tipaque}")
            print(f"Subtotal: ${total:.2f}, Con un descuento de: ${descuento:.2f} (5%)")
        else:
            total_con_descuento = total
            print(f"Tu pedido fue: {cantidad}, Tipo de usuario: Docente, Tipo de paquete: {tipaque}")
            print("No se aplica descuento")
        print(f"Total a pagar: ${total_con_descuento:.2f}")
        total_ventas += total_con_descuento
        if input("\n¿Deseas continuar (S/N)?: ").upper().startswith("N"): break

print(f"\nLa venta total del día es: ${total_ventas:.2f}")
print("\nFin del programa.")

