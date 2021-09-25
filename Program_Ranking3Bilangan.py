# Program Ranking3Bilangan
# Mengurutkan 3 bilangan A, B, dan C dari yang terbesar sampai yang terkecil
# Dengan A /= B /= C

# KAMUS
# A = int
# B = int
# C = int
# A /= B /= C

# ALGORITMA
print("Masukkan 3 bilangan berbeda untuk A, B, dan C")
A = int(input("Masukkan bilangan A = "))
B = int(input("Masukkan bilangan B = "))
C = int(input("Masukkan bilangan C = "))

print("")
print("Bilangan A adalah", A)
print("Bilangan B adalah", B)
print("Bilangan C adalah", C)
print("")

if A > B > C:
    print("Maka urutan bilangan tersebut adalah", A, B, C)
elif A > C > B:
    print("Maka, urutan bilangan tersebut adalah", A, C, B)
elif B > C > A:
    print("Maka, urutan bilangan tersebut adalah", B, C, A)
elif B > A > C:
    print("Maka, urutan bilangan tersebut adalah", B, A, C)
elif C > A > B:
    print("Maka, urutan bilangan tersebut adalah", C, A, B)
else: # C > B > A
    print("Maka, urutan bilangan tersebut adalah", C, B, A)