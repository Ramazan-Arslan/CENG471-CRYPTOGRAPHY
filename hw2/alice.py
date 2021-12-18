#https://cryptobook.nakov.com/key-exchange/diffie-hellman-key-exchange
#Ramazan Arslan & Berk Önal
p = 23
g = 5
a = 4 # random number of Alice
b = 3 # random number of Bob

def isPrime(p):
    for i in range(2, int(p/2)+1):
        if (p % i) == 0:
            print("p =", p ," ( This is not a prime number )")
            break
    else:
        print("p = ", p , "OK ( This is a prime number )")


def isPrimitiveNumber(g,p):
    results = []
    for i in range(1,int(p)):
        check = pow(int(g), i) % int(p)
        if check in results:
            print("g = " ,g, "( This is not a primitive root of modulo",p,")")
            isPrimitive = False
            break
        else:
            isPrimitive = True
        results.append(check)
    if isPrimitive:
        print("g = " ,g, "OK ( This is a primitive root of modulo",p,")")


def secretKeyBob(A,b,p):
    return A**b % p 

def secretKeyAlice(B,a,p):
    return B**a % p 
    
isPrime(p)
isPrimitiveNumber(p,g)
A = (g**a) % p # This can be sent to Bob
B = (g**b) % p # This can be sent to Alice
s = g**(a*b) % p # secret key

print(A)
print(B)
print(s)
print(secretKeyAlice(B,a,p))
print(secretKeyBob(A,b,p))
