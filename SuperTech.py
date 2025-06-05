pesoadolar = float(input("Ingresá la cotización del dolar: "))
pesoaeuro = float(input("Ingresá la cotización del euro: "))

divizadeconversion = input("Elegí la diviza a convertir, dolar o euro: ").lower()

montodeconvesion = float(input("Ingresá el monto a convertir: "))

if divizadeconversion == "dolar":
    print(f"La conversión es de: ${pesoadolar * montodeconvesion} pesos")

elif divizadeconversion == "euro":
    print(f"La conversión es de: ${pesoaeuro * montodeconvesion} pesos")