import os

def renameFiles() :
    #(1) get file names from a folders
    # use 'r' before the path indicate raw string to tell python
    # do not interpret it in another ways round
    file_list = os.listdir(r"C:\Users\Shawn\Documents\OOP\prank")
    print(file_list)

    #get current working directory
    folderPath = os.getcwd();
    print 'Current working path is:', folderPath
    #change the directory where the pictures located in case it resides on
    #the wrong folder
    os.chdir(r"C:\Users\Shawn\Documents\OOP\prank")
    
    #(2) for each file, rename filename
    for file_name in file_list :
        #display the old and new file_name
        print("Old file name :" + file_name)
        print("New file name :" + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

        
    #change back the directory where it used to be at start
    os.chdir(folderPath)
    
renameFiles()
