import time
import webbrowser
import pyautogui

url = "https://l9edating.com/match"
webbrowser.open(url)

while True:
    time.sleep(0.5) 
    pyautogui.click(612,361)
    time.sleep(0.5)
    pyautogui.click(605,474)
    time.sleep(0.5)
    for i in range(10):
        print(f"Iteration {i+1}")
        pyautogui.keyDown("right") 
        time.sleep(0.5)
    print("Finished 10 iterations of holding right arrow key.")