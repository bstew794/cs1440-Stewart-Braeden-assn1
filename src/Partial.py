from Usage import  usage
import  sys

def head(args):
    """output the first part of files"""
    # create variables to specify beginning and end indexes
    endLineIndex = 10
    startFileIndex = 0

    # exits the program with a usage() message if there are not enough arguments
    if len(args) <= 0:
        usage('too few arguments', 'head')
        sys.exit(2)

    # change endLineIndex to the number that the user desires if they typed in "-n" n the command line
    if args[0] == "-n":
        # exits the program with a usage() message if there are not enough arguments
        if len(args) < 3:
            usage('too few arguments', 'head')
            sys.exit(3)

        # exits the program with a usage() message if a invalid number of lines is not given
        if not args[1].isdigit():
            usage('Number of lines is required', 'head')
            sys.exit(3)

        endLineIndex = int(args[1])
        startFileIndex = 2

    # open the files in order
    for file in args[startFileIndex:]:
        currentFile = open(file)
        count = 0

        # print the lines of the current file and increase the count by one; end and close the file when at endLineIndex
        for line in currentFile:
            print(line, end='')
            count += 1

            if count == endLineIndex:
                break

        currentFile.close()  # close the file


def tail(args):
    """output the last part of files"""
    # create variables to specify beginning and end indexes
    numOfLinesGiven = 10
    startFileIndex = 0

    # exits the program with a usage() message if there are not enough arguments
    if len(args) <= 0:
        usage('too few arguments', 'tail')
        sys.exit(2)

    # change numOfLinesGiven to the number that the user desires if they typed in "-n" n the command line
    if args[0] == "-n":
        # exits the program with a usage() message if there are not enough arguments
        if len(args) < 3:
            usage('too few arguments', 'tail')
            sys.exit(3)

        # exits the program with a usage() message if a invalid number of lines is not given
        if not args[1].isdigit():
            usage('Number of lines is required', 'tail')
            sys.exit(2)

        numOfLinesGiven = int(args[1])
        startFileIndex = 2

    # open the files in order starting at startFileIndex
    for file in args[startFileIndex:]:
        currentFile = open(file)
        lineCount = 0

        # count the lines in the file
        for line in currentFile:
            lineCount += 1

        # calculate on which line to start
        startLineIndex = lineCount - numOfLinesGiven

        # if the linCount is less than numOfLinesGiven then start at the beginning of the file
        if startLineIndex < 0:
            startLineIndex = 0

        lineIterator = 0

        currentFile.seek(0, 0)  # resets pointer to the top of the file

        # print lines once the lineIterator is == startLineIndex; must iterate by one for each line read
        for line in currentFile:
            if lineIterator >= startLineIndex:
                print(line, end='')
            lineIterator += 1

        currentFile.close()  # close current file
