#import math
import re

#Read data from plaintext file and eliminate special characters including whitespaces,lowercase letters and numbers
x = 'plaintext.txt'
with open(x, "r+b") as file:
     message = file.read()
     #file.seek(0)
     #file.write(message.upper())
     #file.close()
uncleanText = open(x).read()
regex = re.compile('[\\\\@_,!.\'\"#$%^&*()<>?/|}{~:]')
if(regex.search(uncleanText) != None):                                #if any of the above characters present in plaintext throw error
    print("Input contains special characters, all the special characters,lowercase letters and white spaces will be eliminated") 
plainText = re.sub('[^A-Z]+', '', uncleanText)                        #substitute every character with space except A-Z
open(x, 'w').write(plainText)
print(f"The plaintext is %s" %plainText)                              #prints the final clean plaintext to console

#function to calculate gcd to check if multiplier and mod are co-primes or not 
def gcd(m,n):
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m

#function to encrypt the plaintext
def encrypt(pt,a,b):
    m = 252526
    if gcd(a,m) != 1:
        print(f"ERROR: The values of multiplier and modulus are not co-primes")
        exit(0)
    final_cipher = ""
    #Divide the input/plaintext into 3 character blocks
    for i in range(0,len(pt),3):
        output = ""                                                   #save converted plaintext(alphabets) to equivalent numbers  
        for j in range(0,3):                                          #characters picked in blocks of 3
            p = (ord(pt[i+j])- ord('A'))                              #Subtract from 65 to start assigning values from 0
            p = str(p).rjust(2,'0')                                   #Append 0 for numbers from 1 to 9
            output = output + str(p)
        #print(output)
        #formula to encrypt the plaintext
        cipher = (a * int(output) + b) % m
        #print(cipher)
        final_cipher = final_cipher + str(cipher).rjust(6,'0') + " "  #appending all the blocks together and ensuring the values are 6 digits
    #print(final_cipher)

    #write the cipher text to ciphertext.txt
    with open("ciphertext.txt", "w") as f:
        f.write(final_cipher)

if __name__ == '__main__':
    a = int(input("Input multiplier for Block Affine cipher: "))
    b = int(input("Input offset for Block Affine cipher: "))
    if b > 252526:
        print(f"ERROR: Offest entered not in range")
        exit(0)
    y = encrypt(plainText,a,b)
    print("The ciphertext is written to ciphertext.txt file!")
