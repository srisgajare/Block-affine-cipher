# BLOCK AFFINE CIPHER

## HOW THE CODE WORKS

### ENCRYPT CODE

1. The encrypt code reads data from plaintext.txt file eliminates all characters(lowercase,numbers,special characters) 
except upper case letters for simplicity.
2. Ensure the given input is in the multiples of 3, if not pad with Bs(or any alphabet).
3. The code converts the alphabets to equivalent numbers(ASCII values) & encrypts the data(3 blocks/letters at a time) 
and stores in ciphertext.txt file.
4. User needs to input multiplier and offset, and need to make sure the multiplier and mod are co primes else the program 
will throw error and terminate.

### DECRYPT CODE

1. The decrypt code reads the ciphertext from ciphertext.txt file decrypt the data and writes the plaintext to 
finalplaintextoutput file.
2. User needs to input multiplier and offset, and should ensure both the input values are same as the ones used for 
encrypt.py program.
