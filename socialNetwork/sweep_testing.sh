for i in 300 400 450
do
    ./wrk2/wrk -D exp -d 60 -L -s ./wrk2/scripts/social-network/compose-post.lua http://localhost:8080 -R $i > 6d_60s_$i.out
    sleep 30
done
