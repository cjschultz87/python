import sys
import random

try:
    foxtrot = open(sys.argv[1],"wb")

except:
    print("output path error.")
    
    quit()
    
try:
    L = int(sys.argv[2])

except:
    print("file size error.")
    
    quit()
    
index = 0

while index < L:
    
    if index > 0:
        print("\033[2A")
        
    a = int(random.random() * 256)
    
    percentage = int(100 * float(index)/float(L))
    
    print(f"{a},{percentage}%")
    
    a = a.to_bytes(1,"big")
    
    foxtrot.seek(index,0)
    
    foxtrot.write(a)
    
    index += 1
    
print(f"100%")
    
foxtrot.close()