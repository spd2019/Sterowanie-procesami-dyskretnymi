print("Welcome to LAB2")
from Zajecia_drugie import read_data, neh

tasks_val, machines_val, tasks = read_data.read_data("Zajecia_drugie/ta001.txt")

seq, cmax = neh.neh(tasks, machines_val, tasks_val)
print("Najlepsza sekwencja: ", seq)
print("Najlepszy Cmax: ", cmax)
