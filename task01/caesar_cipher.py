# This is a simple Caesar Cipher program that helps you encrypt and decrypt messages
# The Caesar Cipher shifts each letter in the alphabet by a certain number of positions

def encrypt_message(message, shift):
    """
    This function encrypts a message by shifting each letter by the specified number
    For example, with shift=1: 'A' becomes 'B', 'B' becomes 'C', etc.
    """
    # Create an empty string to store our encrypted message
    encrypted = ""
    
    # Go through each character in the message
    for char in message:
        # Check if the character is a letter (a-z or A-Z)
        if char.isalpha():
            # If it's a lowercase letter, start from 'a' (97 in ASCII)
            # If it's an uppercase letter, start from 'A' (65 in ASCII)
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            
            # Convert the letter to a number (0-25), shift it, and wrap around if needed
            # ord(char) converts the letter to its ASCII number
            # We subtract 'start' to get a number from 0-25
            # We add the shift and use % 26 to wrap around the alphabet
            shifted = (ord(char) - start + shift) % 26
            
            # Convert back to a letter and add to our result
            encrypted += chr(start + shifted)
        else:
            # If the character is not a letter (like space, punctuation, numbers),
            # keep it as is
            encrypted += char
    
    return encrypted

def decrypt_message(message, shift):
    """
    This function decrypts a message by shifting each letter backwards
    For example, with shift=1: 'B' becomes 'A', 'C' becomes 'B', etc.
    """
    # To decrypt, we just encrypt with a negative shift
    return encrypt_message(message, -shift)

def main():
    # This is the main program that runs when you start the script
    while True:
        # Show the menu
        print("\n=== Welcome to Caesar Cipher ===")
        print("What would you like to do?")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit the program")
        
        # Get the user's choice
        choice = input("\nEnter your choice (1, 2, or 3): ")
        
        # If they choose to exit
        if choice == '3':
            print("Thank you for using Caesar Cipher! Goodbye!")
            break
        
        # Check if the choice is valid
        if choice not in ['1', '2']:
            print("Oops! That's not a valid choice. Please enter 1, 2, or 3.")
            continue
        
        # Get the message from the user
        message = input("Enter your message: ")
        
        # Get the shift value with error checking
        while True:
            try:
                # Ask for the shift value
                shift = int(input("Enter the shift value (0-25): "))
                # Check if the shift is valid
                if 0 <= shift <= 25:
                    break
                else:
                    print("The shift must be between 0 and 25!")
            except ValueError:
                print("Please enter a number!")
        
        # Process the message based on the user's choice
        if choice == '1':
            # Encrypt the message
            result = encrypt_message(message, shift)
            print(f"\nYour encrypted message is: {result}")
        else:
            # Decrypt the message
            result = decrypt_message(message, shift)
            print(f"\nYour decrypted message is: {result}")

# This line makes sure the program only runs if you run this file directly
if __name__ == "__main__":
    main() 
