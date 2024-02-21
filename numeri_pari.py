def main():
    numeri_inseriti = []
    continua_inserimento = True

    while continua_inserimento:
        numero_str = input("Inserisci un numero (o -1 per terminare): ")
        if numero_str == "-1":
            continua_inserimento = False
        else:
            if numero_str.isdigit():
                numero = int(numero_str)
                if numero % 2 == 0:
                    numeri_inseriti.append(numero)
                else:
                    print("Il numero inserito non è pari.")
            else:
                print("Inserisci un numero valido.")

    print(f"Hai inserito {len(numeri_inseriti)} numeri pari.")

if __name__ == "__main__":
    main()
