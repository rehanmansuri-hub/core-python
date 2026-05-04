import re #Regular Expression
import os #Operating System


def readLine():

    input_file = open("C:\\Users\\AFJAL MANSURI\\OneDrive\\Desktop\\correct_gmail.txt", 'r')
    output_file1 = open("C:\\Users\\AFJAL MANSURI\\OneDrive\\Desktop\\gmail.txt", "w")
    output_file2= open("C:\\Users\\AFJAL MANSURI\\OneDrive\\Desktop\\yahoo.txt", "w")
    output_file3 = open("C:\\Users\\AFJAL MANSURI\\OneDrive\\Desktop\\outlook.txt", "w")

    for line in input_file:
        if (re.search("@gmail.com", line)):
            output_file1.write(line)
        if (re.search("@yahoo.com", line)):
            output_file2.write(line)
        if (re.search("@outlook.com", line)):
            output_file3.write(line)



            print(line)
    input_file.close()
    output_file1.close()
    output_file2.close()
    output_file3.close()


readLine()


