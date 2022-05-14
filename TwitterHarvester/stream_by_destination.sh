#!/bin/bash

# @author Team 31, Melborune, 2022
#
# Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
# Zhen Cai (1049487), Ziqi Zhang (1241157)

nohup python3 stream.py -q '(Balaclava OR "Box hill" OR Camberwell OR Brunswick OR Malvern OR Docklands OR Flinders OR Footscray OR Moreland OR "Port Melbourne" OR "St Kilda" OR Toorak OR Lygon OR Brunswick OR Caulfield OR "La Trobe" OR Collingwood OR Southbank) (myki OR tram OR trams OR PTV) lang:en -is:retweet' -d melb_db -b ${bearer} &
