import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special=True):
    """
    Generate a random password.
    :param length: Length of the password. Default is 12.
    :param uppercase: Include uppercase letters. Default is True.
    :param lowercase: Include lowercase letters. Default is True.
    :param digits: Include digits. Default is True.
    :param special: Include special characters. Default is True.
    :return: A random password.
    """
    # Define character sets
    upper_chars = string.ascii_uppercase if uppercase else ''
    lower_chars = string.ascii_lowercase if lowercase else ''
    digit_chars = string.digits if digits else ''
    special_chars = string.punctuation if special else ''

    # Combine character sets
    chars = upper_chars + lower_chars + digit_chars + special_chars

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

def check_password_strength(password):
    """
    Check the strength of a password.
    :param password: Password to check.
    :return: A tuple containing the password strength and estimated time to crack.
    """
    # Define character sets
    upper_chars = set(string.ascii_uppercase)
    lower_chars = set(string.ascii_lowercase)
    digit_chars = set(string.digits)
    special_chars = set(string.punctuation)

    # Calculate password strength
    strength = ''
    if len(password) < 8:
        strength = 'very weak'
    elif len(password) < 12:
        strength = 'weak'
    else:
        strength = 'strong'

    if any(c in upper_chars for c in password) and \
       any(c in lower_chars for c in password) and \
       any(c in digit_chars for c in password) and \
       any(c in special_chars for c in password):
        strength = 'very strong'

    # Calculate time to crack
    time_to_crack = ''
    if strength == 'very weak':
        time_to_crack = 'less than a second'
    elif strength == 'weak':
        time_to_crack = 'a few minutes'
    elif strength == 'strong':
        time_to_crack = 'a few years'
    else:
        time_to_crack = 'centuries'

    return strength, time_to_crack

# Ask user what they want to do
choice = input('What would you like to do? Generate a random strong password (1) or check the strength of your password (2)? ')

if choice == '1':
    # Generate a random strong password
    length = int(input('Enter the length of the password: '))
    uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    lowercase = input('Include lowercase letters? (y/n): ').lower() == 'y'
    digits = input('Include digits? (y/n): ').lower() == 'y'
    special = input('Include special characters? (y/n): ').lower() == 'y'

    password = generate_password(length=length, uppercase=uppercase, lowercase=lowercase, digits=digits, special=special)
    print(f'Your password is: {password}')

elif choice == '2':
    # Check the strength of a password
    password = input('Enter your password: ')
    strength, time_to_crack = check_password_strength(password)
    print(f'Your password is {strength} and would take {time_to_crack} to crack.')

else:
    print('Invalid choice. Please enter 1 or 2.')
