import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's you favorite sport?")

answer = pg.prompt("What is your favorite sport?")

if answer == "Basketball":
    speak.Speak ("My favorite sport is Basketball too!")

elif answer == "Football":
    speak.Speak("I Like football too, but i'm better at basketball.")

else:
    speak.Speak("You like the sport " + answer)




speak.Speak("What kind of video do you want to watch?")

video = pg.prompt("Enter video below.")

speak.Speak("OK, let's look for " + video + " on Youtube and see what we find.")

wb.open("https://www.youtube.com/results?search_query=" + video)
