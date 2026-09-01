import random
import string

def generate_random_string(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password

length = int(input("Enter the length of password : "))

print(f"Generated random Password: {generate_random_string(length)}")