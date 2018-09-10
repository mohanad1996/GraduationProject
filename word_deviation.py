import re

def get_word_len(message):
    my_flag = 0
    number_of_words=0
    avg_len=0
    count = len(re.findall(r'\w+', message))
    if(count!=0):
        avg_len=len(message.replace(" ",""))/count
    #print(avg_len)


    return avg_len

#print(get_word_len("maod mohanad nn mod mohanad mohanad mohanad mohanad mohanad mohanad mohanad mohanad mohanad"))
