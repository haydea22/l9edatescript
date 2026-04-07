import pyautogui
import time

def find_coordinates():
    for i in range(20):
        x, y = pyautogui.position()
        print(f"Position {i+1}: x={x}, y={y}")
        time.sleep(0.2)

if __name__ == "__main__":
    find_coordinates()