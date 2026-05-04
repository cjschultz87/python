import sys

###############################

def factorial(n):
    
    index = 1
    foxtrot = 1
    
    while index <= n:
        foxtrot *= index
        index += 1
        
    return foxtrot

###############################
    
def atos(alpha):
    sierra = ""
    
    for a in alpha:
        sierra += a
        
    return sierra

###############################

def commute(alpha, index_0, index_1):
    alpha_prime = []
    
    for a in alpha:
        alpha_prime.append(a)

    a = alpha_prime[index_1]
    
    alpha_prime[index_1] = alpha_prime[index_0]
    alpha_prime[index_0] = a
    
    return alpha_prime

###############################

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

N = 0
N_list = 0

###############################

try:
    N = int(sys.argv[1])
    
    (N <= len(alphabet)) == True

except:
    print("couldn't parse word length (first arg) as integer value less than or equal to the alphabet length.")
    
    quit

###############################
    
try:
    N_list = int(sys.argv[2])
    
    (N_list <= factorial(N)) == True
    
except:
    print("couldn't parse the list length (second arg) as an integer less than or equal to the factorial of the word length (first arg).")
    
    quit

###############################
    
word = []

for a in alphabet[0:N]:
    word.append(a)
   

factorial_explanation = """    
abc ident d (0,1,2) d = 3
cab (ident d) + 5 (2,0,1)

<0,1,2> -> <2,0,1>
(0,2),(1,0),(2,1)
rotate right 1

dab (ident c) (0,1,2)   c = 2
bda (ident c) + 5 (2,0,1)

cda (ident b) (0,1,2)   b = 1
acd (ident b) + 5 (2,0,1)

bcd (ident a) (0,1,2)   a = 0
dbc (ident a) + 5 (2,0,1)


0 abc ident d d = 3           (0,1,2)
1 bac <1,0,2> (0,1),(1,0),(2,2)
2 cba <2,1,0> (0,2),(1,1),(2,0)
3 bca <1,2,0> (0,1),(1,0),(2,2)
4 acb <0,2,1> (0,2),(1,1),(2,0)
5 cab <2,0,1>                   (2,0,1)

1 bac <1,0,2> (0,1),(1,0),(2,2)
2 cba <2,0,1> (0,2),(1,0),(2,1)
3 bca <1,0,2> (0,1),(1,0),(2,2)
4 acb <2,1,0> (0,2),(1,1),(2,0)
5 cab <1,0,2> (0,1),(1,0),(2,2)

bac, cba, bca, acb, cab
102, 201, 102, 210, 102

bac, bca, cba, acb, cab
102, 021, 102, 201, 102

bac, acb, cba, bca, cab
102, 120, 120, 102, 120

bac, cba, acb, bca, cab
102, 201, 201, 210, 120

bac, bca, acb, cba, cab
102, 021, 210, 120, 021

bac, acb, bca, cba, cab
102, 120, 210, 102, 021



dab ident c c = 2 <3,1,2,0> (0,3),(1,1),(2,2),(3,0)
bda (ident c) + 5

cda ident b
acd (ident b) + 5

bcd ident a
dbc (ident a) + 5

factorials
!0 = 1
!1 = 1
!2 = 2
!3 = 6

for length n commute positions (0,n-1) n - 1 times.

0,1,2,1,2,1,
3,1,2,1,2,1,
3,1,2,1,2,1,
3,1,2,1,2,1
"""

alpha_iota = []

index = 0

while index < factorial(N) - 1 and index < N_list - 1:
    alpha_iota.append(0)
    
    index += 1

index = 0
index_1 = 0

a = 1

while a < N:
        if index > len(alpha_iota):
            break
            
        alpha_iota[index] = a
        
        index += factorial(a)
        
        index_1 += 1
        
        if index >= len(alpha_iota):
            a += 1
            index = factorial(a) - 1
            index_1 = 0    

sierra = atos(word)

sierra_alpha = []

sierra_alpha.append(word)

index = 1

while index <= len(alpha_iota):
    alpha = sierra_alpha[index - factorial(alpha_iota[index - 1] - 1)]
    
    c_alpha = commute(alpha, 0, alpha_iota[index - 1])
    
    sierra_alpha.append(c_alpha)
    
    sierra += atos(sierra_alpha[index])
    
    index += 1
    
print(sierra)
