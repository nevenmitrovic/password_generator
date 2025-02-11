import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password_storage = []
for i in range(0, sum([nr_letters, nr_symbols, nr_numbers])):
    raw = random.randint(0, 2)
    let_index = random.randint(0, len(letters) -1)
    nr_index = random.randint(0, len(numbers) -1)
    sym_index = random.randint(0, len(symbols) - 1)

    if raw == 0:
        if len(set(password_storage) & set(letters)) < nr_letters:
            password_storage.append(letters[let_index])
        else:
            raw = random.randint(1, 2)
            if raw == 1:
                if len(set(password_storage) & set(numbers)) < nr_numbers:
                    password_storage.append(numbers[nr_index])
                else:
                    if len(set(password_storage) & set(symbols)):
                        password_storage.append(symbols[sym_index])
            else:
                if len(set(password_storage) & set(symbols)):
                    password_storage.append(symbols[sym_index])
                else:
                    if len(set(password_storage) & set(numbers)) < nr_numbers:
                        password_storage.append(numbers[nr_index])

    elif raw == 1:
        if len(set(password_storage) & set(numbers)) < nr_numbers:
            password_storage.append(numbers[nr_index])
        else:
            raw = random.randint(0, 1)
            if raw == 0:
                if len(set(password_storage) & set(letters)) < nr_letters:
                    password_storage.append(letters[let_index])
                else:
                    if len(set(password_storage) & set(symbols)):
                        password_storage.append(symbols[sym_index])
            else:
                if len(set(password_storage) & set(symbols)):
                    password_storage.append(symbols[sym_index])
                else:
                    if len(set(password_storage) & set(letters)) < nr_letters:
                        password_storage.append(letters[let_index])
    else:
        if len(set(password_storage) & set(symbols)) < nr_symbols:
            password_storage.append(symbols[sym_index])
        else:
            raw = random.randint(0, 1)
            if raw == 1:
                if len(set(password_storage) & set(numbers)) < nr_numbers:
                    password_storage.append(numbers[nr_index])
                else:
                    if len(set(password_storage) & set(letters)) < nr_letters:
                        password_storage.append(letters[let_index])
            else:
                if len(set(password_storage) & set(letters)) < nr_letters:
                    password_storage.append(letters[let_index])
                else:
                    if len(set(password_storage) & set(numbers)) < nr_numbers:
                        password_storage.append(numbers[nr_index])



password_result = ''.join(password_storage)
print(password_result)