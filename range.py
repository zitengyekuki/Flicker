#coding: utf-8
#!/usr/bin/python

import csv


def rangeCSV():
    with open("result.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        lower_than_25 = []
        between_26_to_39 = []
        more_than_40 = []
        for line in reader:
            if line[5] != 'focal_length':
                focal_length = float(line[5].split()[0])
                if focal_length < 25:
                    lower_than_25.append(line)
                elif 25 < focal_length < 39:
                    between_26_to_39.append(line)
                else:
                    more_than_40.append(line)

    with open("lower_than_25.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['url', 'views', 'fave', 'comment', 'aperture', 'focal_length', 'exposure_time', 'iso'])
        for line in lower_than_25:
            writer.writerow(line)
    with open("between_26_to_39.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['url', 'views', 'fave', 'comment', 'aperture', 'focal_length', 'exposure_time', 'iso'])
        for line in between_26_to_39:
            writer.writerow(line)
    with open("more_than_40.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['url', 'views', 'fave', 'comment', 'aperture', 'focal_length', 'exposure_time', 'iso'])
        for line in more_than_40:
            writer.writerow(line)


if __name__ == "__main__":
    rangeCSV()
