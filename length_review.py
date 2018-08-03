import csv

def get_avg_len():
    length=0
    count=0
    with open('C:/Users/admin/PycharmProjects/Graduation-Project/Output.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            length+=len(row[2])
            #print(len(row[2]))
            #print(row[2])
            count+=1

    result=length/count
    print(length/count)
    return result

