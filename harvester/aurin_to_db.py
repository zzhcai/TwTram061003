"""
@author Team 31, Melborune, 2022

Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
Zhen Cai (1049487), Ziqi Zhang (1241157)

"""

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
    # options = readCommand(sys.argv[1:])
    # database = "sa2_income_14_db"
    # database = "sa2_emotion_14_db"
    # database = "sa4_population_14_db"
    # database = "sa3_mental_14_db"
    # database = "sa3_abs_population_14_db"
    database = "sa3_travel_16_db"

    SERVER = "http://admin:admin@172.26.130.6:5984"

    # connecting CouchDB server
    server = couchdb.Server(SERVER)

    # connect to or create a database
    try:
        db = server[database]
    except couchdb.http.ResourceNotFound:
        db = server.create(database)

    # file = "/Users/azathoth/Downloads/SA2_Estimates_of_Personal_Income_-_Own_Unincorporated_Income_2010-2015.json/abs_epi_own_unincorporated_income_sa2_2010_15-4898879420225850498.json"
    # with open(file) as f:
    #     dic = json.load(f)
    #     keys = dic['features'][0]['properties'].keys()
    #     keys = [i for i in keys if i != 'sa2_name16' and i != 'sa2_code_2016']
    #     for i in dic['features']:
    #         d = {'name': i['properties']['sa2_name16']}
    #         for j in keys:
    #             d[j] = i['properties'][j]
    #         db.save({'properties': d})
            
    # file = "/Users/azathoth/Downloads/AEDC_-_Emotional_Maturity__SA2__2009-2018.json/aedc_emotional_sa2_2009_2018-7801432198181255086.json"
    # with open(file) as f:
    #     dic = json.load(f)
    #     # print(dic['features'][0]['properties'])
    #     keys = dic['features'][0]['properties'].keys()
    #     keys = [i for i in keys if i != 'sa2_main16' and i != 'code']
    #     for i in dic['features']:
    #         d = {}
    #         for j in keys:
    #             d[j] = i['properties'][j]
    #         db.save({'properties': d})

    # file = "/Users/azathoth/Downloads/SA4_Population___People_-_National_Regional_Profile_2010-2014.json/sa4_nrp_people_2010_2014-6101965738166165191.json"
    # with open(file) as f:
    #     dic = json.load(f)
    #     # print(dic['features'][0]['properties'].keys())
    #     keys = dic['features'][0]['properties'].keys()
    #     keys = [i for i in keys if i != 'sa4_code_2011' and i != 'sa4_name_2011' and i != 'year']
    #     for i in dic['features']:
    #         d = {'name': i['properties']['sa4_name_2011']}
    #         for j in keys:
    #             d[j] = i['properties'][j]
    #         db.save({'properties': d})

    # file = "/Users/azathoth/Downloads/AIHW_-_Mental_Health_Services_-_Emergency_Department_Presentations_by_Demographics__SA3__2014-2018.json/aihw_mental_hlth_serv_emrgncy_presentations_demo_sa3_2014_18-3120990980095171391.json"
    # with open(file) as f:
    #     dic = json.load(f)
    #     # print(dic['features'][0]['properties'].keys())
    #     keys = dic['features'][0]['properties'].keys()
    #     keys = [i for i in keys if i != 'sa3_name' and i != 'fin_yr' and i != 'sa3_code']
    #     for i in dic['features']:
    #         d = {'name': i['properties']['sa3_name']}
    #         for j in keys:
    #             d[j] = i['properties'][j]
    #         db.save({'properties': d})


    # file = "/Users/azathoth/Downloads/ABS_-_Data_by_Region_-_Population___People__SA3__2011-2019.json/abs_data_by_region_pop_and_people_asgs_sa3_2011_2019-6884485796605196378.json"
    # with open(file) as f:
    #     dic = json.load(f)
    #     # print(dic['features'][0]['properties'].keys())
    #     keys = dic['features'][0]['properties'].keys()
    #     keys = [i for i in keys if i != 'sa3_name_2016' and i != 'year' and i != 'sa3_code_2016']
    #     for i in dic['features']:
    #         d = {'name': i['properties']['sa3_name_2016']}
    #         for j in keys:
    #             d[j] = i['properties'][j]
    #         db.save({'properties': d})

    file = "/Users/azathoth/Downloads/SA3-W22d_Method_of_Travel_to_Work_by_Age_by_Sex-Census_2016.json/sa3_w22d_method_of_travel_to_work_by_age_by_sx_census_2016-8533375896361131108.json"
    with open(file) as f:
        dic = json.load(f)
        # print(dic['features'][0]['properties'].keys())
        keys = dic['features'][0]['properties'].keys()
        keys = [i for i in keys if i != 'sa3_name16' and i != 'year' and i != 'sa3_code16']
        for i in dic['features']:
            d = {'name': i['properties']['sa3_name16']}
            for j in keys:
                d[j] = i['properties'][j]
            db.save({'properties': d})
        


