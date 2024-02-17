def tokenize():

    file =  open("input.txt", 'r')

    #print(file.read())
    spaceFree = ""

    for line in file:
        if ("#" in line):
            continue

        spaceFree += "\n"
        for character in line:
            if (not character.isspace()):
                spaceFree += character
    print(spaceFree)

tokenize()