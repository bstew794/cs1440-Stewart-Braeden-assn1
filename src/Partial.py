def head(args):
    """output the first part of files"""
    endIndex = 10
    startIndex = 0

    if args[0] == "-n":
        endIndex = int(args[1])
        startIndex = 2

    for file in args[startIndex:]:
        currentFile = open(file)
        count = 0

        for line in currentFile:
            print(line, end='')
            count += 1

            if count == endIndex:
                break

        currentFile.close()


def tail(args):
    """output the last part of files"""
    print("TODO: output the last part of files")
