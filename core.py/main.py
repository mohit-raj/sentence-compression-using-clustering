import math
import textmining
from operator import itemgetter, attrgetter

class article (object):

    s_id = 0
    s_length = 0
    s_normalised_length = 0.0

    def __init__(self, index):
        self.index = index


if __name__ == '__main__':

    noOfSentences = 0
    summation = 0.0

    with open('sample-article.txt') as file:
        for eachLine in file:
            summation += len(eachLine.split()) ** 2
            noOfSentences += 1
    
    summation = math.sqrt(summation)
    obj = []

    for i in range(noOfSentences):
        obj.append(article(i))

    index = 0
    
    with open('sample-article.txt') as file:
        for eachLine in file:
            
            obj[index].s_id = index
            obj[index].s_length = len(eachLine.split())
            obj[index].s_normalised_length = obj[index].s_length / summation
            index += 1
     
    for i in range(noOfSentences):
        print obj[i].s_length
        print obj[i].s_normalised_length
        print '.'
    
    # obj = sorted(obj, key = lambda article: article.s_length) 

    pointFirst = min(obj,key = attrgetter('s_length'))
    pointSecond = max(obj, key = attrgetter('s_length'))

    # print pointFirst.s_normalised_length
    # print pointSecond.s_normalised_length


    # # for i in range(noOfSentences):
    #     print obj[i].s_id
    # pointFirst = min_num
    # pointSecond = obj[len(obj) - 1]

    # print noOfSentences

    cluster = [[] for n in range(noOfSentences)]
    cluster[0].append(pointFirst)
    cluster[1].append(pointSecond)

    # for i in range(1, (len(obj) - 1)):

    #     distSimilarityFirst = pointFirst.s_normalised_length * obj[i].s_normalised_length
    #     distSimilaritySecond = pointSecond.s_normalised_length * obj[i].s_normalised_length

    #     if(distSimilarityFirst <= distSimilaritySecond):
    #         # print distSimilarityFirst
    #         # print distSimilaritySecond
    #         # print '.'
    #         print "kk"
    #         cluster[0].append(obj[i])

    #     elif(distSimilaritySecond <= distSimilarityFirst):
    #         # print "mohit"
    #         cluster[1].append(obj[i])

    # for i in cluster[1]:
    #     print i.s_id