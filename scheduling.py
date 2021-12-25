import heapq

class Process:
    def __init__(self, name, arrivalTime, cpuBurst, priority):
        self.name = name
        self.arrivalTime = arrivalTime
        self.cpuBurst = cpuBurst
        self.priority = priority


def readFile(name):
    file = open(name, "r")
    header = file.readline()
    header = header.split()
    processCount = int(header[0])
    quantumTime = int(header[1])

    processes = []

    for i in range(processCount):
        process = file.readline()
        process_detail = process.split()
        name = process_detail[0]
        arrivalTime = int(process_detail[1])
        cpuBurst = int(process_detail[2])
        priority = int(process_detail[3])

        processes.append(Process(name, arrivalTime, cpuBurst, priority))

    file.close()

    return processes, quantumTime


def FCFS(processes):
    file = open("FCFS.txt", "w")
    processes.sort(key=lambda x: x.arrivalTime, reverse=False)
    schedulingChart = "0"

    TT = [0] * len(processes)
    WT = [0] * len(processes)

    currentTime = 0

    for i in range(len(processes)):
        if currentTime < processes[i].arrivalTime:
            currentTime = processes[i].arrivalTime

        WT[i] = currentTime - processes[i].arrivalTime

        schedulingChart += f'~{processes[i].name}~'
        currentTime += processes[i].cpuBurst
        TT[i] = currentTime - processes[i].arrivalTime
        schedulingChart += str(currentTime)

    file.write("Scheduling chart: " + schedulingChart + '\n')
    for i in range(len(processes)):
        file.write(f"{processes[i].name}:\tTT={TT[i]}\tWT={WT[i]}\n")

    print(f'FCFS: {schedulingChart}')

    file.write(f'Average:\tTT={sum(TT) / len(TT)}\tWT={sum(WT) / len(WT)}')
    file.close()


def RR(processes, quantumTime):
    file = open("RR.txt", "w")
    processes.sort(key=lambda x: x.arrivalTime, reverse=False)
    schedulingChart = ""

    TT = [0] * len(processes)
    WT = [0] * len(processes)
    timeLeft = []

    for process in processes:
        timeLeft.append(process.cpuBurst)

    currentTime = 0

    queue = []
    processDone = []
    currentProcess = None
    runningProcess = None

    timeInQuantum = 0

    while True:
        for i in range(len(processes)):
            if processes[i].arrivalTime == currentTime:
                queue.append(i)

        if len(queue) == 0 and currentProcess is None:
            currentTime += 1
            continue

        if currentProcess is not None:
            if timeLeft[currentProcess] == 0:
                processDone.append(currentProcess)
                TT[currentProcess] = currentTime - processes[currentProcess].arrivalTime
                currentProcess = None
                timeInQuantum = 0

        if timeInQuantum == quantumTime:
            queue.append(currentProcess)
            currentProcess = None
            timeInQuantum = 0

        if len(processDone) == len(processes):
            schedulingChart += str(currentTime)
            break

        if currentProcess is None:
            currentProcess = queue[0]
            queue.pop(0)
            timeInQuantum = 0

        timeLeft[currentProcess] -= 1
        if currentProcess != runningProcess:
            runningProcess = currentProcess
            schedulingChart += str(currentTime)
            schedulingChart += f'~{processes[currentProcess].name}~'

        for i in queue:
            WT[i] += 1

        timeInQuantum += 1
        currentTime += 1

    file.write("Scheduling chart: " + schedulingChart + '\n')
    for i in range(len(processes)):
        file.write(f"{processes[i].name}:\tTT={TT[i]}\tWT={WT[i]}\n")

    print(f'RR: {schedulingChart}')

    file.write(f'Average:\tTT={sum(TT) / len(TT)}\tWT={sum(WT) / len(WT)}')
    file.close()


