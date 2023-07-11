import secrets
import string

def generate_pwd(password_length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters + digits + special_chars
    pwd_list = [secrets.choice(characters) for _ in range(password_length)]
    secrets.SystemRandom().shuffle(pwd_list)
    generated_password = ''.join(pwd_list)
    return generated_password
