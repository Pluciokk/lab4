zakupy = {"papryka":6.99, "ryż":9.99, "piwo":3}
print(zakupy)
suma = 0

for key in zakupy:
    suma += zakupy[key]
    print(key)
    print(suma)
print(suma)