def SJF(processes):
    file = open("SJF.txt", "w")
    processes.sort(key=lambda x: x.arrivalTime, reverse=False)
    schedulingChart = ""

    timeLeft = []

    for process in processes:
        timeLeft.append(process.cpuBurst)

    queue = []
    processDone = []
    currentProcess = None

    TT = [0] * len(processes)
    WT = [0] * len(processes)

    runningProcess = None

    currentTime = 0

    while True:
        for i in range(len(processes)):
            if processes[i].arrivalTime == currentTime:
                queue.append(i)

        if len(queue) == 0 and currentProcess is None:
            currentTime += 1
            continue

        if currentProcess is None:
            currentProcess = queue[0]
            queue.pop(0)

        for i in queue:
            if timeLeft[i] < timeLeft[currentProcess]:
                queue.append(currentProcess)
                currentProcess = i
                queue.remove(i)

        timeLeft[currentProcess] -= 1

        if currentProcess != runningProcess:
            runningProcess = currentProcess
            schedulingChart += str(currentTime)
            schedulingChart += f'~{processes[currentProcess].name}~'

        currentTime += 1

        if timeLeft[currentProcess] == 0:
            processDone.append(currentProcess)
            TT[currentProcess] = currentTime - processes[currentProcess].arrivalTime
            currentProcess = None

        if len(processDone) == len(processes):
            schedulingChart += str(currentTime)
            break



        for i in queue:
            WT[i] += 1

    file.write("Scheduling chart: " + schedulingChart + '\n')
    for i in range(len(processes)):
        file.write(f"{processes[i].name}:\tTT={TT[i]}\tWT={WT[i]}\n")

    print(f'SJF: {schedulingChart}')

    file.write(f'Average:\tTT={sum(TT) / len(TT)}\tWT={sum(WT) / len(WT)}')
    file.close()


def priority(processes):
    file = open("Priority.txt", "w")
    processes.sort(key=lambda x: x.arrivalTime, reverse=False)
    schedulingChart = ""

    timeLeft = []

    for process in processes:
        timeLeft.append(process.cpuBurst)

    queue = []
    processDone = []
    currentProcess = None

    TT = [0] * len(processes)
    WT = [0] * len(processes)

    runningProcess = None

    currentTime = 0

    while True:
        for i in range(len(processes)):
            if processes[i].arrivalTime == currentTime:
                heapq.heappush(queue, (processes[i].priority, i))

        print(queue)

        if len(queue) == 0 and currentProcess is None:
            currentTime += 1
            continue

        if currentProcess is None:
            currentProcess = queue[0][1]
            heapq.heappop(queue)

        if len(queue) > 0:
            if currentProcess != queue[0][1]:
                heapq.heappush(queue, (processes[currentProcess].priority, currentProcess))
                currentProcess = queue[0][1]
                heapq.heappop(queue)

        timeLeft[currentProcess] -= 1

        if currentProcess != runningProcess:
            runningProcess = currentProcess
            schedulingChart += str(currentTime)
            schedulingChart += f'~{processes[currentProcess].name}~'

        currentTime += 1

        if timeLeft[currentProcess] == 0:
            processDone.append(currentProcess)
            TT[currentProcess] = currentTime - processes[currentProcess].arrivalTime
            currentProcess = None

        if len(processDone) == len(processes):
            schedulingChart += str(currentTime)
            break

        for i in queue:
            WT[i[1]] += 1

    file.write("Scheduling chart: " + schedulingChart + '\n')
    for i in range(len(processes)):
        file.write(f"{processes[i].name}:\tTT={TT[i]}\tWT={WT[i]}\n")

    print(f'Priority: {schedulingChart}')

    file.write(f'Average:\tTT={sum(TT) / len(TT)}\tWT={sum(WT) / len(WT)}')
    file.close()

processes, quantumTime = readFile("input.txt")
FCFS(processes)
RR(processes, quantumTime)
SJF(processes)
priority(processes)
