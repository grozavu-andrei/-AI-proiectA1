from nltk.stem import SnowballStemmer
import re, math
from collections import Counter

def extract_root(file_1,file_2):
    romana = SnowballStemmer("romanian")

    with open (file_1) as f:
        content = f.readlines()

    file = open(file_2,"w")

    for i in content:
        if (ord(i[0])>=65 and ord(i[0])<=90) or (ord(i[0])>=97 and ord(i[0])<=122):
            words = i[0:-1].split()
            for each in words:
                file.write(romana.stem(each) + ' ')
            file.write('\n')
    file.close()

WORD = re.compile(r'\w+')
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
     words = WORD.findall(text)
     return Counter(words)

def compute_sim(text1,text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine = get_cosine(vector1, vector2)
    print (cosine)

extract_root("1.txt","test1.txt")
extract_root("2.txt","test2.txt")
file = open ("test1.txt", "r")
text_1 = file.read()
file = open ("test2.txt", "r")
text_2 = file.read()
compute_sim(text_1,text_2)