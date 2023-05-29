def count_data(file):
    with open(file, 'r') as infile:
        for line in infile:
            print(line.strip())


print(count_data('list_of_commands.txt'))