budget = float(input("Inserisci il tuo budget per le spese mensili: "))
spese_totali = 0
while True:
    costo_spesa = float(input("Inserisci il costo della spesa: "))
    if costo_spesa > budget:
        scelta = input("La spesa supera il budget. Vuoi annullare questa spesa (s/n)? ")
        if scelta.lower() == 's':
            print("Spesa annullata.")
            continue
        else:
            print("Programma interrotto.")
            break
    budget -= costo_spesa
    spese_totali += costo_spesa
print("Il budget rimanente è:", budget)
