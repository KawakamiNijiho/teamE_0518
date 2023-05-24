import sys
from introduce import Intro
args=sys.argv
name=args[1]
age=int(args[2])
ins=Intro(name=name,age=age)
ins.name_out()
ins.age_out()
