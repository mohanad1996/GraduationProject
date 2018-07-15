import csv
import time

count=0;
start_time = time.time()

with open('C:/New-folder/allreviews.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    text_file = open("Output.csv", "w")

    for row in readCSV:
            if(len(row)==10):
                for i in row:
                    count += 1;
                    if(count!=3):
                        text_file.write(i)
                        print(i)
                    if(count==3):
                        text_file.write(i.replace(",", ""))
                        print(i.replace(",", ""))
                    if(count<10):
                        text_file.write(',')
                        print(',')
                text_file.write('\n')
                print('\n')
                count=0;

text_file.close()
print(count)
print("--- %s seconds ---" % (time.time() - start_time))

