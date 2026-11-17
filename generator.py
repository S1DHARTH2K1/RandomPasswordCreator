import secrets
import string
import random

MIN_LENTH = 8


def generate_password(length=16, is_lower=True, is_upper=True, is_digits=True, is_symbol=True):
    pools = []
    if is_lower:
        pools.append(string.ascii_lowercase)
    if is_upper:
        pools.append(string.ascii_uppercase)
    if is_digits:
        pools.append(string.digits)
    if is_symbol:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("At least one character type must be selected.")
    if length < MIN_LENTH:
        raise ValueError(f"Password length must be at least {MIN_LENTH} characters.")

    chars = [secrets.choice(pool) for pool in pools]

    everything = "".join(pools)
    for _ in range(length):
        chars.append(secrets.choice(everything))

    random.shuffle(chars)

    return ''.join(chars)

print(generate_password())
print(generate_password(8, is_symbol=False))
print(generate_password(20, is_digits=False))