import numpy as np
import datetime
import csv


if __name__=="__main__":
    confirm = False
    while not confirm:
        date = datetime.datetime(datetime.datetime.now().year, int(input("month: ")), int(input("day: ")), hour=int(input("hours: ")), minute=int(input("minutes: ")))
        cont = input(f"Is this correct {date} ? y/n: ")
        if cont == "y":
            confirm = True
        elif cont == "exit":
            exit()
    with open("db.csv", "a") as fd:
        write_fd = csv.writer(fd)
        write_fd.writerow([date.date(), date.hour, date.minute])
        fd.close()