###1
a = "Nastya"
b = "Garina"
c = 2004
print(a, "_", b, "_", c, sep = "")

a, b = b, a
c += 60
print(a, "_", b, "_", c, sep = "")
print("")

###2
a = str(input("Введите имя: "))
b = str(input("Введите фамилию: "))
c = int(input("Введите год: "))
print(a, "_", b, "_", c, sep = "")

a, b = b, a
c += 60
print(a, "_", b, "_", c, sep = "")
print("")