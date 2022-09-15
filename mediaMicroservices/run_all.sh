for i in $(seq 1 $1)
do
    for j in $(seq 1 $1)
    do
        ./setup.sh $i $j $1
    done
done

