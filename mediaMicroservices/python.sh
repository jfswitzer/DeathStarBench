python3 scripts/write_movie_info.py -c datasets/tmdb/casts.json -m datasets/tmdb/movies.json -a $1 && scripts/register_users.sh $1 && scripts/register_movies.sh $1

