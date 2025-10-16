# =========================================
# Ticket de compra (versión con errores)
# =========================================

# (f) “Constantes” (usaremos mayúsculas por convención)
IVA_PORCENTAJE = 21.0        # Porcentaje de IVA
DESCUENTO_BIENVENIDA = 0.10  # Descuento

print("==== TICKET DE COMPRA ====")

#Solicita el nombre del artículo y precio
nombre_articulo = input("Nombre del artículo: ")
precio_unitario = float(input("Precio unitario (€): "))  
precio_unitaro = 0.0 

#Pedimos la cantidad comprada
cantidad = int(input("Cantidad comprada: "))         

#Calculamos el subtotal
subtotal = precio_unitario * cantidad 

#Calcula el descuento
descuento = subtotal * DESCUENTO_BIENVENIDA 

#Calcula el precio con IVA (21%)
precio_con_iva = subtotal + subtotal * IVA_PORCENTAJE 

#Imprime datos
print("Artículo: " + nombre_articulo)
print(f"Unidades: " + str(cantidad))
print(f"Subtotal: " + str(subtotal) + " €")
print(f"Descuento bienvenida (10%): {descuento} €")  
print(f"IVA aplicado (" + str(IVA_PORCENTAJE) + "%): ")

#Calcula el total
total = precio_con_iva - descuento

#Imprime precio a pagar
print(f"TOTAL A PAGAR: {total} €")
