# Paso 1: Solicitar al usuario que ingrese las medidas de la pieza del mueble en cms
medida_en_cms = float(input("Por favor ingrese las medidas del mueble (en cms) "))

# Paso 2: Convertir las medidas de cms a pulgadas
medida_en_pulgadas = medida_en_cms / 2.54

# Paso 3: Mostrar al usuario las medidas convertidas a pulgadas
print("Las medidas de la pieza ingresada son:  ", medida_en_pulgadas)