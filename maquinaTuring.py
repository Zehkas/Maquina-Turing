#Mateo González Lisboa 21271756-8
#Eduardo loyola 21294383-5
#Vicente Herrera 21533069-9

def leerDatos(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    datos = []
    transiciones = []
    cadenas = []
    linea = archivo.readline().rstrip("\n")

    while linea != "":
        datos.append(linea)
        linea = archivo.readline().rstrip("\n")

    for i in range(0, len(datos)):
        datos[i] = datos[i].split(" ")

        if len(datos[i]) == 5 and i != 1:
            transiciones.append(datos[i])

        elif len(datos[i]) == 1:
            cadenas.append(datos[i][0])

    estados = datos[0][0]
    simbolos = datos[0][1]
    alfabeto = datos[1]

    return estados, simbolos, alfabeto, cadenas, transiciones

def imprimirInfo(estados, cantidad_simbolos, alfabeto, transiciones):
    print(f"Estados: {estados}")
    print(f"Símbolos: {cantidad_simbolos}")
    print(f"Alfabeto: ['{alfabeto[0]}', '{alfabeto[1]}', '{alfabeto[2]}', '{alfabeto[3]}', '{alfabeto[4]}']")
    print(f"Tabla de transiciones:")

    estados = sorted(set([state[0] for state in transiciones ]))

    for transicion in transiciones:
        estadoActual = transicion[0]
        simboloEntrada = transicion[1]
        simboloSalida = transicion[2]
        movimiento = transicion[3]
        estadoSiguiente = transicion[4]

    print(f"{'Estado':<8}{alfabeto[0]:<15}{alfabeto[1]:<15}{alfabeto[2]:<15}{alfabeto[3]:<15}{alfabeto[4]:<15}")
    print("-" * 80)

    for estado in estados:
        fila = [f"{estado:<8}"]

        for simbolo in alfabeto:
            transicion = [f"{t[2]},{t[3]},{t[4]}" for t in transiciones if (t[0] == estado and t[1] == simbolo)]

            fila.append(f"{transicion[0]:<15}")

        print("".join(fila))
    print()

def obtenerCinta(estados, cantidad_simbolos, alfabeto, cadenas, transiciones):
    imprimirInfo(estados, cantidad_simbolos, alfabeto, transiciones)
    print(f"{cadenas[0]} Casos disponibles")

    caso = 1

    for cadena in cadenas[1::]:
        cinta = []

        for simbolo in cadena:
            cinta.append(simbolo)

        resultado = maquinaTuring(transiciones, cinta, caso)


        if resultado == True:
            print("La cadena es aceptada")
        else:
            print("La cadena no es aceptada")
        
        caso += 1

    return True

def maquinaTuring(transiciones, cinta, caso):
    estadoActual = 0
    simboloActual = ""
    cabezal = 0
    print()
    print()
    print(f"Caso {caso}")
    print(f"Cadena de entrada: {cinta}")

    

    while estadoActual != -1:

        simboloActual = cinta[cabezal]

        for funcion in transiciones:

            for i in funcion:

                if estadoActual == int(funcion[0]) and simboloActual == funcion[1]:
                    estadoActual = int(funcion[4])
                    cinta[cabezal] = funcion[2]

                    if funcion[3] == "d":
                        cabezal += 1
                        if cabezal > len(cinta) - 1:
                            cabezal = 0

                    elif funcion[3] == "i":
                        cabezal -= 1
                        if cabezal < 0:
                            cabezal = len(cinta)
                            
                    simboloActual = cinta[cabezal]
    
    print(f"Cinta resultante: {cinta}")
    print(f"Posición del cabezal: {cabezal}")
    if cinta[cabezal] == "a":
        return True
    else:
        return False

if __name__ == "__main__":
    estados, cantidad_simbolos, alfabeto, cadenas, transiciones = leerDatos("entrada.txt")
    obtenerCinta(estados, cantidad_simbolos, alfabeto, cadenas, transiciones)