import hashlib
import random
import string
import time
import getpass
import pickle

def decode_recipy(name):
    with open('ingredients.pkl', 'rb') as file:
            data = pickle.load(file)
    with open(f'{name}_decoded_recipy.txt', 'w') as file:
        for i in range(10):
            print(random.choice(data), file=file)

def verify_password(pw:str, name:str):
    for i in range(100):
        print("".join([random.choice(string.ascii_letters) for x in range(100)]))
        time.sleep(0.05)
    if hashlib.sha256(pw.encode()).hexdigest() == "6d38e25e92b8ffd4b1649162f2cc7cb49ce6504e98321bcfa96b4744d7aa6274":
        print("Correct password")
        decode_recipy(name)
    else:
        print("INCORECT PASSWORD]")

def main():
    name = input("Provide your name:")
    pw = getpass.getpass("Provide password:")
    verify_password(pw, name)


if __name__ == "__main__":
    main()
