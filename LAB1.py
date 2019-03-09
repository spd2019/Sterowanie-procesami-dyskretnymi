import numpy as np

print("Starting program...")

data_tab=[]

# Wczytywanie danych
file = open("dane_2m.txt", "r")
data = file.read()
file.close()

print("Reading data:")
print(data)

for number in data.split():         #Wczytywanie danych do tablicy
    data_tab.append(int(number))

print("Data transfered to table: ")
print(data_tab)

task_val = data_tab[0]
machines_val = data_tab[1]

print("Number of tasks: ", task_val)
print("Numer of machines: ", machines_val)

data_tab.pop(0)
data_tab.pop(0)

print("Just tasks")
print(data_tab)








#input('Press ENTER to continue...')


##ALGORYTM JOHNSONA


