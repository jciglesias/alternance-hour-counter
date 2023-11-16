import csv
import datetime

if __name__=="__main__":
    dates, hours, minutes = [],[], []
    theta = [0,0]
    with open('db.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            dates.append(datetime.datetime.strptime(row["date"],'%Y-%m-%d'))
            hours.append(int(row["h"]))
            minutes.append(int(row["m"]))
    weeks = [(datetime.datetime(2023,10,16), datetime.datetime(2023,10,20),[]), (datetime.datetime(2023,11,13), datetime.datetime(2023,11,17),[]), (datetime.datetime(2023,11,20), datetime.datetime(2023,11,24),[])]
    for i in range(len(dates)):
        for x in weeks:
            if x[0] <= dates[i] and dates[i] <= x[1]:
                x[2].append((dates[i], hours[i], minutes[i]))
    for w in range(len(weeks)):
        h,m = 0,0
        for d in weeks[w][2]:
            h += d[1]
            m += d[2]
        h = int(h + m / 60)
        m %= 60
        output = f"week {weeks[w][0].strftime('%d/%m')}: {h} hours {m} minutes"
        if h < 35:
            output += f" <--> {int(((35 - h)*60+m)/60)}h {(35*60 - h*60+m)%60}m left"
        print(output)