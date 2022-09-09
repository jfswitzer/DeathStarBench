./wrk -D exp -d 60 -L -s ./scripts/social-network/compose-post.lua http://$1:8080/wrk2-api/post/compose -R $2
