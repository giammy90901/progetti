somma = 0
conteggio = 0
while True:
    numero = int(input("Inserisci un numero intero (inserisci un numero negativo per terminare): "))
    if numero < 0:
        break
    somma += numero
    conteggio += 1
if conteggio > 0:
    media = somma / conteggio
    print("La media dei numeri inseriti è:", media)
else:
    print("Non hai inserito alcun numero.")
