import csv
import re


def helpfullness2(helpfull,allReview):
    helpfull=int(helpfull)
    allReview= int(allReview)
    if helpfull==0:
        return 0
    else:
        return helpfull/allReview



##############################################################################



#AccountFreshness("5mFtCLdzwGCnalxod1Ox9g")

###############################################################################
def Helpfulness(reviewerId):
    Helpfull = 0
    Useful_Threshold = 4 #determined manualy
    Useful_count = 0
    summation=0
    Helpfull_Count = 0
    Not_Helpfull_Count = 0
    with open('C:/Users/admin/PycharmProjects/Graduation-Project/Output.csv') as csvfile:
        CSVReader = csv.reader(csvfile, delimiter=',')
        for row in CSVReader:
            if(reviewerId == row[1]):
               Useful_count = int(row[4])
               summation+=Useful_count


    #print("Helpfull Count: ",Helpfull_Count)
    #print("Not Helpfull Count: ",Not_Helpfull_Count)
    #Helpfull = Helpfull_Count/(Helpfull_Count+Not_Helpfull_Count)
    #print("Helpfull : ",Helpfull)
    return summation

# Rating of the review
# this feature depends on the rating of the review itself to check its reality

def extreme_rating(rating):
    if(rating <=1 or rating >= 5):
        return 1
    else:
        return 0;

#this feature checks for a url other than yelp.com

def is_url(message):
    flag=0
    urls1=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    urls2 = re.findall('www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)

    for i in urls2:
        urls1.append(i)

    #print(urls1)
    for i in urls1:
        print("Urls: ", i)
        if (('https://yelp.com' not in i) and ('https://www.yelp.com' not in i) and ('yelp.ca') not in i):
            flag=1
    return flag

#print(is_url("https://yelp.com www.yelp.com www.mohanad.com"))