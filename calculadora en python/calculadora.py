# despues de sumar, el usuario puede elegir hacer mas cosas

def operaciones_basicas():
    print("\nque operacion quieres hacer?")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. modulo (lo que sobra de dividir)")
    print("6. sumar 3 numeros")
    print("7. poner una operacion larga (como 2 + 5 - 3)")

    opcion = input("elige un numero del 1 al 7: ")

    if opcion == "1":
        a = int(input("primer numero: "))
        b = int(input("segundo numero: "))
        print("resultado:", a + b)

    elif opcion == "2":
        a = int(input("primer numero: "))
        b = int(input("segundo numero: "))
        print("resultado:", a - b)

    elif opcion == "3":
        a = int(input("primer numero: "))
        b = int(input("segundo numero: "))
        print("resultado:", a * b)

    elif opcion == "4":
        a = int(input("primer numero: "))
        b = int(input("segundo numero: "))
        if b != 0:
            print("resultado:", a // b)  
        else:
            print("no se puede dividir por 0")

    elif opcion == "5":
        a = int(input("primer numero: "))
        b = int(input("segundo numero: "))
        if b != 0:
            print("resultado:", a % b)
        else:
            print("error, no se puede hacer eso")

    elif opcion == "6":
        a = int(input("primer numero: "))
        b = int(input("segundo numero: "))
        c = int(input("tercer numero: "))
        print("resultado:", a + b + c)

    elif opcion == "7":
        expresion = input("escribe una operacion (ejemplo: 2 + 4 - 1): ")
        try:
            resultado = eval(expresion)
            print("resultado:", resultado)
        except:
            print("esa operacion no sirve, intenta otra vez")
    else:
        print("opcion no es valida")

operaciones_basicas()
