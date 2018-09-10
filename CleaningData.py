import csv
import time
import nltk
import re
from collections import Counter

count=0;
all_reviews=0
start_time = time.time()

with open('C:/test/parsingCSV/allreviews.CSV') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    text_file = open("Output1.csv", "w")
    for row in readCSV:
        if(len(row)==10):
                for i in row:
                    count += 1
                    all_reviews+=1

                    if(count==6):
                        text_file.write(i.replace("Update - ",""))
                        print(i.replace("Update - ",""))
                    if (count == 3):
                        text_file.write(i.replace(",", ""))
                        print(i.replace(",", ""))
                    if(count!=3 and count!=6):
                        text_file.write(i.replace('-',"").replace("_",""))
                        print(i.replace('-',"").replace("_",""))
                    if(count<10):
                        text_file.write(',')
                        print(',')
                text_file.write('\n')
                print('\n')
                count=0;

text_file.close()
print(all_reviews)
print("--- %s seconds ---" % (time.time() - start_time))

