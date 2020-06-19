import os
import psutil
import matplotlib.backends.backend_tkagg
from matplotlib import pyplot as plt
import datetime
from time import time

pid_S = os.getpid()
py_S = psutil.Process()
total_time = 0


def Sieve_Of_Eratosthenes(n):
    prime = [True for i in range(n + 1)]

    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is
        # a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    c = 0

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            c += 1
    return c


def isPrime_1(end, time_dict):

    print('****************sieve of eratosthenes*********************')
    t0 = time()
    c = Sieve_Of_Eratosthenes(end)
    print(f"Total prime numbers in range(1, {end}) using Sieve Of Eratosthenes:", c)
    t1 = time() - t0
    time_dict['sieve'] = t1
    print(f"Total time taken for the Sieve of Eratosthenes is:{t1}  Seconds")
    return process_details(pid_S, py_S)


def process_details(pid, py):
    mem = py.memory_info()._asdict()
    swap_memory = psutil.swap_memory()._asdict()
    total_memory = float((swap_memory['total'] / (2 ** 30)))
    used_vms_gib = mem['vms'] / 2 ** 30
    cpu_percent = psutil.cpu_times_percent(interval=0.4, percpu=False)._asdict()

    values = [mem['rss'] / 2 ** 10, mem['vms'] / 2 ** 10, mem['num_page_faults']]
    values1 = [total_memory, used_vms_gib]
    cpu_values = [cpu_percent['user'], cpu_percent['idle'],
                  cpu_percent['system'] + cpu_percent['interrupt'] + cpu_percent['dpc']]
    file_size = [os.path.getsize((__file__)), psutil.disk_usage('C:').total]

    result = {
        f" Process ID: {pid}, RSS: {mem['rss']}, Virtual Memory: {mem['vms']}, Page Faults:{mem['num_page_faults']} "
        f"CPU %: {cpu_percent['user']} Memory usage: {round(used_vms_gib, 4)} GiB out of {round(swap_memory['total'] / (2 ** 30), 4)} GiB, file size {file_size[0]} Bytes"}
    print(f"SieveOfEratosthenes: {result}")
    return plotting(values, values1, cpu_values, file_size)


def plotting(values, values1, cpu_percent, file_size):
    profile_path = os.path.join(os.environ['USERPROFILE'], 'Pictures')
    title = 'SieveOfEratosthenes'
    date_time = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(date_time)
    title = title + str(timestamp) + '.png'
    pictures_path = os.path.join(profile_path, title)

    plot, fig = plt.subplots(2, 2, squeeze=False)
    plot.set_size_inches(20, 20)
    names1 = ('Resident Set Size', 'Virtual Memory', 'number of page faults')
    names2 = ('Total Memory available%', 'Used Memory by this algorithm %')
    names3 = ('Total CPU usage', 'Total CPU free', 'other processes')
    names4 = ('Used Hard disk', 'Total Hard disk')
    colors = ('darkorange', 'dodgerblue', 'seagreen')
    colors1 = ('orangered', 'olivedrab', 'royalblue')
    explode = [0, 0.1, 0.11]
    explode2 = [0, 0.1]

    fig[0][0].pie(values, labels=names1, explode=explode, autopct='%1.1f%%',  startangle=90, colors=colors)
    fig[0][0].set_title(f"Resident Set Size: {values[0]} KiB, 'Virtual Memory: {values[1]} KiB, number of page faults: {values[2]}")
    fig[0][1].pie(cpu_percent, labels=names3, explode=explode, autopct='%1.1f%%',  startangle=90,
                  colors=colors1)
    fig[0][1].set_title(f"CPU usage: {cpu_percent[0]}")
    fig[1][0].pie(values1, labels=names2, explode=explode2, autopct='%1.1f%%', startangle=90,
                  colors=colors)
    fig[1][0].set_title(f"Total available memory: {round(values1[0], 2)}GiB and Memory: {round(values1[1], 2)}GiB")
    fig[1][1].bar(names4, file_size)
    fig[1][1].set_title(f"Used Hard disk {file_size[0]}KB, Total Hard disk{file_size[1] / 2 ** 20}GB")
    plot.suptitle(f'{title}')

    plot.savefig(pictures_path, dpi=400)
    print("file saved at", pictures_path)
