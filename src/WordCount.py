def wc(files):
    """print newline, word, and byte counts for each file"""
    # reset local count variables at start of every loop as well as open the file to be counted
    for file in files:
        currenFile = open(file)
        lineCount = 0
        wordCount = 0
        byteCount = 0

        # add one to line and word count at the start of every loop for each line
        for line in currenFile:
            lineCount += 1

            wordCount += line.count(" ") + 1

            # add one to byteCount for each bytes in a line
            for bytes in line:
                byteCount += 1

        # print out the formatted counts and the filename and then close currentFile
        print(format(lineCount, "<4d") + format(wordCount, "<4d") + format(byteCount, "<4d") + " " + file)
        currenFile.close()
