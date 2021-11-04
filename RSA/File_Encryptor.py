from RSA import *
from tqdm import tqdm

with open("test_file.txt", "r") as f:
    lines = f.readlines()
    for line in tqdm(lines):
        encoded = encryption(line, e, N)
        print(encoded)
        with open("output_file.txt", 'a') as o:
            o.write(encoded)

'''with open("output_file.txt", "r") as f:
    lines = f.readlines()
    for line in tqdm(lines):
        decoded = decryption(line, d, N)
        with open("decrypted_file.txt", 'a') as o:
            o.write(decoded)'''
