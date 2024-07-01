print("Welcome to password generator!")

import random #generates random choices 
import string #adding all types of characters in the string

#define the types of characters
def GenPass(length):
    upperChar = string.ascii_uppercase #upper case characters 
    lowerChar = string.ascii_lowercase  #lower case characters 
    digitsChar = string.digits  #digit characters 
    specialChar = string.punctuation #symbol characters
    
    # Ensure the password contains at least one of each character type
    password = [
        random.choice(upperChar),
        random.choice(lowerChar),
        random.choice(digitsChar),
        random.choice(specialChar)
    ]
    
    AddAll= upperChar+lowerChar+digitsChar+specialChar
    password+= random.choice(AddAll)

    #shuffle the list 
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

def main():
    while True:
        try:
            # Prompt the user to specify the desired length of the password
            length = int(input("Enter the desired length of the password (8-20): "))
            
            if 8 <= length <= 20:
                # Generate password
                password = GenPass (length)
                
                # Display the generated password
                print(f"Generated password: {password}")
                break
            else:
                print("Please enter a length between 8 and 20.")
                
        except ValueError:
            print("Wrong Input. Please enter a valid number for the password length.")

if __name__== "__main__":
    main()
