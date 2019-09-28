def cat(args):
    """concatenate files and print on the standard output"""
    # the below for loop opens each file in args and adds the next file to the end of the first file
    for file in args:
        currentFile = open(file)

        # this for loop prints the file line by line (ending with a space)
        for line in currentFile:
            print(line, end='')

        currentFile.close()

def tac(args):
    """concatenate and print files in reverse"""
    print("TODO: concatenate and print files in reverse")
