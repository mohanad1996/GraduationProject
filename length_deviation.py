from length_review import get_avg_len

def get_deviation(message):
    threshold=0.5 #could be changed 
    my_flag=0
    avg_len=get_avg_len();
    print(avg_len);

    dev=len(message)/avg_len

    if(dev<0.5):
        my_flag=1
    else:
        my_flag=0

    return my_flag

print(get_deviation("mohanad  mohanad mohanad mohanad mohanad mohanad mohanad mohanad mohanad "))