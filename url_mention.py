
def is_url(message):
    my_flag=0
    if(((".com") in message) and (("www.") in message)):
        if(("www.yelp.com") in message):
            my_flag=0
        else:
            my_flag=1

    return my_flag


print(is_url("www.asdasdas.com/asdasd/asdasdas/asdasd"))