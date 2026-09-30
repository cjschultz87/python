import sys

mode = sys.argv[1]
filein = sys.argv[2]
fileout = sys.argv[3]
keyfile = sys.argv[4]

try:
    mode == 'e' or mode == 'd'
    
except:
    print("mode e for encryption, mode d for decryption")
    
    quit()
    
try:
    foxtrot_0 = open(filein,"ab")
    
except:
    print("input file invalid")
    
    quit()
    
try:
    foxtrot_1 = open(fileout,"ab")
    
except:
    print("output file invalid")
    
    quit()
    
try:
    kilo = open(keyfile,"ab")
    
except:
    print("key file invalid")
    
    quit()
    
L_f0 = foxtrot_0.tell()

foxtrot_0.close()

foxtrot_0 = open(filein,"rb")

L_f1 = foxtrot_1.tell()

foxtrot_1.close()

if L_f1 > 0:
    overwrite = 'a'
    
    while not(overwrite == 'y' or overwrite == 'n'):
        
        overwrite = input("overwrite file (y/n)?")
        
        if overwrite == 'n':
            quit()
            
foxtrot_1 = open(fileout,"wb")

L_k = kilo.tell()

kilo.close()

kilo = open(keyfile,"rb")

alpha0 = []
alphak = []

index = 0

while index < L_f0:
    alpha0.append(foxtrot_0.read(1)[0])
    index += 1
    
foxtrot_0.close()

index = 0

while index < L_k:
    alphak.append(kilo.read(1)[0])
    index += 1
    
kilo.close()

alphak_prime = []

if mode == 'd':
    alpha0 = alpha0[::-1]

    index = L_f0 - 1

    while index >= 0:
        alphak_prime.append(alphak[index % L_k])
        
        index -= 1
        
alpha1 = []
        
if len(alphak_prime) > 0:
    alphak = []
    
    for k in alphak_prime:
        alphak.append(k)
        
L_k = len(alphak)
L_a1 = len(alpha0)

for i,a0 in enumerate(alpha0):
    sierra = a0
    
    if mode == 'e':
        sierra = a0 ^ alphak[i % L_k]
        
        if i > 0:
            sierra ^= alpha1[i - 1]
        
    elif mode == 'd':
        if i < (L_a1 - 1):
            sierra = a0 ^ alpha0[i + 1]
            
        sierra ^= alphak[i]
    
    alpha1.append(sierra)

if mode == 'd':
    alpha1 = alpha1[::-1]

for a1 in alpha1:
    foxtrot_1.write(a1.to_bytes(1,"big"))

foxtrot_1.close()

print("file write complete.")