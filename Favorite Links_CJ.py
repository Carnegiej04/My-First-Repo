import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=LsoLEjrDogU"]
music =["https://www.youtube.com/watch?v=X6waHtSgCTc"]

answer = pg.prompt(
"""
which would you like to do?
a) Watch Videos
b) Listen to Music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
