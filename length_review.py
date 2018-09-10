import csv
def get_max_len():
    length=0
    max=0
    min=1000
    with open('C:/Users/admin/PycharmProjects/Graduation-Project/Output.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            length=len(row[2])
            if length>max:
                max=length

    return max

#print(get_max_len())
