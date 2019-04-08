print("Welcome to neh algorithm (main version)")
print("Starting algorithm... ")
import read_data, neh
import time
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Algorithm", "Cmax", "Real time"]

#MODIF?
MODIF = 3

start = 0
stop =0

tasks_val, machines_val, tasks = read_data.read_data("ta001.txt")


if MODIF == 0:
    print("Clasic neh")
    start = time.perf_counter()
    seq, cmax = neh.neh(tasks, machines_val, tasks_val)
    stop = time.perf_counter()
    print("Best sequence: ", seq)
    print("Best Cmax: ", cmax)
    policzony = round((stop-start), 3)
    print("Time: ", policzony)

if MODIF == 1:
    #mod
    print("MOD neh")
    start = time.perf_counter()
    seq, cmax = neh.neh_wm(tasks, machines_val, tasks_val)
    stop = time.perf_counter()
    print("Best sequence: ", seq)
    print("Best Cmax: ", cmax)
    policzony = round((stop-start), 3)
    print("Time: ", policzony)

if MODIF == 2:
    print("Acc neh")
    start = time.perf_counter()
    seq, cmax = neh.neh_acc(tasks, machines_val, tasks_val)
    stop = time.perf_counter()
    print("Best sequence: ", seq)
    print("Best Cmax: ", cmax)
    policzony = round((stop-start), 3)
    print("Time: ", policzony)





if MODIF == 3: #porownanie czasow

    print("Main neh:")
    start = time.perf_counter()
    seq, cmax = neh.neh(tasks, machines_val, tasks_val)
    stop = time.perf_counter()
    policzony = round((stop-start), 3)
    print("Time: ", policzony)

    table.add_row(["Classic", cmax, policzony ])

    print("Acc:")
    start = time.perf_counter()
    seq, cmax = neh.neh_acc(tasks, machines_val, tasks_val)
    stop = time.perf_counter()
    policzony = round((stop - start), 3)
    table.add_row(["Acc", cmax, policzony ])

    print(table)

if MODIF == 4: #porownanie z mod

    print("Acc neh:")
    start = time.perf_counter()
    seq, cmax = neh.neh_acc(tasks, machines_val, tasks_val)
    stop = time.perf_counter()
    policzony = round((stop-start), 3)
    print("Time: ", policzony)

    table.add_row(["Acc", cmax, policzony ])

    print("Acc witch mod:")
    start = time.perf_counter()
    seq, cmax = neh.neh_wm(tasks, machines_val, tasks_val)
    stop = time.perf_counter()
    policzony = round((stop - start), 3)
    table.add_row(["Acc WM", cmax, policzony ])

    print(table)