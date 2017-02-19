import time
import webbrowser

totalBreaks = 3
breakCount  = 0


print("This program started at " + time.ctime());
while (breakCount < totalBreaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=c2O56nWEN2E")
    breakCount = breakCount + 1
