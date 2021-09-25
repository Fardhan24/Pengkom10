# Program TotalHambatanSeri
# Hambatan total harus bernilai positif.
# Jika hambatan bernilai negatif, tuliskan pesan kesalahan

# KAMUS
# R1 : float
# R2 : float
# R3 : float
# RT : R1 + R2 + R3
# R1 >= 0
# R2 >= 0
# R3 >= 0

# ALGORITMA
R1 = float(input("Masukkan nilai hambatan R1 tanpa satuan (ohm) = "))
R2 = float(input("Masukkan nilai hambatan R2 tanpa satuan (ohm) = "))
R3 = float(input("Masukkan nilai hambatan R3 tanpa satuan (ohm) = "))

print("")
print("Nilai hambatan R1 adalah", R1, "ohm")
print("Nilai hambatan R1 adalah", R2, "ohm")
print("Nilai hambatan R1 adalah", R3, "ohm")
print("")

if R1 >= 0 and R2 >= 0 and R3 >= 0:
    RT = R1 + R2 + R3
    print("Jadi, nilai hambatan total adalah", RT, "ohm")
else:  # R1 and R2 and R3 < 0
    print("Hambatan total tidak bisa dihitung")
