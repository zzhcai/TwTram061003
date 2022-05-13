export query="("
query+="$(python3 get_query_keywords.py -f "landmarks.txt")"
query+=") (myki OR tram OR trams) lang:en -is:retweet"
echo $query
python3 search.py -q "(melbourne OR ) (myki OR tram OR trams) lang:en -is:retweet" -d melb_db -u user_db