#https://cryptobook.nakov.com/key-exchange/diffie-hellman-key-exchange
#Ramazan Arslan & Berk Önal
p = 23
g = 5
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
B = (g**b) % p # This can be sent to Alice
A = 4 # This is coming from Alice
print("Alice and Bob publicly agree on the values of p and g. \nHowever, it is advised to use any pair of p and g only once.")
print("b = ",b," (This must be kept secret.)")
print("B = ",B," (This can be sent to Alice.)")
#Finalization of the key exchange
print("s = ",secretKeyBob(A,b,p),"\n(This must be kept secret. However, Alice should be able to calculate this as well.)")
