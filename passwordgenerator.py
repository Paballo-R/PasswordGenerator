import secrets
import string

def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    specialchars = string.punctuation

    pwrd = letters + digits + specialchars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(pwrd))

        if (any(char in specialchars for char in pwd) and sum(char in digits for char in pwd) >= 2):
            pw_strong = True

    return pwd

if __name__ == '__main__':
    print(create_pw())