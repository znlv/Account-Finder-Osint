import sys
import time
import argparse

# ANSI color codes for basic colors
COLOR_CODES = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"  # Resets to default color
}

def slow_print(text, delay=0.05, color="reset"):
    color_code = COLOR_CODES.get(color.lower(), COLOR_CODES["reset"])  # Default to reset if color not found
    sys.stdout.write(color_code)  # Set the text color
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    sys.stdout.write(COLOR_CODES["reset"])  # Reset color after printing
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Slowly print text to the console with optional color.")
    parser.add_argument("text", type=str, help="The text to print slowly.")
    parser.add_argument("--delay", type=float, default=0.05, help="Delay between characters (in seconds).")
    parser.add_argument("--color", type=str, choices=COLOR_CODES.keys(), default="reset", help="Text color.")
    
    args = parser.parse_args()
    slow_print(args.text, args.delay, args.color)
