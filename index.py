# Ramazan Arslan 250201023
# Berk Onal 
# CENG471 HW1

Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def encryptionWithVigenere(plainText,key):
    cipherText = []
    for i in range(len(plainText)):
        cipherCharIndex = (Alphabet.index(plainText[i]) + key[(i % len(key))]) % 26;
        cipherChar = Alphabet[cipherCharIndex];
        cipherText.append(cipherChar)
     
    return("" . join(cipherText))

def decryptionWithVigenere(cipherText,key): 
    plaintText = []
    for i in range(len(cipherText)):
        plainCharIndex = (Alphabet.index(cipherText[i]) - key[(i % len(key))]) % 26;
        plainChar = Alphabet[plainCharIndex];
        plaintText.append(plainChar)
     
    return("" . join(plaintText))

def findingKeyWithVigenere(plainText,cipherText):
    key = []
    #Bu kısım yapılacak
    return 0 

def main():
    key = [10,22,13]
    plainText = "SELAMCANIM"
    cipherText = encryptionWithVigenere(plainText.upper(),key)
    print(cipherText)
    plainTextfromCipherText = decryptionWithVigenere(cipherText.upper(),key)
    print(plainTextfromCipherText)

if __name__ == "__main__":
    main()