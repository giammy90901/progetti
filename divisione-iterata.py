def divisioni_fino_a_N(N):
    if N <= 0:
        print("Inserisci un numero intero positivo diverso da zero.")
        return

    for i in range(2, N + 1):
        risultato = N / i
        print(f"{N} diviso {i} è uguale a {risultato}")

N = int(input("Inserisci un numero intero N: "))
divisioni_fino_a_N(N)
