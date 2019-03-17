print("Welcome to neh algorithm (main version)")
print("Starting algorithm... ")
from Zajecia_drugie import read_data, neh

tasks_val, machines_val, tasks = read_data.read_data("ta001.txt")

seq, cmax = neh.neh(tasks, machines_val, tasks_val)
print("Best sequence: ", seq)
print("Best Cmax: ", cmax)
