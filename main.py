import random # For random fun fact

# This is a Enigma Machine

#Create a Encrypt Function
def encrypt_func(encrypt_list: list):
    encrypt_dict = {
        "A":"Z", "B":"Y", "C":"X", "D":"W", "E":"V", "F":"U", "G":"T", "H":"S",
        "I":"R", "J":"Q", "K":"P", "L":"O", "M":"N", "N":"M", "O":"L", "P":"K",
        "Q":"J", "R":"I", "S":"H", "T":"G", "U":"F", "V":"E", "W":"D", "X":"C", 
        "Y":"B", "Z":"A",
        "a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s",
        "i":"r", "j":"q", "k":"p", "l":"o", "m":"n", "n":"m", "o":"l", "p":"k",
        "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", 
        "y":"b", "z":"a",
        
    }
    encrypt_ans = input("Please type in the words you would like to encrypt.")
    encrypt_message = ""
    for letter in encrypt_ans:
        encrypt_message += encrypt_dict.get(letter) # .get means to return 
    encrypt_list.append(encrypt_message)
    print(f"{encrypt_message}")

# Create a Decrypt Function
def decrypt_func(decrypt_list: list):
    decrypt_dict = {
        "Z":"A", "Y":"B", "X":"C", "W":"D", "V":"E", "U":"F", "T":"G", "S":"H",
        "R":"I", "Q":"J", "P":"K", "O":"L", "N":"M", "M":"N", "L":"O", "K":"P",
        "J":"Q", "I":"R", "H":"S", "G":"T", "F":"U", "E":"V", "D":"W", "C":"X",
        "B":"Y", "A":"Z",
        "z":"a", "y":"b", "x":"c", "w":"d", "v":"e", "u":"f", "t":"g", "s":"h",
        "r":"i", "q":"j", "p":"k", "o":"l", "n":"m", "m":"n", "l":"o", "k":"p",
        "j":"q", "i":"r", "h":"s", "g":"t", "f":"u", "e":"v", "d":"w", "c":"x",
        "b":"y", "a":"z",
    }
    decrypt_ans = input("Please type in the words about what you would like to decrypt!")
    decrypt_text = ""
    for letter in decrypt_ans:
        decrypt_text += decrypt_dict.get(letter)
    decrypt_list.append(decrypt_text)
    print(f"{decrypt_text}")

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
    if encrypt_list:
        for message in encrypt_list:
            print(message) # keep it different so I would know, but ask Mr.Kung if it will mess up game!
    else:
        print("There are no past or current encryptions!")

# Create a list for encrypt
encrypt_list = []

# Create a list for decrypt
decrypt_list = []


# Greet the user
print("Welcome to the Enigma Machine on Python! Today's cipher language is Atbash!")
name = input("What is your name?")
print(f"Hello {name}, I hope you have a blast!")
print(f"(also {name} make sure you get yourself a meal from mcdonalds)")

# Ask the user if they would like to encrypt or decrypt a message
while True:
    user_q = input("Would you like to either encrypt or decrypt a message? Type encrypt or decrypt!").strip()
    if user_q == "encrypt":
        encrypt_func(encrypt_list)
    elif user_q == "decrypt":
        decrypt_func(decrypt_list)
    else:
        print("Type the words encrypt or decrypt only.")
        continue


# Give them a menu to choose from, either encrypt/decrypt a message(restart), give a random fun fact about Atbash, or exit 
    while True:
        print("\nHeyy, here are your following options! (1) Encrypt another message, (2) Decrypt another message, (3) View your history, (4) Fun fact about Atbash and (5) Exit!")
        final = input("Please select from one of the four options above!").strip()

        if final == "1":
           encrypt_func(encrypt_list)
        elif final == "2":
            decrypt_func(decrypt_list)
        elif final == "3":
            previous_his(encrypt_list, decrypt_list)
        elif final == "4":
            fun_fact()