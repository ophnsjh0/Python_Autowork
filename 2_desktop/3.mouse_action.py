import pyautogui

pyautogui.sleep(3)  # 3초 대기
# print(pyautogui.position())

# pyautogui.click(1588, 194, duration=1)  # 1초 동안 좌표로 이동 마우스 클릭

# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(500, 500)
# pyautogui.mouseDown()
# pyautogui.moveTo(700, 700, duration=1)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1152, 188)
# pyautogui.drag(300, 0, duration=0.5)
# pyautogui.dragTo(1452, 188, duration=0.5)

pyautogui.scroll(300)  # 양수이면 위 방향으로, 음수이면 아래 방향으로 300 만큼 스크롤
pyautogui.scroll(-800)
