def reverse_lines(input_file, output_file):
    with open(input_file, 'r') as reader:
        lines = reader.read().splitlines()
    with open(output_file, 'w') as writer:
        writer.write('\n'.join(line for line in reversed(lines)))


reverse_lines('input.txt', 'output.txt')