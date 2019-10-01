from Usage import usage
import sys

def cut(args):
    """remove sections from each line of files"""
    # throws an error message for too few arguments
    if len(args) <= 0:
        usage("too few arguments", "cut")
        sys.exit(2)

    startIndex = 0  # tells the program where to start in args
    columnsToPrint = []  # stores the column numbers of the CSV we need to print

    # determines if the fields to print have been specified and assigns them
    if args[0] == "-f":
        # throws an error message for too few arguments
        if len(args) < 3:
            usage("too few arguments", 'cut')
            sys.exit(3)

        columnsToPrint = args[1].split(',')
        startIndex = 2  # sets the program to start where the actual files will be

        # converts the contents of columnsToPrint to integers and sorts them in ascending order
        for i in range(0, len(columnsToPrint)):
            columnsToPrint[i] = int(columnsToPrint[i])

        columnsToPrint.sort()

    else:
        columnsToPrint.append(0)  # sets default column to print to 0

    # opens CSV files in order
    for file in args[startIndex:]:
        currentFile = open(file)

        # splits the current line of a CSV file wherever there is a "," and stores them in a list
        for line in currentFile:
            columns = line.split(",")
            i = 0

            printMessage = ""  # creates a string that we will print later

            # adds the contents of columns that match the specified fields to our final print message in CSV style
            while i < len(columnsToPrint):
                if i > 0:
                    printMessage += ","

                # adds an empty string if the index is out of range for columns
                if (columnsToPrint[i] - 1) >= len(columns):
                    printMessage += ""

                else:
                    printMessage += columns[columnsToPrint[i] - 1].rstrip()

                i += 1

            print(printMessage)  # prints a line that contains the specified columns in CSV style

        currentFile.close()

def paste(args):
    """merge lines of files"""
    # throws an error message for too few arguments
    if len(args) <= 0:
        usage("too few arguments", "paste")
        sys.exit(2)

    finalListLength = 0  # this sets the length of all the columns in the CSV file to be created

    # figure out the file with the most lines and store it in finalListLength
    for file in args:
        currentFile = open(file)
        fileLength = len(list(currentFile))
        currentFile.close()

        if fileLength > finalListLength:
            finalListLength = fileLength

    finalList = []  # this is where we will store the final strings to be printed

    # open the current file and store its lines in tempLineList and then close the file
    for file in args:
        currentFile = open(file)
        tempLinesList = currentFile.readlines()
        currentFile.close()
        i = 0

        # if the file is shorter than the longest file, pad its list with empty strings at the end
        while len(tempLinesList) < finalListLength:
            tempLinesList.append("")

        # add items from tempLinesList to finalList in CSV style whilst iterating using i
        while i < finalListLength:
            # add the current index of tempLinesList to finalList if its current index is empty
            if len(finalList) < finalListLength:
                finalList.append(tempLinesList[i].rstrip())

            # add the current index of tempLinesList with a comma if finalList[i] is not empty
            else:
                tempString = "," + tempLinesList[i].rstrip()

                finalList[i] += tempString

            i += 1

    # print the list containing the lines of our new CSV file
    for string in finalList:
        print(string)
