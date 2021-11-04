import math
from tqdm import tqdm
import time

mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
           "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
           "x": 24, "y": 25, "z": 26, " ": 27, ".": 28, ",": 29, "[": 30, "]": 31, "(": 32, ")": 33, "{": 34,
           "}": 35, ":": 36, "=": 37, "_": 38, '"': 39, "'": 40, "8": 41, "\n": 42, "A": 43, "B": 44, "C": 45,
           "D": 46, "E": 47, "F": 48, "G": 49, 'H': 50, "I": 51, "J": 52, "K": 53, "L": 54, "M": 55, "N": 56,
           "O": 57, "P": 58, "Q": 59, "R": 60, 'S': 61, "T": 62, "U": 63, "V": 64, "W": 65, "X": 66, "Y": 67,
           "Z": 68, "!": 69, "?": 70, "1": 71, "2": 72, '3': 73, "4": 74, "5": 75, "6": 76, "7": 77, "9": 78,
           "0": 79, "-": 80, ";": 81, "<": 82, ">": 83, "*": 84, "\\": 85}

rev_mapping = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
               13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
               24: 'x', 25: 'y', 26: 'z', 27: ' ', 28: '.', 29: ',', 30: '[', 31: ']', 32: '(', 33: ')', 34: '{',
               35: '}', 36: ':', 37: '=', 38: '_', 39: '"', 40: "'", 41: '8', 42: "\n", 43: 'A', 44: 'B', 45: 'C',
               46: 'D', 47: 'E', 48: 'F', 49: 'G', 50: 'H', 51: 'I', 52: 'J', 53: 'K', 54: 'L', 55: 'M', 56: 'N',
               57: 'O', 58: 'P', 59: 'Q', 60: 'R', 61: 'S', 62: 'T', 63: 'U', 64: 'V', 65: 'W', 66: 'X',  67: 'Y',
               68: 'Z', 69: '!', 70: '?', 71: '1', 72: '2', 73: '3', 74: '4', 75: '5', 76: '6', 77: '7', 78: '9',
               79: '0', 80: "-", 81: ";", 82: "<", 83: ">", 84: "*", 85: "\\"}


def encryption(text, encrypt_key, public):
    sent = []
    cypher_text = []
    for letter in text:
        sent.append(mapping[letter])
    for each in tqdm(sent): #tqdm(sent)
        calc = (each ** encrypt_key) % public
        cypher_text.append(str(calc))
        print(cypher_text)
    cypher_text = ':'.join(cypher_text)
    return cypher_text


def decryption(cypher_text, decrypt_key, public):
    plain_text = []
    num = []
    for digit in cypher_text.split(':'):
        num.append(int(digit))
    for each in tqdm(num):  #tqdm(num)
        calc = (each ** decrypt_key) % public
        plain_text.append(rev_mapping[calc])
        print(plain_text)
    plain_text = ''.join(plain_text)
    return plain_text


def get_N(p, q):
    N = p*q
    phi_N = (p-1)*(q-1)
    return N, phi_N


def generate_encrypt(phi_N):
    for i in range(2, phi_N):
        if math.gcd(i, phi_N) == 1:
            return i


def generate_decrypt(e, phi_N):
    i = 1
    while True:
        if (i*e) % phi_N == 1:
            return i
        else:
            i += 1


N, phi_N = get_N(89, 97)     #853, 1187
e = generate_encrypt(phi_N)
d = generate_decrypt(e, phi_N)


print("="*100)
while True:
    option = input("Input option[encrypt(1), decrypt(2)]: ")
    if option == '1':
        userinput = input("Input text to be encrypted: ")
        encrypted = encryption(userinput, e, N)
        print(f"Encryption key:({e}, {N})")
        print(f"Encrypted text:{encrypted}")
        print("=" * 100)

    elif option == '2':
        userinput = input("Input text to be decrypted: ")
        decrypted = decryption(userinput, d, N)
        print(f"Decryption key:({d}, {N})")
        print(f"Decrypted test:{decrypted}")
        print("=" * 100)
    else:
        print("Please choose the option above.")