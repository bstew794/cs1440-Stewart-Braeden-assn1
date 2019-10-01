from Usage import usage
import sys

def cat(args):
    """concatenate files and print on the standard output"""
    # throws an error message for too few arguments
    if len(args) <= 0:
        usage("too few arguments", "cat")
        sys.exit(2)

    # the below for loop opens each file in args and adds the next file to the end of the first file
    for file in args:
        currentFile = open(file)

        # this for loop prints the file line by line (ending with a space)
        for line in currentFile:
            print(line, end='')

        currentFile.close()

def tac(args):
    """concatenate and print files in reverse"""
    # throws an error message for too few arguments
    if len(args) <= 0:
        usage("too few arguments", "tac")
        sys.exit(2)

    # the below for loop opens each file in args and adds the next file to the end of the first file
    for file in args:
        currentFile = open(file)

        # this for loop prints the file line by line in reverse (ending with a space)
        for line in reversed(list(currentFile)):
            print(line, end='')

        currentFile.close()
