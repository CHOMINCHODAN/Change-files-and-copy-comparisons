import csv
import pandas as pd

with open('/media/rastech/T71/event_data_20221102/rosbag2_2022_11_02-10_31_48_D/metadata.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(' '.join(row))




