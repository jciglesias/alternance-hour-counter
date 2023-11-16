import numpy as np
import datetime
import csv


if __name__=="__main__":
    date = datetime.datetime(datetime.datetime.now().year, int(input("month: ")), int(input("day: ")), hour=int(input("hours: ")), minute=int(input("minutes: ")))
    # print(date.date())
    with open("db.csv", "a") as fd:
        write_fd = csv.writer(fd)
        write_fd.writerow([date.date(), date.hour, date.minute])
        fd.close()