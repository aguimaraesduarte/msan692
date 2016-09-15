#!/bin/bash

OUTPUT=.
MYSRC=~/Documents/msan692/pipeline

for t in TSLA VBK
do
	echo "Testing" $t

	# Test GET
	curl -s http://parrt.pythonanywhere.com/history/$t > /tmp/$t.html
	curl -s http://aguimaraesduarte.pythonanywhere.com/history/$t > $OUTPUT/$t.html	
        python $MYSRC/htmlcompare.py $OUTPUT/$t.html /tmp/$t.html

	# Test POST
	curl -s --data "ticker=$t" http://aguimaraesduarte.pythonanywhere.com/history/ > /tmp/post-$t.html
        python $MYSRC/htmlcompare.py $OUTPUT/$t.html /tmp/post-$t.html

	# Test GET JSON
	curl -s http://parrt.pythonanywhere.com/data/$t > /tmp/$t.json
	curl -s http://aguimaraesduarte.pythonanywhere.com/data/$t > $OUTPUT/$t.json
        python $MYSRC/jsoncompare.py $OUTPUT/$t.json /tmp/$t.json
done
