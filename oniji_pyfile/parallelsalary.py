import sys
args = sys.argv

from func_salary import calcsalary

for i in range(len(args)):
    if i == 0:
        continue
    calcsalary(int(args[i])) 


