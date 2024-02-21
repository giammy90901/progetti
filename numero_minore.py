numeri = []
while True:
    numero = float(input("Inserisci un numero (inserisci 0 per terminare): "))
    if numero == 0:
        break
    numeri.append(numero)
if len(numeri) == 0:
    print("Non hai inserito nessun numero diverso da 0.")
else:
    numero_minore = min(numero for numero in numeri if numero != 0)
    print("Il numero minore inserito è:", numero_minore)
