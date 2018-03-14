import pyautogui as pg
import time
import webbrowser
points = 0

# Question
answer = pg.prompt(
"""
Which team has the most superbowls wins?

a)Cowboys
b)Steelers
c)Patriots
"""
    )

# Give points
if answer == "a":
    points += 0
elif answer == "b":
    points += 1
elif answer == "c":
    points += 0

# Question
answer = pg.prompt(
"""
Which of this teams has NOT won a super bowl?

a)Vikings
b)Saints
c)Ravens
"""
    )

# Give points
if answer == "a":
    points += 1 
elif answer == "b":
    points += 0
elif answer == "c":
    points += 0


# Question
answer = pg.prompt(
"""
Which of these quarterbacks has the most passing yards?

a)Drew Brees
b)Dan Marino
c)Brett Favre
"""
    )

# Give points
if answer == "a":
    points += 0 
elif answer == "b":
    points += 0
elif answer == "c":
    points += 1

# Question
answer = pg.prompt(
"""
Who has the record for the most rushing touchdowns in one season?

a)Emmit Smith
b)Barry Sanders
c)LaDainian Tomlinson
"""
    )

# Give points
if answer == "a":
    points += 0 
elif answer == "b":
    points += 0
elif answer == "c":
    points += 1

# Question
answer = pg.prompt(
"""
Which of these players has the most receiving yards in their career?

a)Terrel Owens
b)Randy Moss
c)Larry Fitzgerald
"""
    )

# Give points
if answer == "a":
    points += 1 
elif answer == "b":
    points += 0
elif answer == "c":
    points += 0

# Question
answer = pg.prompt(
"""
Which of these players has the most interceptions in a career?

a)Charles Woodson
b)Ronnie Lott
c)Ed Reed
"""
    )

# Give points
if answer == "a":
    points += 1 
elif answer == "b":
    points += 0
elif answer == "c":
    points += 0
# END OF SURVEY
if points <=2:
    pg.alert("You are not a football fan")
    webbrowser.open ("https://www.google.com/search?q=NFL+football+fans&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjq-tXT0P3YAhWOl-AKHR8dCQMQ_AUICigB&biw=1366&bih=637#imgrc=lO8gUsRT2vCrHM:")
if points >2 and points <5:
    pg.alert("you are an intermidiate football fan")
    webbrowser.open ("https://www.google.com/search?q=NFL+football+fans&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwim_6uH0P3YAhUyleAKHXkXA04Q_AUICigB&biw=1366&bih=637#imgrc=bnER2Ib9UymrfM:")
if points >4:
    pg.alert("you are a real football fan")
    webbrowser.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1366&bih=637&tbm=isch&sa=1&ei=Qk9vWu3rCsK1ggepza3gBg&q=nfl+fans&oq=nfl+fans&gs_l=psy-ab.3..0l10.5314.6242.0.6521.5.4.1.0.0.0.72.253.4.4.0....0...1c.1.64.psy-ab..0.5.259...0i7i30k1.0.FkBcU3dTuxw#imgrc=5Ywy7MlZMDsvAM:")
