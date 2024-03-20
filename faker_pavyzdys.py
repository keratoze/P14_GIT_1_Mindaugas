from faker import Faker
import requests

fa = Faker()
print(fa.name())

listas = []
for _ in range(10):
    listas.append(fa.name())
print(listas)
