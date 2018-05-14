import pyautogui as pg

pg.hotkey('winleft', 'ctrl', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.typewrite('espn.com\n',0.5)
pg.moveTo(174, 112, 3)
pg.click(174, 112, 1)
pg.moveTo(1235, 108, 4)
pg.click(1235, 108, 1)
pg.moveTo(1071, 115, 2)
pg.click(1071, 115, 1)

