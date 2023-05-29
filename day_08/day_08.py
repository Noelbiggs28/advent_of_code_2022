def how_many_visible(file):
    with open(file,'r') as infile:
        for line in infile:
            print(line.strip())

print(how_many_visible('practice.txt'))