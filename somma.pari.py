numero = int(input("Inserisci un numero intero: "))
somma_pari = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        somma_pari += i
print("La somma dei numeri pari compresi tra 1 e", numero, "è:", somma_pari)
