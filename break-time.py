#Written by Anthony Ciulla!
#Date: 12/30/2016 @ 10:37PM

import webbrowser #import for opening in chrome
import time #import for current time and program sleep
import sys #import to shut the program down

desired_breaks = input('Enter Desired Number of Breaks: ') #Input Number Breaks We Want!
desired_breaks = int(desired_breaks) #Convert desired_breaks back to int because input converts it to str
desired_hours = input('Enter Desired Hours Between Breaks: ') # How Long Between Breaks
desired_hours = int(desired_hours) #Convert desired_hours back to int because input converts it to str
desired_video = "https://www.youtube.com/watch?v=26Mqmc5rWM8" #Video to Open(Lauren Daigle)
breaks = 1 #Set to 1 so that we dont take 4 breaks for some reason
current_time = time.ctime() #add the current time to a var

desired_seconds = desired_hours * 60 * 60 #convert desired_hours to seconds

print("Break Program Started At " + current_time)#print that the program is starting

while(breaks <= desired_breaks):#while we still have breaks to take
    print("Will notify for " + str(desired_breaks) + " breaks, with your next break time in " + str(desired_seconds) + " seconds!")#print vars about break
    time.sleep(int(desired_seconds)); #make program wait for desired time
    print("Opening " + desired_video + "!") #let user know that we are opening the video
    webbrowser.open(desired_video) #open the video
    print("Will Remind you again in " + str(desired_seconds) + " Seconds, with " + str(desired_breaks - breaks) + " breaks left!")#inform them of time until next break
    print("=============================================================================") #clean line to seperate breaks
    breaks += 1 #add 1 to break counter

while(breaks == desired_breaks): #when we have used all our breaks
    exit() #end the program

