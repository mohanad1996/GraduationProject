from length_review import get_max_len

avg_len = get_max_len();


def get_deviation(message):
    threshold=0.5 #could be changed 
    my_flag=0
    #print(avg_len);
    dev=len(message)/avg_len
    if(dev<0.5):
        my_flag=1
    else:
        my_flag=0

    return dev

