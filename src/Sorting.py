from Usage import usage
import  sys

def sort(args):
    """sort lines of text files"""
    # the next chunk of code checks if there are too few arguments
    if len(args) <= 0:
        usage('too few arguments', 'sort')
        sys.exit(2)

    sortedlist = []  # creates a list to store all the lines of the files accessed

    # opens files in order and then stores their lines in sortedList and then closes the file
    for file in args:
        currentFile = open(file)

        for line in currentFile:
            sortedlist.append(line)

        currentFile.close()

    # prints all the lines once they have been alphabetically sorted
    for line in sorted(sortedlist):
        print(line, end='')
