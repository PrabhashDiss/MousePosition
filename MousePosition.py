import pyautogui

print("Press Ctrl-C to quit.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse pointer location: ({x}, {y})")
except KeyboardInterrupt:
    print("\nExiting program.")
