# Program Maksimum 2 Bilangan
# Input A dan B. Tuliskan mana yang paling besar.
# Jika A > B, maka bilangan terbesar adalah A
# Jika A < B, maka bilangan terbesar adalah B
# Jika A = B, maka bilangan terbesar adalah A atau B

# KAMUS
# A : float
# B : float

# ALGORRITMA
A = float(input("Masukkan nilai A = "))
B = float(input("Masukkan nilai B = "))

if (A > B):
    print("Bilangan terbesar adalah A")
elif (A < B):
    print("Bilangan terbesar adalah B")
else:  # A = B
    print("Bilangan terbesar adalah A atau B")

# Program ini ada 3 kasus