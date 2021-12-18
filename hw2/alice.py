#https://cryptobook.nakov.com/key-exchange/diffie-hellman-key-exchange
#Ramazan Arslan & Berk Önal

p = 23
g = 5
a = 4 # random number of Alice

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


def secretKeyAlice(B,a,p):
    return B**a % p 
    
isPrime(p)
isPrimitiveNumber(p,g)
A = (g**a) % p # This can be sent to Bob
B = 10 # This is coming from Bob
print("Alice and Bob publicly agree on the values of p and g. \nHowever, it is advised to use any pair of p and g only once.")
print("a = ",a," (This must be kept secret.)")
print("A = ",A," (This can be sent to Bob.)")
#Finalization of the key exchange
print("s = ",secretKeyAlice(B,a,p),"\n(This must be kept secret. However, Bob should be able to calculate this as well.)")

