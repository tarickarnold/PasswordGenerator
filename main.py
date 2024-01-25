import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+{}:\"<>?[];',./\\"
all_chars = lower + upper + numbers + symbols

length = 16

password = ''.join(random.sample(all_chars, length))
print("Generated Password:", password)

