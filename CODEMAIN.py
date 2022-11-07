from ast import If
import string
import random
from pathlib import Path

#I assigned a variable called alpha which makes a list that allows the algorithm to encrypt/decrypt
#a phrase of any length containing alphabet characters, digits, and special characters.
alpha = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits + ' ') + ["\n",]

#I did two dictionaries that maps alpha to index and index to alpha.
#What the zip function does, is for example in the alphabet takes the first letter which is ‘a’
#mapping it to the first of the range of Len of the alphabet which is 0, ‘b’ gets to 1, etc.
alphaindex = dict(zip(alpha, range(len(alpha))))
indexalpha = dict(zip(range(len(alpha)), alpha))

#I defined encrypt to take two parameters which are the message that the user will enter and the key
#I used a function called splt which splits the message to the length of the key
#A for loop that starts at 0 and continues to the end of the user message,
# also it has a jump of the length of the key.
#I converted the message to an index and added the key, as it is encryption.
#The variable called num converts alpha to an index of the current letter and alpha to an index of our key
#modulus Len of alpha.
def encrypt(usermessage, key):
        encryptedtxt = ""
        splt = [usermessage[i : i + len(key)] 
            for i in range(0, len(usermessage), len(key))]
        for insplt in splt:
            i = 0
            for letter in insplt:
                num = (alphaindex[letter] + alphaindex[key[i]]) % len(alpha)
                encryptedtxt += indexalpha[num]
                i += 1
        return encryptedtxt

#I defined decrypt containing two parameters which are encrypted text and the key. 
#The same steps for encryption apply to decryption except the key is subtracted.
def decrypt(encrypted, key):
        decrypted = ""
        encryptedsplt = [encrypted[i : i + len(key)] 
            for i in range(0, len(encrypted), len((key)))]
        for insplitdec in encryptedsplt:
            i = 0
            for letter in insplitdec:
                number = (alphaindex[letter] - alphaindex[key[i]]) % len(alpha) 
                decrypted += indexalpha[number]
                i += 1
        return decrypted

#A variable called S which allows the user to input E for encryption D for decryption or F for file cipher. 
S = input("Write E for encrypt or D for decryption or F for file cipher - ")

#If the user inputs E he will enter a message
#a key with a mix of digits, special characters, and alphabets is generated randomly
#With each message the user inputs. .Join joins characters and the key takes 5 digits. 
if S == "E":
    E = input("message - ")
    randomkey = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=5))
    print("key - " + randomkey)
    cipher = encrypt(E, randomkey)
    print("encrypted message - " + cipher)
if S == "D":
    E = input("message - ")
    keyintake = input("key - " )
    cipher = decrypt(E, keyintake)
    print("decrypted message - " + cipher)


#file

if S == "F":
    fileaction = input("E for encryption or D for decryption - ")
    if fileaction == "E":
        #openfile = open('encrypt.txt', 'r')
        #readfile = openfile.readlines()
        readfile = Path('encrypt.txt').read_text()
        filekey =''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=5))
        filencrypt = encrypt(readfile, filekey)
        keydocument = open('Key.txt', 'w')
        keydocument.write(filekey)
        opendocument = open('encryptedfile.txt', 'w+')
        opendocument.write(filencrypt)
        print("Key - " + filekey)
        print("File Encryption Complete")
    
    if fileaction == "D":
        #openfile = open('decrypt.txt', 'r')
        #readfile = openfile.readline()
        readfile = Path('decrypt.txt').read_text()
        keyinput = input("enter key - ")
        filedecrypt = decrypt(readfile, keyinput)
        opendocument = open('decryptedfile.txt', 'w+')
        opendocument.write(filedecrypt)
        print("File Decryption Complete")


#Complete