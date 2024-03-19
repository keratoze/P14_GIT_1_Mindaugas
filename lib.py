# def hello_name(count, name):
#     for _ in range(count):
#         print(f"Hello, {name}!")
#
# hello_name(3, "John")

#2
# def lyginis_nelyginis_print(number):
#     if number % 2 == 0:
#         print(f"Skaičius {number} yra lyginis.")
#     else:
#         print(f"Skaičius {number} yra nelyginis.")
#
# skaičius = int(input("Įveskite skaičių: "))
# lyginis_nelyginis_print(skaičius)
#

#3
# def lyginis_nelyginis_return(number):
#     if number % 2 == 0:
#         return "skaičius lyginis"
#     else:
#         return "skaičius nelyginis"
#
# skaičius = int(input("Įveskite skaičių: "))
# rezultatas = lyginis_nelyginis_return(skaičius)
# print(rezultatas)

#4
def ar_lyginis(number):
    return number % 2 == 0

skaičius = int(input("Įveskite skaičių: "))
rezultatas = ar_lyginis(skaičius)
print(rezultatas)
