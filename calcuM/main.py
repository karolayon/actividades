def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def isitaninteger(num):
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())

def isiteven(num):
    return isitaninteger(num) and num % 2 == 0


def main():
    print("Bienvenido a la calculadora mejorada!")

    nums = [5, 7, 9]
    print(f"Suma de {nums} = {addmultiplenumbers(nums)}")
    print(f"Multiplicación de {nums} = {multiplymultiplenumbers(nums)}")
    print(f"¿6 es par? {isiteven(6)}")
    print(f"¿7.3 es entero? {isitaninteger(7.3)}")


if __name__=="__main__":
  main()