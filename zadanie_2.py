print("Zadanie 2 Konwersja temperatury z Fahrenhaita na Celcjusza, oraz na Kelvina")
temp_fahr = 100  # przykładowa temperatura w stopniach Fahrentheida
kelvin_offset = 273.15  # stała do konwersji z Celsjusza do Kelvina
fahrenheit_to_celsius = 5 / 9  # współczynnik konwersji z fahrentheita do celsjusza
fahrenheit_constant = 32  # stała do konwersji z Fahrenhaita na Celsjusza

print("Temperatura w Fahrenheicie", temp_fahr)
temp_cel = (temp_fahr - fahrenheit_constant)  * fahrenheit_to_celsius
print("Temperatura w Celsjuszach", temp_cel)

temp_kel = temp_cel + kelvin_offset
print("Temperatura w Kelvinach")