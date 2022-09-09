sudo docker service rm $(sudo docker service ls -q)
sudo docker stack deploy --compose-file=docker-compose.yml teststack
