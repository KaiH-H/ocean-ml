#!/bin/bash

cd 
cd Desktop/session-4-1/
echo "Start"
for LINE in date_list.txt
	do 
	python write_exec_files.py $LINE
	chmod +x *
	./vectorq.exec
	./omegainv.exec
	done