import csv

def get_avg_rate(id):
    length=0
    ext_flag=0
    lower=1
    upper=5
    count=0
    rating=0
    with open('C:/Users/admin/PycharmProjects/Graduation-Project/Output.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if(id==row[1]):
               # print(id)
                #print(row[3])
                rating+=int(row[3])
                #print(row[3])
                count+=1

    result=rating/count
    if (result > upper or result < lower):
        ext_flag = 1
    else:
        ext_flag = 0
    #print(ext_flag)
    #print(rating)
    #print(count)
    #print(result)


    return result
    #return ext_flag


