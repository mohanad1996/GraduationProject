from nltk import word_tokenize, pos_tag, WordNetLemmatizer
from nltk.corpus import stopwords


#def get_pos(message):
#    review_tokenized = []
#    message=str(message)
#    lmt = WordNetLemmatizer()
#    tokenize_words = word_tokenize(message.lower(),language='english')
#    pos_word = pos_tag(tokenize_words)
#    tokenize_words = ["_".join([lmt.lemmatize(i[0]),i[1]]) for i in pos_word if (i[0] not in stopwords.words("english") and len(i[0]) > 2)]
#    review_tokenized.append(tokenize_words)
#    print(review_tokenized)


    #message= review_tokenized


def get_pos(message):
    message=str(message).lower()

    tokenized = word_tokenize(message)
    tagged = pos_tag(tokenized)
    dev_j=0
    dev_n=0
    count=0
    #print(tagged)
    for i in tagged:
        if i[1]=="JJ": # NN for nouns, RB for adverbs, JJ for adjective, VBP for verbs....
            #print(i)
            count+=1
    if len(tagged)!=0:
        dev_j=count/len(tagged)

    count=0;
    for i in tagged:
        if i[1] == "VB":  # NN for nouns, RB for adverbs, JJ for adjective , VBP for verbs....
            #print(i)
            count += 1
    if len(tagged)!=0:
        dev_n=count/len(tagged)

    #print(dev)
    return dev_j,dev_n
    #print(len(tagged))


#print(get_pos("this is a sample to test test pos taggers bad good"))