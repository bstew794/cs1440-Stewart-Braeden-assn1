from Usage import usage
import sys

def grep(args):
    """print lines that match patterns"""
    # throws an error message for too few arguments
    if len(args) <= 0:
        usage("too few arguments", "grep")
        sys.exit(2)

    goalWord = args[0]  # stores the substring it is looking for
    startIndex = 1  # points to where the first file is in the argument array
    getOpposite = False  # a variable that stores whether or not "-v" has been invoked from the command line

    # sets the proper conditions for if "-v" is invoked at the command line
    if args[0] == "-v":
        # throws an error message for too few arguments
        if len(args) <= 3:
            usage("too few arguments", "grep")
            sys.exit(3)

        goalWord = args[1]
        startIndex = 2
        getOpposite = True

    # open the files in order starting at startIndex
    for file in args[startIndex:]:
        currentFile = open(file)

        for line in currentFile:

            # print all the lines not containing goalWord if getOpposite is True
            if getOpposite:
                if goalWord not in line:
                    print(line, end='')

            # prints all the lines containing goalWord if getOpposite is false
            else:
                if goalWord in line:
                    print(line, end='')

        currentFile.close()  # close the file

def startGrep(args):
    """print lines that match patterns"""
    # throws an error message for too few arguments
    if len(args) <= 0:
        usage("too few arguments", "grep")
        sys.exit(2)

    goalWord = args[0]
    startIndex = 1

    # open the files in order starting at startIndex
    for file in args[startIndex:]:
        currentFile = open(file)

        for line in currentFile:
            columns = line.split(",")
            if goalWord in columns[0]:
                print(line, end='')

        currentFile.close()  # close the file
