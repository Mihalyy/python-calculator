def sum(number_1, number_2):
    return number_1 + number_2

def substract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def squareroot(number_1,number_2):
    return number_1 ** number_2

def modulo(number_1, number_2):
    return number_1 % number_2

print("=== KALKULATOR SKIBIDI ===\n")
print("1. Penjumlahan [+]")
print("2. Pengurangan [-]")
print("3. Perkalian   [*]")
print("4. Pembagian   [/]")
print("5. Pempangkatan[**]")
print("6. Modulus     [%}")
print("Pilih operasi:")

select= int(input("Pilih operasi:"))
number_1= int(input("Masukan nomor pertama"))
number_2= int(input("Masukan nomor kedua"))

match select:
    case 1:
        print(number_1, "+", number_2, "=",
                    sum(number_1, number_2))
                    
    case 2:print(number_1, "-", number_2, "=",
                    substract(number_1, number_2))

    case 3:print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

    case 4:print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
        
    case 5: print(number_1, "**", number_2, "=",
                    squareroot(number_1,number_2))

    case 6: print(number_1, "%", number_2, "=",
                    modulo(number_1,number_2))
        
    case _:print("Invalid input")
        
        