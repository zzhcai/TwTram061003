from optparse import OptionParser
import sys

def readCommand(argv):
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="keywords_file", help="enter keywords file", default="")
    options, others = parser.parse_args(argv)

    return options

options = readCommand(sys.argv[1:])
filename = options.keywords_file

with open(filename, 'r') as f:
    lines = f.readlines()
    keywords = [line.strip().strip(',') for line in lines if len(line) > 1]
    keywords_query = ' OR '.join(keywords)
    print(keywords_query)

