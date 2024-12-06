with open("input.txt") as file:
    data = file.readlines()

total = 0

for line in data:
    line_digits = []
    for char in line:
        if char.isnumeric():
            line_digits.append(int(char))
    get_first_digit = [line_digits[0]]
    get_last_digit = [line_digits[-1]]
    combine_digits = str(get_first_digit[0]) + str(get_last_digit[-1])
    total = int(combine_digits) + total

print(total)
