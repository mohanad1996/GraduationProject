
def is_url(message):
    my_flag=0
    if(((".com") in message) or (("www.") in message)):
        if(("yelp.com") in message and ("*.com") not in message):
            my_flag=0
        else:
            my_flag=1

    return my_flag


#print(is_url("yelp.com/asdasd/asdasdas/asdasd"))