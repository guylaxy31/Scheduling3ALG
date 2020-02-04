import random

# RAND FOR DATASET 1
dataset1 = [0]*60
i = 0
while i < 42:
    dataset1[i]=random.randint(2,8)
    i += 1

while i < 54:
    dataset1[i]=random.randint(20,30)
    i += 1

while i < 60:
    dataset1[i]=random.randint(35,40)
    i += 1

random.shuffle(dataset1)
tmpdataset1 = dataset1.copy()

# RAND FOR DATASET 2 
dataset2 = [0]*40
i = 0
while i < 20 :
    dataset2[i]=random.randint(2,8)
    i += 1

while i < 32 :
    dataset2[i]=random.randint(20,30)
    i += 1

while i < 40:
    dataset2[i]=random.randint(35,40)
    i += 1

random.shuffle(dataset2)
tmpdataset2 = dataset2.copy()

# RAND FOR DATASET 3
dataset3 = [0]*20
i = 0
while i < 8 :
    dataset3[i]=random.randint(2,8)
    i += 1

while i < 16 :
    dataset3[i]=random.randint(20,30)
    i += 1

while i < 20:
    dataset3[i]=random.randint(35,40)
    i += 1

random.shuffle(dataset3)
tmpdataset3 = dataset3.copy()

print("\n")
print('------------------ First Come First Served [ FCFS ] ------------------')
print("\n")
print('[ ############ DATASET 1 PROCESS IN QUEUE ############ ]')
print(dataset1)
with open('dataset1fcfs.txt', 'w') as f:
    for item in dataset1:
        f.write("%s," % item)

waitT = 0
avgWaitT = 0
k=0
f = open("dataset1fcfswait.txt", "w")
while k < len(dataset1):
    
    if k == 0:
        waitT += 0
        k += 1
        f.write(str(waitT)+",")  
        continue

    waitT += dataset1[k-1]
    f.write(str(waitT)+",")  
    k += 1
avgWaitT = waitT/len(dataset1)

f.close()
print('Waiting time is',waitT)
print('Average waiting time is',avgWaitT)
q=round(avgWaitT)+1

print("\n")
print('[ ############ DATASET 2 PROCESS IN QUEUE ############ ]')
print(dataset2)
with open('dataset2fcfs.txt', 'w') as f:
    for item in dataset2:
        f.write("%s," % item)

waitT2 = 0
avgWaitT2 = 0
k=0
f = open("dataset2fcfswait.txt", "w")
while k < len(dataset2):
    
    if k == 0:
        waitT2 += 0
        k += 1
        f.write(str(waitT2)+",")  
        continue

    waitT2 += dataset2[k-1]
    f.write(str(waitT2)+",")  
    k += 1
avgWaitT2 = waitT2/len(dataset2)

f.close()
print('Waiting time is',waitT2)
print('Average waiting time is',avgWaitT2)
q2=round(avgWaitT2)+1

print("\n")
print('[ ############ DATASET 3 PROCESS IN QUEUE ############ ]')
print(dataset3)
with open('dataset3fcfs.txt', 'w') as f:
    for item in dataset3:
        f.write("%s," % item)

waitT3 = 0
avgWaitT3 = 0
k=0
f = open("dataset3fcfswait.txt", "w")
while k < len(dataset3):
    
    if k == 0:
        waitT3 += 0
        k += 1
        f.write(str(waitT3)+",")  
        continue
    waitT3 += dataset3[k-1]
    f.write(str(waitT3)+",")   
    k += 1
avgWaitT3 = waitT3/len(dataset3)

f.close()
print('Waiting time is',waitT3)
print('Average waiting time is',avgWaitT3)
q3=round(avgWaitT3)+1

print("\n")
print('------------------ Shortest-Job-First [ SJF ] ------------------')
dataset1.sort()
dataset2.sort()
dataset3.sort()

with open('dataset1sjf.txt', 'w') as f:
    for item in dataset1:
        f.write("%s," % item)
        
with open('dataset2sjf.txt', 'w') as f:
    for item in dataset2:
        f.write("%s," % item)
        
with open('dataset3sjf.txt', 'w') as f:
    for item in dataset3:
        f.write("%s," % item)

print("\n")
print('[ ############ DATASET 1 PROCESS IN QUEUE ############ ]')

print(dataset1)

