#open("ReadFilesExample.txt", "r")   Only allows you to read the data
                        #  , "w")    Only allows you to edit the file
                        #  , "a")    Only allow you add to the end
                        # , "r+")    Allows you to both read and write

employee_file = open("ReadFilesExample.txt", "r")
employee_file.close()
#print(employee_file.readable())   Returns boolean for whether it can be read
#print(employee_file.read())       Outputs everything in the file
#print(employee_file.readline())   Reads the first line
#print(employee_file.readline())   Reads next line
#print(employee_file.readlines())  Take all lines and put in list
#print(employee_file.readlines()[1]) Outputs 2nd line in file
#for employee in employee_file.readlines():  # How to iterate through
#    print(employee)
#employee_file.close()   # Need to close once finished

with open("ReadFilesExample.txt", "r") as file: # This auto closes the file when finished
    print (file.readlines())