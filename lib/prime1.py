import os
import psutil
import math
import matplotlib.backends.backend_tkagg
from matplotlib import pyplot as plt
from time import time
import datetime

pid_N = os.getpid()
py_N = psutil.Process()


def naive(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


def isPrime_0(end, time_dict):

    print("****************Naive implementation *********************")
    c = 0  # for counting
    t0 = time()
    for n in range(1, end):
        x = naive(n)
        c += x
    print(f"Total prime numbers in range(1, {end}) using Naive Implementation:", c)
    t1 = time() - t0
    time_dict['naive'] = t1
    print(f"Total time taken to complete Naive implementation is: {t1} Seconds")

    return process_details(pid_N, py_N)


def process_details(pid, py):
    # print('in process_details N', os.getpid())
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
        f"Process ID: {pid}, RSS: {mem['rss']}, Virtual Memory: {mem['vms']}, Page Faults:{mem['num_page_faults']} "
        f"CPU %: {cpu_percent['user']} Memory usage: {round(used_vms_gib, 4)} GiB out of {round(swap_memory['total'] / (2 ** 30), 4)} GiB, file size {file_size[0]} Bytes"}

    print(f"Naive Implementation: {result}")
    # uncomment the below line to save the graph
    # return plotting(values, values1, cpu_values, file_size)


def plotting(values, values1, cpu_percent, file_size):
    profile_path = os.path.join(os.environ['USERPROFILE'], 'Pictures')

    title = 'NaiveImplementation'
    date_time = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(date_time)
    title = title + str(timestamp) + '.png'
    pictures_path = os.path.join(profile_path, title)
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
    explode2 = [0,0.1]

    fig[0][0].pie(values, labels=names1, explode=explode, autopct='%1.1f%%', startangle=90, colors=colors)
    fig[0][0].set_title(
        f"Resident Set Size: {values[0]} KiB, 'Virtual Memory: {values[1]} KiB, number of page faults: {values[2]}")
    fig[0][1].pie(cpu_percent, labels=names3,explode=explode, autopct='%1.1f%%',  startangle=90, colors=colors1)
    fig[0][1].set_title(f"CPU usage: {cpu_percent[0]}")
    fig[1][0].pie(values1, labels=names2,explode=explode2, autopct='%1.1f%%', startangle=90, colors=colors)
    fig[1][0].set_title(f"Total available memory: {round(values1[0], 2)}GiB and Memory: {round(values1[1], 2)}GiB")
    fig[1][1].bar(names4, file_size)
    fig[1][1].set_title(f"Used Hard disk {file_size[0]}KB, Total Hard disk{file_size[1]/2**20}GB")
    plot.suptitle(f'{title}')

    plot.savefig(pictures_path, dpi=400)
    print("file saved at", pictures_path)