waitT = 0
k=0
f = open("dataset1jsfswait.txt", "w")
while k < len(dataset1):
    
    if k == 0:
        waitT += 0
        k += 1
        f.write(str(waitT)+",")  
        continue

    waitT += dataset1[k-1]
    f.write(str(waitT)+",") 
    k += 1
avgWaitT = waitT/len(dataset1)
f.close()
print('Waiting time is',waitT)
print('Average waiting time is',avgWaitT)

print("\n")
print('[ ############ DATASET 2 PROCESS IN QUEUE ############ ]')

print(dataset2)

waitT2 = 0
avgWaitT2 = 0
k=0
f = open("dataset2jsfswait.txt", "w")
while k < len(dataset2):
    
    if k == 0:
        waitT2 += 0
        k += 1
        f.write(str(waitT2)+",")  
        continue

    waitT2 += dataset2[k-1]
    k += 1
    f.write(str(waitT2)+",") 
avgWaitT2 = waitT2/len(dataset2)
f.close()
print('Waiting time is',waitT2)
print('Average waiting time is',avgWaitT2)

print("\n")
print('[ ############ DATASET 3 PROCESS IN QUEUE ############ ]')

print(dataset3)

waitT3 = 0
avgWaitT3 = 0
k=0
f = open("dataset3jsfswait.txt", "w")
while k < len(dataset3):
    
    if k == 0:
        waitT3 += 0
        k += 1
        f.write(str(waitT3)+",")  
        continue

    waitT3 += dataset3[k-1]
    f.write(str(waitT3)+",") 
    k += 1
avgWaitT3 = waitT3/len(dataset3)
f.close()
print('Waiting time is',waitT3)
print('Average waiting time is',avgWaitT3)

print('\n')
print('------------------ Round Robin [ RR ] ------------------')

print("\n")
print('[ ############ DATASET 1 PROCESS IN QUEUE ############ ]')
print(tmpdataset1)

k = 0
waitqT = 0
f = open("dataset1rrbwait.txt", "w")
while sum(tmpdataset1) != 0:
    if tmpdataset1[k] > q:
        waitqT += q
        f.write(str(waitqT)+",") 
        tmpdataset1[k] = tmpdataset1[k]-q       
    else:
        waitqT += tmpdataset1[k]
        f.write(str(waitqT)+",") 
        tmpdataset1[k] = 0
    if k < len(tmpdataset1)-1:
        k += 1
    else:
        k = 0

avgWaitT = waitqT/len(tmpdataset1)
f.close()
print('Time quantum is',q)
print('Waiting time is',waitqT)
print('Average waiting time is',avgWaitT)
    
print('\n')
print('[ ############ DATASET 2 PROCESS IN QUEUE ############ ]')
print(tmpdataset2)

k = 0
waitqT2 = 0
f = open("dataset2rrbwait.txt", "w")
while sum(tmpdataset2) != 0:
    if tmpdataset2[k] > q2:
        waitqT2 += q2
        f.write(str(waitqT2)+",") 
        tmpdataset2[k] = tmpdataset2[k]-q2        
    else:
        waitqT2 += tmpdataset2[k]
        f.write(str(waitqT2)+",")         
        tmpdataset2[k] = 0
    if k < len(tmpdataset2)-1:
        k += 1
    else:
        k = 0

avgWaitT2 = waitqT2/len(tmpdataset2)
f.close()
print('Time quantum is',q2)
print('Waiting time is',waitqT2)
print('Average waiting time is',avgWaitT2)

print('\n')
print('[ ############ DATASET 3 PROCESS IN QUEUE ############ ]')
print(tmpdataset3)
k = 0
waitqT3 = 0
f = open("dataset3rrbwait.txt", "w")
while sum(tmpdataset3) != 0:
    if tmpdataset3[k] > q3:
        waitqT3 += q3
        f.write(str(waitqT3)+",")         
        tmpdataset3[k] = tmpdataset3[k]-q3        
    else:
        waitqT3 += tmpdataset3[k]
        f.write(str(waitqT3)+",")                 
        tmpdataset3[k] = 0
    if k < len(tmpdataset3)-1:
        k += 1
    else:
        k = 0
    
avgWaitT3 = waitqT3/len(tmpdataset3)
f.close
print('Time quantum is',q3)
print('Waiting time is',waitqT3)
print('Average waiting time is',avgWaitT3)