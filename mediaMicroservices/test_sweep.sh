./run.sh localhost 25 > /dev/null
for i in 25 50 60 75 100 150
do
    echo $i
    ./run.sh localhost $i > $1_60s_r$i.out
    sleep 10
done
