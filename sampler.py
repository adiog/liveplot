import math
from time import sleep
import sys
x=0
while True:
  print(math.sin(x))
  sys.stdout.flush()
  x+=0.1
  sleep(0.05)

