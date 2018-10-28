#!usr/bin/python3
#! -*- coding: utf-8 -*-

from Crypto.Cipher import *
import base64,random,os,hashlib,time

#####################################################################################################
# Hir I made diffrent Encode and decodde logarthme So if you want to dev just add  new logarthme    #
#####################################################################################################

#Thanks for Net-Centric Computing Assignment for they free RSA python code

###################################################################################################
############################# This For help   #####################################################
###################################################################################################

def random_line(dir):
    lines = open(dir).read().splitlines()
    myline = random.choice(lines)
    return myline



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


'''
Tests to see if a number is prime.
'''


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return str(cipher)


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return str(''.join(plain))



######################################################################################################################
###########################################       Encoding          ##################################################
######################################################################################################################

def encodeAES(key,dir):
    if '.cry' not in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()
        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        BLOCK_SIZE = 32
        PADDING = '{'
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        secret = hashlib.md5(str(key).encode('utf-8')).hexdigest()
        cipher = AES.new(secret)
        encoded = EncodeAES(cipher, think)
        ###########################################################################
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

def encodeRSA(privateKey,dir):
    if '.cry' not in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print("encoding data of the file [It will take Some time] ...")
        ########################################################################
        encoded = encrypt(privateKey,think)
        ###########################################################################
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")



def encodeXOR(key, dir):
    if '.cry' not in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        secret = hashlib.md5(key).hexdigest()
        cipher = XOR.new(secret)
        encoded = base64.b64encode(cipher.encrypt(think))
        ###########################################################################
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

def encodeBASE64(dir):
    if '.cry' not in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        os.system('clear')
        ########################################################################
        encoded = base64.b64encode(think)
        ###########################################################################
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

def encodeBASE32(dir):
    if '.cry' not in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        encoded = base64.b32encode(think)
        ###########################################################################
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

def encodeBASE16(dir):
    if '.cry' not in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print("encoding data of the file ...")
        time.sleep(3)
        ########################################################################
        encoded = base64.b16encode(think)
        ###########################################################################
        time.sleep(3)
        print('writing in you file ...')
        os.remove(dir)
        newfile = open(dir + '.cry',"w")
        newfile.write(encoded)
        newfile.close()
    else:
        print("The File is already encrypt")

######################################################################################################################
###########################################       Decoding          ##################################################
######################################################################################################################


def decodeAES(key,dir):
    if '.cry' in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        PADDING = '{'
        DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
        secret = hashlib.md5(str(key).encode('utf-8')).hexdigest()
        print(secret)
        print(len(secret))
        cipher = AES.new(secret)
        decoded = DecodeAES(cipher, think)
        ###########################################################################
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decodeXOR(key,dir):
    if '.cry' in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        secret = hashlib.md5(key).hexdigest()
        cipher = XOR.new(secret)
        decoded = cipher.decrypt(base64.b64decode(think))
        ###########################################################################
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decodeBASE64(dir):
    if '.cry' in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        decoded = base64.b64decode(think)
        ###########################################################################
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decodeBASE32(dir):
    if '.cry' in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        decoded = base64.b32decode(think)
        ###########################################################################
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")

def decodeBASE16(dir):
    if '.cry' in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()

        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        decoded = base64.b16decode(think)
        ###########################################################################
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")



def decodeRSA(privatkey,dir):
    if '.cry' in dir:
        files = open(dir,"r")
        think = files.read()
        files.close()
        think = float(think)

        os.system('clear')
        print('Decoding your data File....')
        ############################################################################
        decoded = decrypt(privatkey,think)
        decoded =''.join(map(lambda x: str(x), encrypted_msg))
        ###########################################################################
        name = dir.replace('.cry',"")
        os.remove(dir)
        print('writing in to your file...')
        newfile = open(name,"w")
        newfile.write(decoded)
        newfile.close()
    else:
        print("The File is not encrypt to Decrypt")
