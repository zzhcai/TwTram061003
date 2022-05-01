#!/bin/bash

# @author Team 31, Melborune, 2022
#
# Bingzhe Jin (1080774), Hongwei Chen (891632), Tian Hui (1054513),
# Zhen Cai (1049487), Ziqi Zhang (1241157)

. ./openrc.sh; ansible-playbook -u ubuntu --key-file=cloud.key --ask-become-pass main.yaml
