import time
import sys
import os

timeout=int(sys.argv[1])
count=0

while count < timeout:
    time.sleep(0.5)
    count=count+1
    left = int(timeout)-count
    print(u"i'm still running, item left: %s" % left)
    
print("i'm done")
print(os.environ)

