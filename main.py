#!/usr/bin/env python3




def main():
    print("Hello, World!")
    nome1 = input("Come ti chiami? \n")
    print("Ciao, contadino/a " + nome1 + " benvenuto nella tua nuova fattoria")

    if nome1 == "Luca":
        print("ti conosco")
    else:
        print("non ti conosco")


# Esecute.
if __name__ == '__main__':
    main()


def addizione(x, y):
    return x + y

def sottrazione(x, y):
    return x - y

def moltiplicazione(x, y):
    return x * y

def divisione(x, y):
    if y != 0:
        return x / y
    else:
        return "Errore: divisione per zero"

print("Seleziona l'operazione:")
print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")

scelta = input("Inserisci la tua scelta (1/2/3/4): ")

num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

if scelta == '1':
    print(num1, "+", num2, "=", addizione(num1, num2))
elif scelta == '2':
    print(num1, "-", num2, "=", sottrazione(num1, num2))
elif scelta == '3':
    print(num1, "*", num2, "=", moltiplicazione(num1, num2))
elif scelta == '4':
    print(num1, "/", num2, "=", divisione(num1, num2))
else:
    print("Scelta non valida")