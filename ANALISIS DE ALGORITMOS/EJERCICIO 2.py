def suma_hasta_n(n):
    if n==1:
        return 1
    else: 
        return n+ suma_hasta_n(n-1)

#2
def potencia_recursiva(a,n):
    if n==0:
        return 1
    else:
        return a*potencia_recursiva(a,n-1)
#
def potencia_recursiva():
    a = float(input("Ingrese el número base (a): "))
    n = int(input("Ingrese la potencia (n): "))

    def calcular_potencia(a, n):
        if n == 0:
            return 1
        else:
            return a * calcular_potencia(a, n - 1)

    resultado = calcular_potencia(a, n)
    print(f"El resultado de {a} elevado a la potencia {n} es: {resultado}")

potencia_recursiva()