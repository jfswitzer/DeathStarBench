for i in 300 400 450 500 550 600 800 1000 1500 2000 2200 2400 2600 2800 3000
do
    ./wrk2/wrk -D exp -d 60 -L -s ./wrk2/scripts/hotel-reservation/mixed-workload_type_1.lua http://localhost:5000 -R $i > 6d_60s_$i.out
    sleep 30
done
