from faker import Faker

fa = Faker()
print(fa.name())

listas = []
for _ in range(10):
    listas.append(fa.name())
print(listas)
