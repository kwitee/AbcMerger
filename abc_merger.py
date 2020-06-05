import os
import sys


def convert_x_numbering(abc):
    converted_abc = str()
    counter = 1

    for line in iter(abc.splitlines()):
        previous = converted_abc + "\n" if converted_abc != str() else str()

        if line.startswith("X:"):
            converted_abc = previous + "X: " + str(counter)
            counter = counter + 1
        else:
            converted_abc = previous + line

    return converted_abc


directory = sys.argv[1]
output_file_path = os.path.join(directory, "merged.abc")

if os.path.exists(output_file_path):
    os.remove(output_file_path)

output = str()

for file_name in os.listdir(directory):
    if file_name.endswith(".abc"):
        with open(os.path.join(directory, file_name), "r") as input_file:
            output = (output + "\n\n" if output != str() else str()) + input_file.read()

        output = convert_x_numbering(output)

        with open(output_file_path, "w") as output_file:
            output_file.write(output)
