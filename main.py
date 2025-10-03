#!/usr/bin/env python3
import sys
import os
import time
from colorama import Fore, Style, init

# init colorama
init(autoreset=True)

# rainbow color list
rainbow_colors = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA
]

def rainbow_print(text, delay=0.01, end="\n"):
    """
    Slow rainbow print — prints text character by character with rainbow colors.
    end: newline or '' etc.
    """
    for i, ch in enumerate(text):
        sys.stdout.write(rainbow_colors[i % len(rainbow_colors)] + ch + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    # end handling
    if end:
        sys.stdout.write(end)
        sys.stdout.flush()

def prompt_rainbow(prompt_text, delay=0.01):
    """
    Print the prompt in rainbow on the same line (no newline) then call input().
    Returns the input string, or None on EOF/Interrupt.
    """
    try:
        # print prompt without newline but with slow effect
        for i, ch in enumerate(prompt_text):
            sys.stdout.write(rainbow_colors[i % len(rainbow_colors)] + ch + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(delay)
        # now get input from user (cursor stays on same line)
        return input()
    except (EOFError, KeyboardInterrupt):
        # put newline so terminal looks tidy
        print()
        return None

def safe_input(prompt_text="", delay=0.01):
    """
    Wrapper: show rainbow prompt and handle EOF/KeyboardInterrupt gracefully.
    If prompt_text is empty, just call input() but still handled.
    """
    if prompt_text:
        return prompt_rainbow(prompt_text, delay=delay)
    else:
        try:
            return input()
        except (EOFError, KeyboardInterrupt):
            print()
            return None

# === Application logic with rainbow UI ===

def main():
    """MAIN loop: returns next state 'link' or 'exit'"""
    while True:
        os.system("clear")
        rainbow_print("=== MAIN MENU ===", 0.005)
        rainbow_print("1. Camera hack link generator", 0.005)
        rainbow_print("2. Exit", 0.005)

        choice = safe_input("\nEnter your choice: ", delay=0.01)
        if choice is None:
            # non-interactive or interrupted → exit
            rainbow_print("\nNo input detected. Exiting...", 0.01)
            time.sleep(0.6)
            return "exit"

        choice = choice.strip()
        if choice == "1":
            rainbow_print("\nLink generator menu redirecting...", 0.01)
            time.sleep(0.6)
            return "link"
        elif choice == "2":
            rainbow_print("\nExiting...", 0.01)
            time.sleep(0.4)
            return "exit"
        else:
            rainbow_print("\nInvalid choice. Try again.", 0.01)
            time.sleep(1)

def link():
    """LINK loop: returns 'main' or 'exit'"""
    while True:
        os.system("clear")
        rainbow_print("=== LINK GENERATOR MENU ===", 0.005)
        rainbow_print("Note: demo placeholder only. No illegal actions supported.", 0.005)

        chat_id = safe_input("\nEnter your TG chat id (or press Enter to go back): ", delay=0.01)
        if chat_id is None:
            rainbow_print("\nNo input. Exiting...", 0.01)
            return "exit"
        if chat_id.strip() == "":
            # back to main
            rainbow_print("\nGoing back to MAIN menu...", 0.01)
            time.sleep(0.4)
            return "main"

        bot_token = safe_input("Enter your bot token (or press Enter to go back): ", delay=0.01)
        if bot_token is None:
            rainbow_print("\nNo input. Exiting...", 0.01)
            return "exit"
        if bot_token.strip() == "":
            rainbow_print("\nGoing back to MAIN menu...", 0.01)
            time.sleep(0.4)
            return "main"

        # Demo behavior: show received values (NO illegal functionality provided)
        rainbow_print("\n[Demo] Received chat_id: " + chat_id, 0.01)
        rainbow_print("[Demo] Received bot_token: " + bot_token, 0.01)

        nxt = safe_input("\nPress Enter to stay in LINK menu, type 'back' to go MAIN, or 'exit' to quit: ", delay=0.01)
        if nxt is None:
            rainbow_print("\nExiting...", 0.01)
            return "exit"
        nxt = nxt.strip().lower()
        if nxt == "back":
            return "main"
        elif nxt == "exit":
            return "exit"
        # otherwise loop continues (stay in link menu)

# === CONTROLLER ===
if __name__ == "__main__":
    current = "main"
    while True:
        if current == "main":
            current = main()
        elif current == "link":
            current = link()
        else:
            # exit or unknown state → break
            break

    rainbow_print("\nProgram terminated. Thanks!", 0.01)
