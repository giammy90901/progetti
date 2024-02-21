numeri_inseriti = 0
numero_precedente = int(input("Inserisci il primo numero: "))
while True:
    numero_successivo = int(input("Inserisci il numero successivo: "))
    if numero_successivo % numero_precedente == 0:
        numeri_inseriti += 1
        numero_precedente = numero_successivo
    else:
        break

print("La quantità di numeri inseriti è:", numeri_inseriti)