def sort_file():
    from tkinter.filedialog import askopenfilename

    # open dialog
    filename = askopenfilename()

    # get the content of file
    readfile = open(filename)

    # generate array, str.split('\n')
    arr = readfile.readlines()
    readfile.close()

    # sort the array
    arr.sort()

    # update the file
    writefile = open(filename, "w")
    writefile.writelines(arr)
    writefile.close()


    # user feedback

    print("file updated")
    input("press enter to quit")



if __name__ == "__main__":
    sort_file()
