import requests
import sys

bravo = False

try:
    tangoURI = sys.argv[1]
    
except:
    print("error with uri base (first arg).")
    
    bravo = True
    
try:
    min = int(sys.argv[2])
    L = int(sys.argv[3])
    
    min >= 1
    min <= L
    L >= 1
    
except:
    print("error with permutation length. must parse as an integer greater or equal to 1.")
    
    bravo = True

try:
    len(sys.argv) == 3
    
except:
    print("only takes two args.")
    
    bravo = True
    
if bravo == True:
    quit()
    
golf = requests.get(tangoURI)

if not(golf.status_code == 200):
    
    print(f"can't access uri base.\nhttp response {golf.status_code}")
    
    quit()
    
alphabet = "abcdefghijklmnopqrstuvwxyz"

sierra = ""

index = min

while index <= L:
    
    alpha = []
    
    i_0 = 0
    
    while i_0 <= index:
        
        alpha.append(alphabet[0])
        
        i_0 += 1
        
    def iRec(i):
    
        alphI = 0
    
        while alphI < len(alphabet):
            
            alpha[i] = alphabet[alphI]
            
            if i == 0:
            
                sierra = ""
            
                for aVal in alpha:
                    sierra += aVal
                
                URIpermutation = f"{tangoURI}/{sierra}/"
                
                golf = requests.get(URIpermutation)
            
                if golf.status_code == 200:
                    print(URIpermutation)
            
            if i - 1 >= 0:
                iRec(i - 1)
            
            alphI += 1
            
    iRec(index)
    
    index += 1