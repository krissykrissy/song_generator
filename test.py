from time import sleep
import sys
import random
def print_slowly(text):
    for c in text:
        print c,
        sys.stdout.flush()
        sleep(0.8)




def checkHistory():
  lines = []
  with open("history.txt", 'r') as f1:
    for line in f1:
      line = line.rstrip()
      linelist = line.split(',')
            
      lines.append(linelist)
    return lines

def resMethod():
    list1 = [1]
    list2 = [1,2,3,4,5,6,7,8,9,0]
    
    a = random.choice(list2)
    if a in list1:
      print a
      return a
      
    else:
      print a
      a = resMethod()
             
#    while true:
#      random.choice(list1)
#      if l1 in list2:
#        

L = ["a","b","c"]

st = ', '.join(L)

print st
