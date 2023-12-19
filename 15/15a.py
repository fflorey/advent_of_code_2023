with open("input.txt", "r") as file:
    line = file.readline().strip()


def hash_string(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value


def calculate_focusing_power(sequence):
    boxes = [{} for _ in range(256)]
    total_power = 0

    for step in sequence:
        label = ''.join(filter(str.isalpha, step))
        operation = step[len(label)]

        if len(step) > len(label) + 1:
            focal_power = int(step[len(label) + 1:])
        else:
            focal_power = 0
        
        print("Label:", label, "Operation:", operation, "Focal Power:", focal_power)
        box_index = hash_string(label) % 256
        print("Box Index:", box_index)
        if operation == '=':
            boxes[box_index][label] = focal_power
        elif operation == '-':
            if label in boxes[box_index]:
                del boxes[box_index][label]
        elif operation == '+':
            for lens in boxes[box_index]:
                if lens[0] == label:
                    boxes[box_index][lens] = focal_power
                    break
        print("Box Index:", box_index, "Box:", boxes[box_index])

    print("Calculating total power")
    for box_index in range(256):
        if len(boxes[box_index]) > 0:
            print("Box index:", box_index, "Box:", boxes[box_index], "Total Power:", total_power)
            for lens_id, lens in enumerate(boxes[box_index]):
                print("Lens:", lens, "Focal Length:", boxes[box_index][lens])
                total_power += (box_index + 1) * (lens_id + 1) * boxes[box_index][lens]
            # total_power += sum([(box_index + 1) * (i + 1) * lens[1] for i, lens in enumerate(boxes[box_index])])

    return total_power


# split the line by ',' and store all the strings in a list
strings = line.split(",")
total = 0
focusing_pwr = calculate_focusing_power(strings)
print("focusing power:", focusing_pwr)
input()
print("Now part a of the puzzle")
input()
for s in strings:
    v = hash_string(s)
    print(s, v)
    total += hash_string(s)

print("total:", total)
    