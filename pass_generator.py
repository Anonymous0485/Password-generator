import threading
import time
import secrets
import string

def generate_password(length=8):
    list = "@"
    """Generate a random password with letters (uppercase and lowercase), digits, and symbols."""
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_unique_password_to_file(password, password_set, filename='passwords.txt'):
    """Save the generated password to a file if it's unique."""
    if password not in password_set:
        with open(filename, 'a') as file:
            file.write(password + '\n')
        password_set.add(password)

def password_generator():
    unique_passwords = set()
    while True:
        password = generate_password()
        save_unique_password_to_file(password, unique_passwords)
        time.sleep(1)  # Adjust sleep duration as needed

# Start the generator thread
generator_thread = threading.Thread(target=password_generator)
generator_thread.start()

# Wait for the generator thread to finish
generator_thread.join()
