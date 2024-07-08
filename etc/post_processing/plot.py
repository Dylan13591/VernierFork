import sys
import matplotlib.pyplot as plt 
  
selfTime = [] 
regionNames = [] 

lineNumber = 0

for line in sys.stdin:
    if lineNumber <= 5:
        lineNumber += 1
    else:
        line = line.split()
        selfTime.append(float(line[3]))
        regionNames.append(line[8])

plt.bar(regionNames, selfTime, color = 'g', label = 'File Data') 
  
plt.xlabel('Region Names', fontsize = 12) 
plt.ylabel('Self Time', fontsize = 12) 
  
plt.title('Performance', fontsize = 20) 
plt.legend() 
plt.show() 
