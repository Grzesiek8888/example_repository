from datetime import datetime
try:
    user_input = float(input("Wprowadz liczbe"))
    print(user_input/10)
except ValueError as e:
    print(datetime.now(),"ERROR:",e)
else:
    print("Uff udalo sie wprowadzic dobra wartosc")
finally:
    print("Koniec programu")

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(datetime.now(),"ERROR:",e)

# print("Test")
# raise Exception("Przepraszamy jest blad!")
lista = [1,2,3,4,5]
try:
    print(lista[124141241414221])
except IndexError as e:
    print("Wybrales wartosc z poza dlugosci listy", e)