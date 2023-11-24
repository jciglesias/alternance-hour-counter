import numpy as np
import datetime
import csv
import os

npyfd = "badge_time.npy"


if __name__=="__main__":
    try:
        arr = np.load(npyfd,allow_pickle=True)
        now = datetime.datetime.now()
        time = datetime.datetime(now.year, now.month, now.day, hour=(now.hour - arr[0].hour), minute=(now.minute - arr[0].minute)) if now.minute >= arr[0].minute else datetime.datetime(now.year, now.month, now.day, hour=(now.hour - arr[0].hour - 1), minute=(now.minute + 60 - arr[0].minute))
        os.remove(npyfd)
        print(time)
    except Exception as e:
        confirm = False
        while not confirm:
            date = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, hour=int(input("hour: ")), minute=int(input("minute: ")))
            cont = input(f"Is this correct {date} ? y/n: ")
            if cont == "y":
                confirm = True
            elif cont == "exit":
                exit()
        arr = np.array([date])
        np.save(npyfd,arr)
        exit()
    with open("db.csv", "a") as fd:
        write_fd = csv.writer(fd)
        write_fd.writerow([time.date(), time.hour, time.minute])
        fd.close()