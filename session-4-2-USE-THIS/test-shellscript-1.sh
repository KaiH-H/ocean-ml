#!/bin/bash


cd 
cd Desktop/Internships/ocean-ml/session-4-2-USE-THIS/

echo "Start"

while read line; do
	echo "$line"
	python write_exec_files.py $line
	chmod +x *
	gfortran -O3 -o vectorq.exe vectorq.f
	gfortran -O3 -o omegainv.exe omegainv.f
	./vectorq.exec
 	./omegainv.exec
done <date_list.txt

# FileNotFoundError: [Errno 2] No such file or directory: '/Users/brownscholar/Desktop/session-4-2/vectorq.exec'


# while read line; do
# do 

# 	python write_exec_files.py $line
# 	chmod +x *
# 	./vectorq.exec
# 	./omegainv.exec
# done <file