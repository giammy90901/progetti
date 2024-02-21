budget = float(input("Inserisci il tuo budget per le spese mensili: "))
spese_totali = 0
while True:
    costo_spesa = float(input("Inserisci il costo della spesa: "))
    if costo_spesa > budget:
        print("Il budget non è sufficiente per coprire questa spesa. La spesa non verrà aggiunta.")
        break
    budget -= costo_spesa
    spese_totali += costo_spesa
print("Il budget rimanente è:", budget)
