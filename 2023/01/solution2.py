import re

from word2number import w2n

with open("input.txt") as file:
    data = file.readlines()


split_line = str()
data_list = []
fix_line = []
format_line = str()
number_list = []
grand_total = 0
start_of_sting_numbers = None

# Remove \n in data
for line in data:
    if "\n" in line:
        fix_line = line[:-1]
        data_list += [fix_line]
else:
    data_list += [line]

# print (data_list)


for line in data_list:
    format_line = str()
    for char in line:
        if char.isnumeric():
            format_line = format_line + ("#" + char + "#")
        else:
            format_line = format_line + char

    split_line = format_line.split("#")
    final_line = list(filter(None, split_line))

    end_of_string_number = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)

    if re.search("one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", str(final_line[0])) is None:
        start_of_sting_numbers = re.search(
            "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", str(final_line[1])
        ).group(0)
    else:
        start_of_sting_numbers = re.search(
            "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", str(final_line[0])
        ).group(0)
    start_total = w2n.word_to_num(start_of_sting_numbers)
    end_total = w2n.word_to_num(end_of_string_number[-1])

    numbercombine = str(start_total) + str(end_total)

    print("Line: " + str(line))
    print("Combine: " + str(numbercombine))
    grand_total = int(numbercombine) + grand_total

print(grand_total)
