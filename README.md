# Scheduling

A program that calculates the Scheduling chart, TT and WT for each process in 4 ways of process scheduling: First Come First Serve, Round Robin, Shortest Job First and Priority Queue.
The input file name is "input.txt"
The first row is the number of processes and quantum time. The following rows are the processes in format: name, arrival time, time burst and priority.
</br>*Example input:*</br>
```
3 4
P1 0 24 3
P2 1 5 2
P3 2 3 1
```
Output files are named by the abbreviations of schedualing strategies: "FCFS.txt", "RR.txt", "SJF.txt", "Priority.txt".
</br>*Example output for the above input:*</br>
FCFS.txt
```
Scheduling chart: 0~P1~24~P2~29~P3~32
P1:	TT=24	WT=0
P2:	TT=28	WT=23
P3:	TT=30	WT=27
Average:	TT=27.333333333333332	WT=16.666666666666668
```
RR.txt
```
Scheduling chart: 0~P1~4~P2~8~P3~11~P1~15~P2~16~P1~32
P1:	TT=32	WT=8
P2:	TT=15	WT=10
P3:	TT=9	WT=6
Average:	TT=18.666666666666668	WT=8.0
```
SJF.txt
```
Scheduling chart: 0~P1~1~P2~2~P3~5~P2~9~P1~32
P1:	TT=32	WT=8
P2:	TT=8	WT=3
P3:	TT=3	WT=0
Average:	TT=14.333333333333334	WT=3.6666666666666665
```
Priority.txt
```
Scheduling chart: 0~P1~1~P2~2~P3~5~P2~9~P1~32
P1:	TT=32	WT=8
P2:	TT=8	WT=3
P3:	TT=3	WT=0
Average:	TT=14.333333333333334	WT=3.6666666666666665
```
