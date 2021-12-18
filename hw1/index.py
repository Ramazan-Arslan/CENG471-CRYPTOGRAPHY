# Ramazan Arslan 250201023
# Berk Önal  260201045
# CENG471 HW1
Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# It collects the key with the index of the character in plaintext and modulates it with 26. 
# In this way, the ciphertext is formed.
def encryptionWithVigenere(plainText,key):
    cipherText = []
    for i in range(len(plainText)):
        cipherCharIndex = (Alphabet.index(plainText[i]) + key[(i % len(key))]) % 26;
        cipherChar = Alphabet[cipherCharIndex];
        cipherText.append(cipherChar)
     
    return("" . join(cipherText))

def decryptionWithVigenere(cipherText,key): 
# It finds the plaintext by subtracting the key from the ciphertext.
    plaintText = []
    for i in range(len(cipherText)):
        plainCharIndex = (Alphabet.index(cipherText[i]) - key[(i % len(key))]) % 26;
        plainChar = Alphabet[plainCharIndex];
        plaintText.append(plainChar)
     
    return("" . join(plaintText))

def findingKeyWithVigenere(plainText,cipherText):
# Repeating pattern are searched by subtracting plaintext from the ciphertext. In this way, key length and key are found.
    tempKeySet = []
    for i in range(len(plainText)):
        charIndex = (Alphabet.index(cipherText[i]) - (Alphabet.index(plainText[i]))) % 26;
        tempKeySet.append(charIndex);
    key=[]
    for i in range(1,len(plainText)):
        if tempKeySet[0] == tempKeySet[i]:
            if i <= len(plainText)/2:
                if tempKeySet[:i] == tempKeySet[i:2*i]:
                    key = tempKeySet[:i]
                    break
            else:
                print(1)
                if tempKeySet[:len(plainText)-i] == tempKeySet[i:len(plainText)]:
                    key = tempKeySet[:i]
                    break
        else:

            key = tempKeySet   
    return key 

def main():
    key = [10,22,14,14,8,10]
    plainText = "WEAREUSINGVIGENEREALGORITHM"
    cipherText = encryptionWithVigenere(plainText.upper(),key)
    print("\nCipher Text:",cipherText)
    plainTextfromCipherText = decryptionWithVigenere(cipherText.upper(),key)
    print("\nPlaint Text:",plainTextfromCipherText)
    foundKey = findingKeyWithVigenere(plainText, cipherText)
    print("\nKey:",foundKey)

if __name__ == "__main__":
    main()