import pandas as pd

FileName1 = './sa_population2.csv'


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


if __name__ == "__main__":
    res = getSa2population()
    print(res)
    res = getSa2Malepopulation()
    print(res)
    res = getSa2Femalepopulation()
    print(res)
