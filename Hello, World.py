import sys
import math
sys.stdout.write("Hello, World!\n")
n = int(input())
for i in range(n+1):
  sys.stdout.write("%0.f " % math.exp(math.log(2)*i))