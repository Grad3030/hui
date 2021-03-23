from random import choices
from string import ascii_letters, digits

SYMBOLS = list(set(ascii_letters + digits) - {'I', 'l', '1', 'o', 'O', '0'})


def generate_password(m):
    return ''.join(choices(SYMBOLS, k=m))


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        passwords.add(generate_password(m))
    return list(passwords)


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")