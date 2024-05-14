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
def add(a,b):
    res = bin(int(a,2) + int(b,2))[2:].zfill(size)
    if (len(res) > size):
        return res[1:]
    return res
def restoring_div(X,Q,Z, count):
    A = '0'.zfill(size)
    print(A + " " + Q)
    while(count > 0):
        A = A[1:] + Q[0]
        print(A + " " + Q[-n:])
        A = add(A, Z)
        print (A + " " + Q[-n:])
        if A[0] == '0':
            Q = Q[1:] + '1'
            print(A + " " + Q)
        else:
            Q = Q[1:] + '0'
            A = add(A,X)
            print(A + " " + Q)
        count -= 1
        print("\n")
    return Q,A

q = int(input("Enter Dividend:"))
m = int(input("Enter Divisor:"))
bin_q = bin(q)[2:]
bin_m = bin(m)[2:]
n = len(bin_q)
n1 = len(bin_m)
size = max(n,n1) + 1
bin_m = bin_m.zfill(size)
neg_m = two_c(bin_m, size)
Quotient, remainder = restoring_div(bin_m, bin_q, neg_m , n)
print(f"Quotient: {Quotient}, Remainder: {remainder}")