
from loops.secret import password
import time

numbers = ['0','1','2','3','4','5','6','7','8','9','1']

for x in numbers: # 1
    for y in numbers: # 0
        for a in numbers:
            for m in numbers:
                time.sleep(0)
                print('attempting ' + x+y+m+a)
                if x+y+m+a == password:
                    print('CRACKED! Password is ' + x+y+m+a)
                    quit()
                
# 0,0
# 0,1
    










