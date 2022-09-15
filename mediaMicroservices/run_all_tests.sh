#take all nodes offline
for i in {1..10}
do
    sudo docker node update --availability drain panik$i
done

#add them in one at a time and run tests on $i sized cluster
for i in {1..10}
do
    sudo docker node update --availability active panik$i    
    ./run_all.sh $i $i
done
