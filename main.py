import random # For random fun fact

# This is a Enigma Machine

#Create a Encrypt Function
def encrypt_func(encrypt: list):
    while True:
        encrypt_ans = input("Please type in the words you would like to encrypt!")
    


# Create a Decrypt Function
def decrypt_func(decrypt: list):
    while True:
        decrypt_ans = input("Please type in the words you like to decrypt!")
    


# Create a Atbash Fun Fact Function
def fun_fact():
    facts = [
        "The Atbash cipher, is a simple monoalphabetic substitution cipher originally used to encrypt the Hebrew alphabet.",
        "It works by substituting each letter from one end with its corresponding letter on the other.",
        "In English, A becomes Z, B becomes Y, and so on.",
        "The Atbash cipher is sometimes called the mirror code!"
    ]
    print(random.choice(facts))

# Create a View History Function
def previous_his(encrypt_list: list, decrypt_list: list):
    print("\nHere are your past encryptions and decryptions!")
    if decrypt_list:
        for text in decrypt_list:
            print(text)
    else: 
        print("There is no previous or current decryptions..")


# Create a list for encrypt
encrypt_list = []

# Create a list for decrypt
decrypt_list = []

# Greet the user
print("Welcome to the Enigma Machine on Python! Today's cipher language is Atbash!")
name = input("What is your name?")
print(f"Hello {name}, I hope you have a blast!")

# Ask the user if they would like to encrypt or decrypt a message
while True:
    user_q = input("Would you like to either encrypt or decrypt a message? Type encrypt or decrypt!")

    if user_q == "encrypt":
        encrypt_func(encrypt_list)
    elif user_q == "decrypt":
        decrypt_func(decrypt_list)
    else:
        print("Type the words encrypt or decrypt only.")
        continue

# Present the user with their message encrypted or decrypted


# Give them a menu to choose from, either encrypt/decrypt a message(restart), give a random fun fact about Atbash, or exit
while True:
    print("\nHere are your new choices if you would like to have some fun! (1) Decrypt or Encrypt a message again, (2) Get a fun fact about Atbash, or (3) Exit the Program!")
    choice = input("Please select your next option...").strip()