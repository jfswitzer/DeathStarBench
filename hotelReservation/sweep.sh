for i in 6500 7000 8000 9000 10000
#for i in 500 1000
do
    ./wrk2/wrk -D exp -d 60 -L -s ./wrk2/scripts/hotel-reservation/mixed-workload_type_1.lua http://localhost:5000 -R $i > 10d_60s_$i.out
    sleep 30
done
