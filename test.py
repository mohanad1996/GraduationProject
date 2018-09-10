def write_to_file(word_len,length_dev,pos_adj,pos_verb,url,frist,is_extreme,filtered):
    csv_out.write(str(word_len))
    csv_out.write(",")
    csv_out.write(str(length_dev))
    csv_out.write(",")
    csv_out.write(str(pos_adj))
    csv_out.write(",")
    csv_out.write(str(pos_verb))
    csv_out.write(",")
    csv_out.write(str(url))
    csv_out.write(",")
    csv_out.write(str(frist))
    csv_out.write(",")
    csv_out.write(str(is_extreme))
    csv_out.write(",")
    csv_out.write(str(filtered))
    csv_out.write("\n")
    return



import csv
import time
from Find_Cosine_Sim import find_cos
from features_calculation import Helpfulness, extreme_rating
from length_deviation import get_deviation
from find_avg_rating import get_avg_rate
from features_calculation import is_url
from word_deviation import get_word_len
from POS_taggers import get_pos
start_time = time.time()
length=0
ext_flag=0
lower=1
upper=5
count=0
rating=0
max=0
current=0
csv_out=open("out_data.csv","w") #output csv file




write_to_file("word_len","length_dev","pos_adj","pos_verb","url","frist","is_extreme","filtered")
with open('C:/Users/admin/PycharmProjects/Graduation-Project/Output.csv') as csvfile1:
    next(csvfile1)
    readCSV1 = csv.reader(csvfile1, delimiter=',')
    for row1 in readCSV1:
        count+=1
        if count==1000:
            print("--- %s seconds ---" % (time.time() - start_time))

        print("sample number: ",count)
        #with open('C:/Users/admin/PycharmProjects/Graduation-Project/Out.csv') as csvfile2:
        #    readCSV2 = csv.reader(csvfile2, delimiter=',')
        #    max=0
        #    for row2 in readCSV2:
         #       if(row1[0]!=row2[0]):
         #           current=find_cos(row1[2],row2[2])
         #       if current>max:
         #           max=current
        #print("cosine sim: ",max)
        pos=get_pos(row1[2])
        write_to_file(get_word_len(row1[2]), get_deviation(row1[2]), pos[0], pos[1],is_url(row1[2]), float(row1[7])/float(row1[8]),  extreme_rating(int(row1[3])),row1[9])
        #print("avg word length: ",get_word_len(row1[2]))
        #print("length deviation : ", get_deviation(row1[2]))
        #print("POS of adjective: ",pos[0])
        #print("POS of verbs: ",pos[1])
        #print("url mention: ",is_url(row1[2]))
        #print("first count: ",float(row1[7])/float(row1[8]))
        #print("is extreme:", extreme_rating(int(row1[3])))
        #print("helpfullness: ",Helpfulness(row1[1]))
        #print("----------------")
        #print("--- %s seconds ---" % (time.time() - start_time))

        #with open('C:/Users/admin/PycharmProjects/Graduation-Project/Output.csv') as csvfile2:
        #    readCSV2 = csv.reader(csvfile2, delimiter=',')
        #    for row2 in readCSV2:
                #print(row1[2])
                #print(row2[2])
                #print(row2[2])
                #print(get_word_len(row1[2]))
                #print(find_cos(row1[2], row1[2]))
                #print(find_cos(row1[2],row2[2]))
                #ikprint(row1[2],row2[2])
        #        count+=1
        #        count-=1
        #count+=1
        #print(count)


print("final count",count)
print("--- %s seconds ---" % (time.time() - start_time))



