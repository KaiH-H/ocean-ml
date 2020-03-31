#!/bin/bash

cd 
cd Desktop/Internships/ocean-ml/session-3-12/
echo "Start"
cat date_list.txt | while read line
do 
	python writing-exec-files.py $line
	chmod +x *
	./vectorq.exec
	./omegainv.exec