for i in 2000 3000 4000 5000
do
        ./wrk -D exp -d 60 -L -s ./scripts/social-network/compose-post.lua http://localhost:8080/wrk2-api/post/compose -R $i > sn_1phone_r$i.out
done
