def main():
    """
    # open files
    file = open("./data/data.txt", "r")
    print (file.read())
    file.close()

    #alternative way to open files
    with open("/home/becode/data/data.txt", "r") as fichier:
          print(fichier.read())

    # open data.txt and split in sentences
    textList = []
    file = open("/home/becode/data/data.txt", "r")
    text =  (file.read())
    textList = text.split(".") #text split at "."
    print(textList)
    file.close()

    # how to open and write in a file
    file = open("/home/becode/data/data.txt", "a")
    file.write("Hi everyone, I'm adding sentences to the file !")
    file.close()

    # Can you take the content of the data.txt file from the data directory, capitalize all the words and write them in the writing file after the existing one ?
    # It's up to you to write the end
    wordList = []
    with open("/home/becode/data/data.txt", "r") as fichier:
        text = fichier.read()
        for word in text.split(" "):
            wordList.append(word.capitalize()) # this works best
    file = open("/home/becode/data/write.txt", "a")
    file.write(" ".join(wordList))
    file.close()

    # put all filenames in variable and then in final.txt
    import os.path
    import re
    file_names = []
    # print(os.listdir("/home/becode"))
    path = os.path.abspath('/home/becode/data')
    folder_path = path

    for path, dirs, files in os.walk(folder_path):
        for filename in files:
            if re.match("(.)+.txt", filename) is not None:
                file_names.append(filename)

    #rep_text = os.path.join(path, "text") # I used os.mkdir instead
    os.mkdir("/home/becode/data/text")
    file = open("/home/becode/data/text/final.txt", "a")
    for item in file_names:
        file.write(item + " ")
    file.close()
    """
    # And then, can you open all the files in your data directory and save all their contents in a variable, using a loop?
    # Finally, save this concatenated information (assemblies) in a new file

    import os.path
    import re

    path = os.path.abspath('/home/becode/data')
    folder_path = path

    string = ""
    for path, dirs, files in os.walk(folder_path):
        for file in files:
            if re.match("(.)+.txt", file) is not None:
                file = open(os.path.join(path, file)) # use path!!
                string += file.read()

    writefile = open(os.path.join(folder_path, "concat.txt"), "a") # good to use a diff variable, writefile, for the file here, instead of again using file = open ...
    writefile.write(string)
    writefile.close()


main()
