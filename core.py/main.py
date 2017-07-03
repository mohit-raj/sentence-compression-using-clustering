import math
import textmining
from operator import itemgetter, attrgetter

class article (object):

    s_id = 0
    s_length = 0
    s_string =""

    def __init__(self, index):
        self.index = index


if __name__ == '__main__':

    noOfSentences = 0
    summation = 0.0

    with open('/home/mohit/Desktop/sentence-compression-using-clustering/core.py/Input documents CORPUS/sample-article-1.txt') as file:
        for eachLine in file:
            summation += len(eachLine.split()) ** 2
            noOfSentences += 1
    
    summation = math.sqrt(summation)
    obj = []
    doc = []

    for i in range(noOfSentences):
        obj.append(article(i))

    index = 0
    
    with open('/home/mohit/Desktop/sentence-compression-using-clustering/core.py/Input documents CORPUS/sample-article-1.txt') as file:
        for eachLine in file:
            
            obj[index].s_id = index
            obj[index].s_string = eachLine
            obj[index].s_length = len(eachLine.split())
            index += 1
    # print noOfSentences

    for i in range(noOfSentences):
        doc.append(obj[i].s_string)
    
    matrix = textmining.TermDocumentMatrix();
    
    for i in doc:
        matrix.add_doc(i)

    matrix.write_csv('/home/mohit/Desktop/sentence-compression-using-clustering/core.py/Matrix Generated Output/matrix.csv', cutoff=1)
    # for row in matrix.rows(cutoff=1):
    #     print row

    # for column in matrix.columns(cutoff=1):
    #     print column

    count = 0
    with open('/home/mohit/Desktop/sentence-compression-using-clustering/core.py/Matrix Generated Output/matrix.csv') as file:
        for eachLine in file:
            count += 1
            if(count == 1):
                continue
            else:
                
