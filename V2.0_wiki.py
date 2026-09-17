import wikipediaapi
import os
import time
import sys

UA = "MyPersonalWikiBot/2.0 (contact: your_email@example.com)"
wiki = wikipediaapi.Wikipedia(user_agent=UA, language="en")

GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def draw_banner():
 os.system('clear')
 print(f"{CYAN}{BOLD}======================================")
 print("      📚 MY PERSONAL WIKI APP 📚       ")
 print(f"======================================{RESET}")
 print(f"{GREEN} [1] {RESET}Search & Save New Article")
 print(f"{GREEN} [2] {RESET}List Local Downloaded Files")
 print(f"{GREEN} [3] {RESET}Delete a Downloaded File")
 print(f"{GREEN} [4] {RESET}Exit System")
 print(f"{CYAN}======================================{RESET}")

def play_loading_animation():
 os.system('clear')
 frames = ["|", "/", "-", "\\"]
 print(f"\n{YELLOW}{BOLD}📡 CONNECTING TO WIKIPEDIA CORE MATRIX...{RESET}\n")
 for i in range(16):
  frame = frames[i % len(frames)]
  progress = "#" * i
  spaces = " " * (15 - i)
  sys.stdout.write(f"\r{CYAN}[{frame}] LOADING: [{GREEN}{progress}{spaces}{CYAN}] {i*7}%")
  sys.stdout.flush()
  time.sleep(0.12)
 sys.stdout.write(f"\r{GREEN}[+] LOADING COMPLETE: [################] 100%\n\n{RESET}")
 sys.stdout.flush()
 time.sleep(0.4)

while True:
 draw_banner()
 choice = input(f"\n{YELLOW}{BOLD}Select an option [1-4]: {RESET}")
 
 if choice == '1':
  topic = input(f"\n{CYAN}Enter search term: {RESET}")
  if not topic.strip(): continue
  
  play_loading_animation()
  
  page = wiki.page(topic)
  if not page.exists():
   print(f"{RED}❌ Error: Topic page not found.{RESET}")
   input(f"\nPress Enter to return...")
   continue
  print(f"{GREEN}{BOLD}Title: {page.title}{RESET}")
  print(f"{BLUE}URL: {page.fullurl}{RESET}")
  print(f"\n{BOLD}Summary Preview:{RESET}\n{page.summary[:500]}...")
  filename = page.title.replace(" ", "_") + ".txt"
  with open(filename, "w", encoding="utf-8") as f: f.write(page.text)
  print(f"\n{GREEN}💾 Article text saved -> {filename}{RESET}")
  input(f"\nPress Enter to return to menu...")
  
 elif choice == '2':
  print(f"\n{CYAN}{BOLD}--- Local Vault Content ---{RESET}")
  files = [f for f in os.listdir('.') if f.endswith('.txt')]
  if not files: print(f"{RED}No offline files found yet.{RESET}")
  else:
   for idx, f_name in enumerate(files, 1): print(f"{GREEN}[{idx}]{RESET} {f_name.replace('_', ' ')}")
  input(f"\nPress Enter to return to menu...")
  
 elif choice == '3':
  print(f"\n{RED}{BOLD}--- Delete Local Vault Files ---{RESET}")
  files = [f for f in os.listdir('.') if f.endswith('.txt')]
  if not files:
   print(f"{RED}No files available to delete.{RESET}")
   input(f"\nPress Enter to return to menu...")
   continue
  for idx, f_name in enumerate(files, 1): print(f"{RED}[{idx}]{RESET} {f_name.replace('_', ' ')}")
  try:
   del_choice = int(input(f"\n{YELLOW}Enter number to delete (or 0 to cancel): {RESET}"))
   if del_choice == 0: continue
   if 1 <= del_choice <= len(files):
    target_file = files[del_choice - 1]
    os.remove(target_file)
    print(f"\n{GREEN}🔥 Successfully deleted: {target_file.replace('_', ' ')}{RESET}")
   else: print(f"{RED}Invalid file number selected.{RESET}")
  except ValueError: print(f"{RED}Please enter a valid number.{RESET}")
  input(f"\nPress Enter to return to menu...")
  
 elif choice == '4':
  print(f"\n{RED}Shutting down wiki matrix.{RESET}\n")
  break
 else:
  print(f"{RED}Invalid assignment choice.{RESET}")
  input(f"\nPress Enter to retry...")
