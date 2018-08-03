import re

def get_word_len(message):
    my_flag = 0
    number_of_words=0

    count = len(re.findall(r'\w+', message))
    avg_len=len(message.replace(" ",""))/count
    print(avg_len)
    if(avg_len>6 or avg_len <4):
        my_flag=1
    else:
        my_flag=0
    print(avg_len)
    return my_flag

print(get_word_len("maod mohanad nn mod mohanad mohanad mohanad mohanad mohanad mohanad mohanad mohanad mohanad"))
