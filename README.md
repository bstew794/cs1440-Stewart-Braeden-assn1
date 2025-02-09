# CS 1440 Assignment 1: Text Tools

* [Instructions](doc/Instructions.md)
* [Expected Output](doc/examples)
* [Hints](doc/Hints.md)
* [Rubric](doc/Rubric.md)
* [WorkLog](doc/WorkLog)

## Overview

A client has sought DuckieCorp's services to process a large quantity of textual data.  Specifically, the data is in the
form of a Comma Separated Values (CSV) file which is far too large to load as a spreadsheet in an application such as
LibreOffice Calc or Microsoft Excel.

My supervisor explained to the client that it would be easier for them to install Linux and use its built-in text
processing tools for this job.  Fortunately for our bottom line (and my job security), this client is adamant that
installing Linux is out of the question.  Instead, DuckieCorp will recreate a suite of Linux text processing programs
in Python.

my supervisor made a start at this project, but only got as far as creating a general outline and finishing the
`usage()` routine before his other responsibilities at DuckieCorp became too great. He has left this project to me,
the only one available, to complete.  Hopefully, my good work will turn this small job will into a standing contract.



## Objectives

-   Process command-line arguments in `sys.argv`
-   Organize code into modules
-   Process string data with Python's built-in functionality
-   Efficiently process large quantities of data


## Expected Behavior

Read the [example](doc/examples) files to see what a correct program's output might look like.

In the provided samples, lines beginning with `$` represent the command typed into the shell.
When you run the same command you should not copy the `$`.

## Miscellaneous

tail() in Partial.py is my most inefficient function since I have it iterate through the given file twice.