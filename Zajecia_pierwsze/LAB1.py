from Zajecia_pierwsze import read_data, bruteforce, johnson

##############################################
TWO_OR_THREE = 3         #Two or three machines algorithm??
##############################################
print("Starting program...")


##MAIN##
if(TWO_OR_THREE == 2):
    tasks_val, machines_val, tasks = read_data.read_data("Zajecia_pierwsze\data_2m.txt")
if(TWO_OR_THREE == 3):
    tasks_val, machines_val, tasks = read_data.read_data("Zajecia_pierwsze\data_3m.txt")
    print("The package ta000 has been loaded")

bruteforce.bruteforce(tasks, machines_val, tasks_val)
johnson.johnson_algorithm(machines_val, tasks)





