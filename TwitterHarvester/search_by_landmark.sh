#!/bin/bash

# @author Team 31, Melborune, 2022
#
# Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
# Zhen Cai (1049487), Ziqi Zhang (1241157)

nohup ython3 search.py -q '(Melbourne OR "Federation Square" OR "Luna Park" OR "Melbourne Cricket Ground" OR "Melbourne Museum" OR "Melbourne Zoo" OR "Melbourne Showgrounds" OR "Victoria Market" OR "National Gallery of Victoria" OR "Royal Botanic Gardens" OR "Royal Exhibition Building" OR Monash OR RMIT OR Deakin OR Swinburne OR "Yarra River" OR "Shrine of Remembrance" OR Flagstaff OR swanston OR "Curtin House" OR "Little Bourke" OR "Melbourne Aquarium" OR "Little Collins") (myki OR tram OR trams OR PTV) lang:en -is:retweet' -d melb_db &
