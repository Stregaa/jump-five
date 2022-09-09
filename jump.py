# Jump-5 Cypher Encrypter/Decrypter

jump_key = {
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0",
    "6": "4",
    "7": "3",
    "8": "2",
    "9": "1"
}

def welcome():
    # Asks user for input regarding encrypting or decrypting
    print("Welcome to the Jump-Five Cypher Encrypter/Decrypter.")
    try:
        choice = int(input("Would you like to encrypt[1] or decrypt[2] some numbers?: "))
        if choice == 1 or choice == 2:
            return choice
        else:
            print("Input must be 1 or 2.")
            quit()
    except ValueError:
        print("Input must be 1 or 2.")
        quit()

def decrypt(task):
    # Asks user for numbers, then decrypts/encrypts them
    encrypted = ""
    
    if task == 1:
        numbers = str(input("Please enter the numbers you would like to encrypt with Jump-Five: "))
        for num in numbers:
            encrypted += jump_key[num]
        return encrypted 
    elif task == 2:
        numbers = str(input("Please enter the numbers you would like to decrypt with Jump-Five: "))
        for num in numbers:
            encrypted += jump_key[num]
        return encrypted

def main():
    task = welcome()

    if task == 1:
        print("The encrypted numbers are: " + decrypt(task))
    elif task == 2:
        print("The decrypted numbers are: " + decrypt(task))


if __name__ == "__main__":
    main()