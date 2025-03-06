import random # For random fun fact

# This is a Enigma Machine

# Create a Encrypt Function

# Create a Decrypt Function


# Create a Atbash Fun Fact Function
def fun_fact():
    facts = [
        "The Atbash cipher, is a simple monoalphabetic substitution cipher originally used to encrypt the Hebrew alphabet.",
        "It works by substituting each letter from one end with its corresponding letter on the other.",
        "In English, A becomes Z, B becomes Y, and so on.",
        "The Atbash cipher is sometimes called the mirror code!"
    ]
    print(random.choice(facts))
# Create a list for encrypt
encrypt = []

# Create a list for decrypt
decrypt = []

# Greet the user
print("Welcome to the Enigma Machine on Python! Today's cipher language is Atbash!")
name = input("What is your name?")
print(f"Hello {name}, I hope you have a blast!")

# Ask the user if they would like to encrypt or decrypt a message
while True:
    try:
        user_q = input("Would you like to encrypt or decrypt a message?")
    except:
        if not "yes" or "no":
            print("Please select either yes or no.")
    

# When user selects if they would like to encrypt or decrypt then ask them to type in their message


# Present the user with their message encrypted or decrypted


# Give them a menu to choose from, either encrypt/decrypt a message(restart), give a random fun fact about Atbash, or exit