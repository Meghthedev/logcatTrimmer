import re
from datetime import datetime

def trim_logcat(logcat):
    trimmed_logcat = re.sub(r'^((?!crash|error|fail|fatal|not found|avc|missing).)*$\n', '', logcat, flags=re.MULTILINE)
    return trimmed_logcat

def save_logcat(logcat):
    today = datetime.now().strftime('%d%m')
    filename = f"{today}-Logcat.txt"
    with open(filename, 'w') as file:
        file.write(logcat)
    return filename  # Return the filename for printing

def main():
    filename = input("Enter the filename of the input logcat file: ")
    try:
        with open(filename, 'r') as file:
            logcat = file.read()
            trimmed_logcat = trim_logcat(logcat)
            saved_filename = save_logcat(trimmed_logcat)  # Store the returned filename
            print(f"Logcat saved to {saved_filename}")  # Print the saved filename
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")

if __name__ == "__main__":
    main()
