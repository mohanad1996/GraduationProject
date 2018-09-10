from nltk.tokenize import sent_tokenize, word_tokenize


def is_brand(message):
    count=0
    list=["expensive","aa","asda","asdd","as","as"]########
    word_tokens = word_tokenize(message)

    for i in word_tokens:
        if i in list:
            count+=1

    print(count)
    dev=count/len(word_tokens)
    return dev

print(is_brand("expensive qasd asd asd aa aasd"))