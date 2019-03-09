import numpy as np
import johnson
import read_data

##############################################
TWO_OR_THREE = 3         #Two or three machines algorithm??
##############################################
print("Starting program...")


##MAIN##
if(TWO_OR_THREE == 2):
    tasks_val, machines_val, tasks = read_data.read_data("data_2m.txt")
if(TWO_OR_THREE == 3):
    tasks_val, machines_val, tasks = read_data.read_data("data_3m.txt")


johnson.johnson_algorithm(machines_val, tasks)





