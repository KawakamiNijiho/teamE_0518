import sys
from introfamily import IntroFam
args=sys.argv
name=args[1]
age=int(args[2])
cat_name=args[3]
ins=IntroFam(name=name,age=age,cat_name=cat_name)
print(ins.name_out())
print(ins.age_out())
print(ins.cat_out())

