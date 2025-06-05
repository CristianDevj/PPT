edadcliente = int(input("Ingresá la edad: "))

if edadcliente < 18 or edadcliente > 60:
    print("No podés ingresar, no cumplís los requisitos de edad.")

elif 18 <= edadcliente <= 60:
    print("Podés ingresar, crack.")