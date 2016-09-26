CORPUS=$1
OUTPUT=$2

echo "Testing tfidf.py"
for f in $CORPUS/*.xml
do
    echo -n .
    name=$(basename -s .xml $f)
    python tfidf.py $CORPUS $f > /tmp/$name.tfidf
    python wordcompare.py /tmp/$name.tfidf $OUTPUT/$name.tfidf
done
echo

echo "Testing common.py"
for f in $CORPUS/*.xml
do
    #echo $f
    echo -n .
    name=$(basename -s .xml $f)
    python common.py $f > /tmp/$name.count
    python wordcompare.py /tmp/$name.count $OUTPUT/$name.count
done
echo