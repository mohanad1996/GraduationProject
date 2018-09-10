import re
import math
import time
import sys
from collections import Counter
import nltk
from nltk.corpus import stopwords
from stemming.porter2 import stem
from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)


def get_result(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result


def find_cos(statment1,statment2):
    statment1=statment1.lower();
    statment2=statment2.lower();
    word_tokens = word_tokenize(statment1)
    word_tokens2 = word_tokenize(statment2)
    stop_words = set(stopwords.words('english'))
    snow = nltk.SnowballStemmer('english')
    filtered_sentence1 = [w for w in word_tokens if not w in stop_words]
    filtered_sentence1 = []


    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence1.append(w)

    filtered_sentence2 = [w for w in word_tokens2 if not w in stop_words]
    filtered_sentence2 = []

    for w in word_tokens2:
        if w not in stop_words:
            filtered_sentence2.append(w)

    statment1=''
    for word in filtered_sentence1:
        statment1+=snow.stem(word)+' '
    statment2=''
    for word in filtered_sentence2:
        statment2 += snow.stem(word)+' '



    statment1 = re.sub(r'[^\w\s]','',statment1).replace('  ',' ')
    statment2 = re.sub(r'[^\w\s]','',statment2).replace('  ',' ')




    #print(statment1)

    #print(statment2)

    return get_result(statment1,statment2)




start=time.time()

#print(find_cos("I came to Chicago on business and was initially supposed to stay downtown; however a colleague recommended this hotel--and I am so glad that they did! The attention to detail and finishing touches in my room are what made this hotel feel like home. Staying in a smaller hotel allowed me to connect with the local Chicago vibe while simultaneously enjoying exquisite service from the staff at a fraction of what it might cost to stay in a Magnificent Mile high-rise. Considering the quality ambiance and charm of this hidden Chicago treasure it made my trip a memorable experience. Not only was I able to secure a bike rental to avoid the high cost of renting a car but I also was directed to some of the local galleries in the West Loop by the friendly staff members.","I still love this place but the took Mu Shu off the menu. Â I am deeply saddened. Show owner comment Â»"))

#print(time.time()-start)