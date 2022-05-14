import pandas as pd
import requests
import json
import numpy as np
import matplotlib.pyplot as plt

FileName1 = './sa_population2.csv'
SERVER = "http://admin:admin@172.26.130.6:5984/historic_melb/"

def drawTweetsVSPopulation(showNumber = 10):
    """ Draw the graph Tweets VS Population
    """

    li1 = []
    li2 = []
    r = getTweetsVSPopulation()
    for k, v in r.items():
        li1.append( (k,v['tweetCount']) )
        li2.append( (k,v['populationCount']) )

    li1 = sorted(li1, key=_takeSecond, reverse=True)
    li2 = sorted(li2, key=_takeSecond, reverse=True)
    li2 =li2[:showNumber]
    li1= li1[:showNumber]
    # plt.figure(1)
    # plt.subplot(211)
    # plt.hist(li1,li2)
    # plt.subplot(212)
    # plt.hist(li1,li3)
    plt.rcdefaults()

    fig,ax = plt.subplots()

    ax.barh(np.arange(len(li1)), [x[1] for x in li2] , align='edge')
    ax.set_yticks(np.arange(len(li1)))
    ax.set_yticklabels([x[0] for x in li2])
    ax.invert_yaxis()
    ax.set_xlabel('populationCount')
    ax.set_title('Top ' +str(showNumber) + ' regions for population')

    plt.show()

    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(np.arange(len(li2)), [x[1] for x in li2], align='edge')
    ax.set_yticks(np.arange(len(li2)))
    ax.set_yticklabels([x[0] for x in li2])
    ax.invert_yaxis()
    ax.set_xlabel('tweetsCount')
    ax.set_title('Top ' + str(showNumber) + ' regions for tweet numbers.')

    plt.show()


def getTweetsVSPopulation():
    """Returns a dict {'Brunswick East': {'tweetCount': 7, 'populationCount': 13293}, ...},
    where 'Brunswick East' is sa2 name.
    """

    PopRes = getSa2population()
    res = dict()
    q_res = _queryDesign()['rows']
    for kv in q_res:
        if kv['key'][2] not in PopRes:
            print(kv['key'][2], ' has no AURIN data')
        else:
            res[kv['key'][2]] = {"tweetCount": kv['value']['count'], "populationCount": PopRes[kv['key'][2]]}
    return res

def getSa2population():
    """Returns a dict, key is sa2 name, value is its population"""
    return _getSa2pop(desiredCol=' persons_num')


def getSa2Malepopulation():
    """Returns a dict, key is sa2 name, value is its male population"""
    return _getSa2pop(desiredCol=' males_num')


def getSa2Femalepopulation():
    """Returns a dict, key is sa2 name, value is its female population"""
    return _getSa2pop(desiredCol=' females_num')


def _getSa2pop(fileName=FileName1, desiredCol=' persons_num'):
    """Returns a dict, key is sa2 name, value is the desiredCol"""

    sa2Population = dict()
    df = pd.read_csv(fileName)
    for index, row in df.iterrows():
        if row[' sa2_name16'] not in sa2Population:
            sa2Population[row[' sa2_name16']] = row[desiredCol]
        else:
            sa2Population[row[' sa2_name16']] += row[desiredCol]
    return sa2Population


def _queryDesign(serverURL = SERVER):
    x = requests.get(serverURL + '_design/attitude/_view/sa_sum_count?group_level=3')
    x = json.loads(x.text)
    return x

def _takeSecond(elem):
    return elem[1]
if __name__ == "__main__":
    # PopRes = getSa2population()
    # print(PopRes)
    # res = getSa2Malepopulation()
    # print(res)
    # res = getSa2Femalepopulation()
    # print(res)
    # r = getTweetsVSPopulation()
    # print(r)
    drawTweetsVSPopulation()
