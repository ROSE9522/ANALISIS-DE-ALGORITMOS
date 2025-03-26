def mover_disco(origen, destino):
    disco = origen.pop()
    destino.append(disco)
    print(f"Mover disco {disco} de {origen} a {destino}")

def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        mover_disco(origen, destino)
    else:
        torres_hanoi(n-1, origen, auxiliar, destino)
        mover_disco(origen, destino)
        torres_hanoi(n-1, auxiliar, destino, origen)

# Ejemplo de uso
ndiscos = 2
t1 = list(range(ndiscos, 0, -1))
t2 = []
t3 = []

torres_hanoi(ndiscos, t1, t2, t3)
