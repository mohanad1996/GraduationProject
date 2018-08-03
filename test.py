import csv
from find_avg_rating import get_avg_rate
from word_deviation import get_word_len
length=0
ext_flag=0
lower=1
upper=5
count=0
rating=0
with open('C:/Users/admin/PycharmProjects/Graduation-Project/Output.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(get_word_len(row[2]))
        count+=1
print("final count",count)

