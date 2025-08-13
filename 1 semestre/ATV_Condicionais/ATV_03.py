temp_agua = float(input("Qual a temperatura da agua: "))
estado_agua = ""

if temp_agua < 0:
    estado_agua = "solido"
else:
    if temp_agua >= 0 and temp_agua <= 100:
        estado_agua = "liquido"
    else:
        estado_agua = "gasoso"

print(f"O estado da agua é {estado_agua}")