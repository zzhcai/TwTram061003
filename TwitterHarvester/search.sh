#!/bin/bash

# @author Team 31, Melborune, 2022
#
# Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
# Zhen Cai (1049487), Ziqi Zhang (1241157)

export query="("
query+="$(python3 get_query_keywords.py -f "landmarks.txt")"
query+=") (myki OR tram OR trams) lang:en -is:retweet"
echo $query
python3 search.py -q "(melbourne) (myki OR tram OR trams) lang:en -is:retweet" -d melb_db -u user_db
