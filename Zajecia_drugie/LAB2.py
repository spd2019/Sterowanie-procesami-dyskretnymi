print("Welcome to neh algorithm (main version)")
print("Starting algorithm... ")
import read_data, neh
import time

#MODIF?
MODIF = 1

start = 0
stop =0

tasks_val, machines_val, tasks = read_data.read_data("ta001.txt")


if MODIF == 1:
    #mod
    print("nowy neh")
    start = time.clock()
    seq, cmax = neh.neh_wm(tasks, machines_val, tasks_val)
    stop = time.clock()

if MODIF == 0:
#Clasic neh
    start = time.clock()
    seq, cmax = neh.neh(tasks, machines_val, tasks_val)
    stop = time.clock()



print("Best sequence: ", seq)
print("Best Cmax: ", cmax)
policzony = (stop-start)
print("Time: ", policzony)

#Accelerated neh