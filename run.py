import pyautogui
import time
import threading
import keyboard 
import webbrowser

## Main Url to open
url = "https://l9edating.com/match"
webbrowser.open(url)
time.sleep(3)

loc1 = (612, 361)  # Coordinates to click on the drop down menu
loc2 = (605, 474)  # Coordinates to click on the healslut option

stop_script = False

def check_esc():
    global stop_script
    while not stop_script:
        if keyboard.is_pressed('esc'):
            stop_script = True
            print("\nESC pressed! Stopping IMMEDIATELY...")
            break
        time.sleep(0.01)

print("Script started! Press ESC to stop IMMEDIATELY.")

# Start ESC monitoring thread
esc_thread = threading.Thread(target=check_esc, daemon=True)
esc_thread.start()

try:
    while not stop_script:
        pyautogui.click(loc1)
        time.sleep(0.5)
        pyautogui.click(loc2)
        time.sleep(0.5)
        
        for i in range(10):
            if stop_script:
                break
            print(f"Iteration {i+1}")
            pyautogui.keyDown("right") 
            time.sleep(0.5)
            pyautogui.keyUp("right")
        
        if stop_script:
            break    
        print("Finished 10 iterations.")

except KeyboardInterrupt:
    stop_script = True
    print("\nStopped by Ctrl+C!")
finally:
    pyautogui.keyUp("right")
    print("Cleanup complete.")