python3 fill_template.py $1 $2
sudo docker service rm $(sudo docker service ls -q)
sudo docker stack deploy --compose-file=docker-temp.yml dsb
sleep 60
python3 scripts/write_movie_info.py -c datasets/tmdb/casts.json -m datasets/tmdb/movies.json -a localhost && scripts/register_users.sh localhost && scripts/register_movies.sh localhost
sleep 60
./test_sweep.sh $1$2_$3
rm docker-temp.yml
sleep 60
