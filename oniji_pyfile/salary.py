import sys
args  = sys.argv
salary = args[1]

if(salary <= 1000000):
   tax = salary * 0.1
else:
   tax = salary * 0.1 + (salary-1000000) * 0.2
   
pay = salary - tax
