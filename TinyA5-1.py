from ast import While
import math

def to4bitBin(P):
	scale = 16 ## equals to hexadecimal
	num_of_bits = 4
	return bin(int(P, scale))[2:].zfill(num_of_bits)

def maj(x1,y3,z3):
    m=x1
    if( x1 == y3 or x1 == z3):
        return m
    if( x1 != y3 and y3 == z3):
        return y3
    return m

def Turn(list):
    r = []

    if (len(list) == 6):
        r.append( int(list[2]) ^ int(list[4]) ^ int(list[5]) ) 

    if (len(list) == 8):
        r.append(int(list[6]) ^ int(list[7]))

    if (len(list) == 9):
        r.append(int(list[2]) ^ int(list[7]) ^ int(list[8]))

    for x in range(len(list)-1):
        r.append(list[x])
    return r

    

PlainText = input('enter a plain text (in Hexadecimal):\n')
P_encoded = list(to4bitBin(PlainText))

Key = input('enter K key (23 bit):\n')
while len(Key)<23 or len(Key)>23:
    print("Key Error! Please enter again!")
    Key = input('enter K key (23 bit):\n')

x = [int(i) for i in list(Key[:6])]
y = [int(i) for i in list(Key[6:14])]
z = [int(i) for i in list(Key[14:23])]



S = []
C = [c for c in range(len(P_encoded))]
for i in range(len(P_encoded)):
    m = maj(x[1],y[3],z[3])
    print("maj() = ",m)
    if (x[1] == m):
        x = Turn(x)

    if (y[3] == m):
        y = Turn(y)

    if (z[3] == m):
        z = Turn(z)
    

    print("X = ",x)
    print("Y = ",y)
    print("Z = ",z)
    print("\n")
    S.append( int(x[5]) ^ int(y[7]) ^ int(z[8]))



print("\nPlain Text Encoded: ",P_encoded)
print("S = ",S)

for i in range(len(P_encoded)):
    C[i] = S[i] ^ int(P_encoded[i])

print("Cypher Text = ",C)

input('Press ENTER to exit')