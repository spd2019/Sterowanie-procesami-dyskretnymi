#Algroytm Pzepływowy i Johnsona
print("Starting program...")

data_tab=[]

# Wczytywanie danych
file = open("dane.txt", "r")
data = file.read()
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


file.close()



#input('Press ENTER to continue...')

