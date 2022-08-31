docker service rm $(docker service ls -q)
docker stack deploy --compose-file=docker-compose.yml teststack
