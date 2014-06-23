for i in $(ls)
do
    tr -d '\r' < $i > $i-tmp
    mv $i-tmp $i
done
