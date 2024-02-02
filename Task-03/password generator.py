import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if length <= 0:
        print("Please enter a positive number for the password length.")
        return
    
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
