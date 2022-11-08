# Ali.Vigenere
# Vigenère cipher Encryption/Decryption

A brief description of what this project does

Alphabetic text can be encrypted using the Vigenère Cipher. It makes use of a basic type of polyalphabetic substitution.
Using the Vigenère square or Vigenère table, the original text is encrypted.
In this python program you will be able to encrypt/decrypt any message of any length with any alphabetic characters, special characters, and numbers. In addition, it encrypts text in a file and writes its cipher to a file, the key is changed automatically with each new phrase.

Key is generated randomly with each new phrase.

# Instructions for using the code
Encryption

1) Press E(Capital) for Encryption
2) Type the message that you want to encrypt 
3) The message will be printed with a randomly generated key

Decryption

1) Press D(Capital) for Decryption
2) The user will be asked to write the message that they want to decrypt
3) Also the user will will be asked for the key that was used for encryption
4) Finally the decrypted message will be printed

File encryption and Decryption

1) the user must open a file called ‘encrypt.txt’, Then input the message they want to encrypt in that file and save it
2) Run the main code and press F(Capital) for file cipher
3) Then press E(Capital) for file encryption 
4) The encrypted message will open in a file called ‘encryptedfile.txt’, and The key will be saved in a file called ‘Key.txt’

The same applies for file decryption, the user must open a file called 'decrypt.txt' and input the message they want to decrypt, then save it. Run the main code and press F(Capital) for file cipher. Press D(Capital) for file decryption and the user will be asked for the key that was used for encryption. Finally, the decrypted message will open in a file called 'decryptedfile.txt'

# Vigenere table
![image](https://user-images.githubusercontent.com/114480187/200598527-b00b79c0-2d12-4817-9d8f-31d1796ef8d0.png)

![image](https://user-images.githubusercontent.com/114480187/200599202-19fcd385-83ce-4bd1-aace-17eeeb2397aa.png)

For Encryption 
The first letter of the plaintext, G is paired with A, the first letter of the key. So use row G and column A of the Vigenère square, namely G. Similarly, for the second letter of the plaintext, the second letter of the key is used, the letter at row E, and column Y is C, and etc.

For Decryption
is performed by going to the row in the table corresponding to the key, finding the position of the ciphertext letter in this row, and then using the column’s label as the plaintext. For example, in row A (from AYUSH), the ciphertext G appears in column G, which is the first plaintext letter. Next, we go to row Y (from AYUSH), locate the ciphertext C which is found in column E, thus E is the second plaintext letter.
