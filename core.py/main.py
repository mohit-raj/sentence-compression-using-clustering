import math
import csv
import textmining
import numpy
from operator import itemgetter, attrgetter

class article (object):

    s_id = 0
    s_length = 0
    s_mod_lenght = 0
    s_string =""

    def __init__(self, index):
        self.index = index


if __name__ == '__main__':

    noOfSentences = 0

    with open('/home/mohit/Desktop/sentence-compression-using-clustering/Input documents CORPUS/sample-article-1.txt') as file:
        for eachLine in file:
            noOfSentences += 1
    
    obj = []
    doc = []

    for i in range(noOfSentences):
        obj.append(article(i))

    index = 0
    
    with open('/home/mohit/Desktop/sentence-compression-using-clustering/Input documents CORPUS/sample-article-1.txt') as file:
        for eachLine in file:
            
            obj[index].s_id = index
            obj[index].s_string = eachLine
            obj[index].s_length = len(eachLine.split())
            obj[index].s_mod_lenght = 0
            index += 1

    for i in range(noOfSentences):
        doc.append(obj[i].s_string)
    
    matrix = textmining.TermDocumentMatrix();
    
    for i in doc:
        matrix.add_doc(i)

    matrix.write_csv('/home/mohit/Desktop/sentence-compression-using-clustering/Matrix Generated Output/matrix.csv', cutoff=1)

    data = list(csv.reader(open('/home/mohit/Desktop/sentence-compression-using-clustering/Matrix Generated Output/matrix.csv')))
  
    index = 0
    for rows in data[1:]:
        for item in rows:
            obj[index].s_mod_lenght = obj[index].s_mod_lenght + (int(item) ** 2)


        obj[index].s_mod_lenght = math.sqrt(obj[index].s_mod_lenght)
        index += 1

    countOfTerms = 0

    for rows in data[1]:
        for item in rows:
            countOfTerms += 1
        

    index = 0
    i = 1
    j = 1
    tempSum = 0.0
               
    while(i <= 4):
        j = 1
        index = 0
        while(j <= 4):
            if(i != j):
                index = 0
                while(index < countOfTerms):
                    tempSum = tempSum + ((float)(data[i][index]) / obj[i-1].s_mod_lenght) * ((float)(data[j][index]) / obj[j-1].s_mod_lenght)
                    index += 1
                print numpy.arccos(tempSum)
                tempSum = 0.0
                index = 0
            j += 1
        i += 1