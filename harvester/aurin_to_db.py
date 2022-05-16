import sys
import couchdb
from optparse import OptionParser
import json

def readCommand(argv):
    parser = OptionParser()

    parser.add_option("-f", "--file", dest="file", help="enter file", default="")

    parser.add_option(
        "-d", "--database", dest="database", help="database name", default=""
    )
    
    options, otherjunk = parser.parse_args(argv)

    return options

# python3 aurin_to_db.py -f FILENAME -d DBNAME
if __name__ == "__main__":
    options = readCommand(sys.argv[1:])

    SERVER = "http://admin:admin@172.26.130.6:5984"

    # connecting CouchDB server
    server = couchdb.Server(SERVER)

    # connect to or create a database
    try:
        db = server[options.database]
    except couchdb.http.ResourceNotFound:
        db = server.create(options.database)

    with open(options.file) as f:
        dic = json.load(f);
        for i in dic['features']:
            db.save(i)
            