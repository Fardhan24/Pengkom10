# Program WujudAir
# Menentukan suhu air dan menuliskan wujudnya.
# Jika suhu air <= 0 derajat, wujud air beku
# Jika suhu air > 0 dan < 100 derajat, wujud air cair
# Jika suhu air >= 100, wujud air uap

# KAMUS
# T : suhu air
# T : float

# ALGORITMA
T = float(input("Masukkan suhu air tanpa satuan (derajat) = "))

if (T <= 0):
    print("Wujud air adalah beku")
elif (0 < T < 100):
    print("Wujud air adalah cair")
else: # T >= 100
    print("Wujud air adalah uap")