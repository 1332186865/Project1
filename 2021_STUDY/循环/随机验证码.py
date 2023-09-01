import random


def generate_code(code_len=4):
    all_chars = '0123456789'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


a = generate_code()
print(a)
