# Inicjalizuj sumę = 0, num1 = 10, num2 = 20 (PROCES)
# Wprowadź liczby (I / O)
# Dodaj je i zapisz wynik w sumie (PROCES)
# Wydrukuj sumę (I / O)

suma = 0
number1 = 10
number2 = 20
suma = number1 + number2
print("Suma", suma, "liczba pierwsza", number1, "liczba druga", number2)
print("Suma:", suma, "\nLiczba pierwsza:", number1, "\nLiczba druga:", number2)

# Zadanie 2 Konwersja temperatury z Fahrenhaita na Celcjusza, oraz na Kelvina
# Zainicjalizuj temp w Farh
# Zainicjalizuj temp w Celcjuszach jako nowa zmienna np: temp_cel i przypisz do niej wynik konwersji 
# Zainicalizuj temp w Kelwinach jako nowa zmienna np: temp_kel i przypisz do niej wynik konwersji

print("Zadanie 2 Konwersja temperatury z Fahrenhaita na Celcjusza, oraz na Kelvina")
temp_fahr = 100  # przykładowa temperatura w stopniach Fahrentheida
kelvin_offset = 273.15  # stała do konwersji z Celsjusza do Kelvina
fahrenheit_to_celsius = 5 / 9  # współczynnik konwersji z fahrentheita do celsjusza
fahrenheit_constant = 32  # stała do konwersji z Fahrenhaita na Celsjusza

Print("Temperatura w Fahrenheicie", temp_fahr)
temp_cel = (temp_fahr - fahrenheit_constant)  * fahrenheit_to_celsius
print("Temperatura w Celsjuszach", temp_cel)

temp_kel = temp_cel + kelvin_offset
print("Temperatura w Kelvinach")

