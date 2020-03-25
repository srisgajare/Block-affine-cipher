#import math

#function to calculate gcd to check if multiplier and mod are co-primes or not 
def gcd(m,n):
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m

#function to compute multiplicative inverse of multiplier
def multiplicative_inverse(multiplier,mod):
    x = 0
    old_x = 1
    y = 1
    old_y = 0
    while mod != 0:
        temp = mod
        quotient = multiplier // mod
        mod = multiplier % mod
        multiplier = temp
        temp = x
        x = old_x - quotient * x
        old_x = temp
        temp = y
        y = old_y - quotient * y
        old_y = temp
    return old_x % 252526  #return positive inverse value

#Read the cipher text from the file   
with open("ciphertext.txt", "r") as f:
    cipherText = f.read()
    #print(cipherText)

#Decrypt function to decrypt the ciphertext read from file 
def decrypt(cipherText,inverse,b):
    final_decrypted_output = ""
    for i in range(0,len(cipherText), 7):                                          #picking 6 numbers including space to decrypt every block
        decrypt = str((inverse * (int(cipherText[i:i+6]) - b)) % m).rjust(6,'0')   #formula to decrypt 
        #print(decrypt)
        for j in range(0,6,2):                                                     #each block has 6 digits where 2 digits represent number corresponding to a letter  
            character = chr(int(decrypt[j:j+2]) + ord('A'))                        #add 65 to determine the ascii value obtained and hence the character
            final_decrypted_output += character 
    print(f"The decrypted message is %s" %final_decrypted_output)

    #Write the decrypted message to outputfile
    with open("finalplaintextoutput.txt", "w") as f:
        f.write(final_decrypted_output)


if __name__ == '__main__':
    m = 252526
    a = int(input("Input multiplier for Block Affine cipher, this should be same as the one used for encryption: "))
    b = int(input("Input offset for Block Affine cipher, this should be same as the one used for encryption: "))
    if b > m:
        print(f"ERROR:Offest entered not in range")
        exit(0)
    if gcd(a,m) != 1:
        print(f"ERROR: The values of multiplier and modulus are not co-primes")
        exit(0)
    else:
        mod_inverse = multiplicative_inverse(a,m)
    #print(mod_inverse)
    y = decrypt(cipherText,mod_inverse,b)
    print("The output is written to finalplaintextoutput.txt file!")
