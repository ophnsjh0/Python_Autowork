import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")  # 파일로 저장

# pyautogui.mouseInfo()
# 1431,195 60,169,242 #3CA9F2

pixel = pyautogui.pixel(1431, 195)
print(pixel)

# print(pyautogui.pixelMatchesColor(1431, 195, (60, 169, 242)))
# print(pyautogui.pixelMatchesColor(1431, 195, pixel))
print(pyautogui.pixelMatchesColor(1431, 195, (60, 169, 243)))
