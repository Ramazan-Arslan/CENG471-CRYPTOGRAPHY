#https://cryptobook.nakov.com/key-exchange/diffie-hellman-key-exchange
#Ramazan Arslan & Berk Önal
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
import sys

if(sys.argv[1] == 'dhke'):
    p = int(sys.argv[3])
    g = int(sys.argv[5])
    a = 4 # random number of Alice

    def isPrime(p):
        for i in range(2, int(p/2)+1):
            if (p % i) == 0:
                print("p =", p ," ( This is not a prime number )")
                print("The program is ending")
                quit();
                
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
        else:
            print("The program is ending")
            quit();


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


else:
    def decimalToBinary(num):
        return "{0:b}".format(int(num))

    def leadingZero(binaryKey):
        if(len(binaryKey) < 8):
            key = ''
            count = 8-len(binaryKey)
            for i in range(count):
                key += '0'
        key += binaryKey 
        return key

    def desEncryption(message,key):
        cipher = DES.new(key, DES.MODE_ECB)
        plaintext = message.encode()
        msg = cipher.encrypt(pad(plaintext, 64))
        return msg

    def desDecryption(cipherText,key):
        decipher = DES.new(key, DES.MODE_ECB)
        de_msg = decipher.decrypt(cipherText)
        return unpad(de_msg, 64).decode()

    message = sys.argv[3];
    key = decimalToBinary(int(sys.argv[5]))
    if(len(key)< 8): 
        key = leadingZero(key).encode()

    encrpytedText = desEncryption(message,key)
    decrpytedText = desDecryption(encrpytedText,key)
    print("Raw ciphertext (Normally this is sent to Alice over a network):\n",encrpytedText)
    print("\nDecrypted plaintext:\n",decrpytedText)

