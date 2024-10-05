import time,sys

def print_star ():
    indent = 0
    estars = "******"
    while indent < 5:
        print(" "*indent+estars)
        time.sleep(0.5)
        indent +=1
    else: 
        while indent != - 1:
            print(" "*indent+estars)
            time.sleep(1)
            indent -=1

try:
 print_star()
except KeyboardInterrupt:
   print("dont intetrupt idiot")
   time.sleep(2)
   sys.exit()