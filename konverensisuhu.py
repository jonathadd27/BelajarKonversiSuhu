# Latihan konversi satuan temperature

# Mengubah celcius ke bentuk lain

print("PROGRAM KONVERSI TEMPERATURE")

celcius = float(input("Masukan suhu dalam celcius : "))
print("Suhu dalam celcius adalah", celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah", reamur, "Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

#Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")
