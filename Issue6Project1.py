import string
import random
import re

length = random.randint(8,14)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

i = 0
while i < 41:
        special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
        all = lower + upper + num + symbols
        temp = random.sample(all,length)
        password = "".join(temp)
        print(password)
        i += 1
