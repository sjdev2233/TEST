import sys 
import os 
import time 

def main():
  while True:
        os.system("clear")
        print("=== MAIN MENU ===\n1. Camara hack link generator\n2. Exit")
        choise=input("\nEnter your choice: ")
        if choise == "1":
            print("link generator menu redirecting ")
            return link()
            
        if choise == "2" :   
            print("exit")
            sys.exit()

def link():
    while True:
          print("=== Link Generator menu ===")
          chat_id=input("enter your tg chat id")
          bot_token=input("enter your boy token: ")
          os.system("clear")
          sys.exit()
          

# === CONTROLLER ===
if __name__ == "__main__":
    current = "main"
    while True:
        if current == "main":
            current = main()
        elif current == "link":
            current = link()
