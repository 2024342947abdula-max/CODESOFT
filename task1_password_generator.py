import random
import string

def generate_password(length):
    """
    Generate a random password based on the specified length.
    Includes uppercase letters, lowercase letters, digits, and symbols.
    """
    # Define character set for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== PASSWORD GENERATOR APPLICATION ===")

    # USER INPUT: Ask for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("ERROR: Password length must be greater than 0.")
            return
    except ValueError:
        print("ERROR: Please enter a valid numeric value.")
        return

    # GENERATE PASSWORD
    password = generate_password(length)

    # DISPLAY PASSWORD
    print("\nGenerated Password:", password)
    print("Password Length:", len(password))


if __name__ == "__main__":
    main()
