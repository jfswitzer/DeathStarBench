./wrk -D exp -d 60 -L -s ./scripts/media-microservices/compose-review.lua http://$1:8080/wrk2-api/review/compose -R $2
