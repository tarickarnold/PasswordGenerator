import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "0123456789"
all_chars = "!@#$%^&*()_+{}:\"<>?[];',./\\"

length = 16

password = ''.join(random.sample(all_chars, length))
print("Generated Password:", password)
