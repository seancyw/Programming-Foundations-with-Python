import urllib

def readText() :
    #Open file
    quotes = open(r"C:\Users\Shawn\Documents\OOP\movie_quotes.txt")

    #Read file
    fileContent = quotes.read()
    
    #Close the file
    quotes.close()

    #Check curse words
    checkProfanity(fileContent)

def checkProfanity(text) :
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read();

    #print output
    if (output == 'true') :
        print 'profanity found'
    elif (output == 'false'):
        print 'no profanity found'
    else :
        print 'Unable to scan document properly'
          
    connection.close()

readText()
