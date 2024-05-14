def two_c(x,size):
    l1 = list(x)
    for i in range(len(l1)):
        if l1[i] == '0':
            l1[i] = '1'
        else:
            l1[i] = '0'
    y = "".join(l1)
    res = bin(int(y,2) + 1)
    return res[2:].zfill(size)

def ASR(X,Y,Z):
    a = X[0]
    for i in range(1,len(X)):
        a = a + X[i-1]
    b = X[-1]
    for j in range(1, len(Y)):
        b = b + Y[j-1]
    c = Y[-1]
    return a,b,c

def add(A,B):
    res = bin(int(A,2) + int(B,2))[2:].zfill(size)
    if (len(res) > size):
        return res[1:]
    return res
def booths(M, Q , neg , count):
    A = ""+'0'.zfill(n+1)
    Q1 = '0'
    print(A + " " + Q + " " + Q1)
    while(count>0):  
        test = Q[-1] + Q1
        if(test == '00' or test == '11'):
            A,Q,Q1 = ASR(A,Q,Q1)
            print(A + " " + Q + " " + Q1)
        elif(test == '01'):
            A = add(A,M)
            A,Q,Q1 = ASR(A,Q,Q1)
            print(A + " " + Q + " " + Q1)
        elif(test == '10'):
            A = add(A,neg)
            A,Q,Q1 = ASR(A,Q,Q1)
            print(A + " " + Q + " " + Q1)
        count -= 1


m = int(input("Enter the multiplicand:"))
q = int(input("Enter the multiplier:"))

bin_M = bin(abs(m))[2:]
n = len(bin_M)
bin_Q = bin(abs(q))[2:]
n1 = len(bin_Q)
size = max(n,n1) + 1
bin_M = bin_M.zfill(size)
bin_Q = bin_Q.zfill(size)
neg_M = two_c(bin_M, size)
neg_Q = two_c(bin_Q , size)

if (m < 0) & (q > 0):
    booths(neg_M, bin_Q , bin_M , size)
elif (m > 0) & (q < 0):
    booths(bin_M, neg_Q , neg_M , size)
elif (m < 0) & (q < 0):
    booths(neg_M, neg_Q , bin_M, size)
else:
    booths(bin_M, bin_Q , neg_M , size)