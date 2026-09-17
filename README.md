<p align="left">
  <img src="Logo.jpg" width="250" alt="MyWiki Logo">
</p>

![version](https://img.shields.io/badge/Version-1.0-blue?logo=1panel) ![python](https://img.shields.io/badge/Python_compatible-yellow?logo=python) ![termux](https://img.shields.io/badge/Android_compatible-green?logo=android)
![linux](https://img.shields.io/badge/Linux_compatible-black?logo=linux)
![awesome](https://awesome.re/badge.svg)
![git](https://img.shields.io/badge/Uses-Git-red?logo=git)
![terminal](https://img.shields.io/badge/Only_Works_On->terminals-black?logo=gnometerminal)
<a href="https://github.com/an-iq-too-high"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/badge/GitHub-%40an--iq--too--high-181717.svg?logo=github&amp;variant=branded&amp;size=sm&amp;mode=dark"><img alt="GitHub" src="https://www.shieldcn.dev/badge/GitHub-%40an--iq--too--high-181717.svg?logo=github&amp;variant=branded&amp;size=sm&amp;mode=light"></picture>

*Note: this can work on termux*

# HOW TO RUN

Firstly you'll have to git clone this repository

```
git clone https://github.com/an-iq-too-high/mywiki
```

Then say

```
cd mywiki
```

**BUT DON'T RUN THE .JS YET!!!** 
You'll then have to say this

```
cat << 'EOF' > wiki.py
import wikipediaapi
import os

UA = "MyPersonalWikiBot/1.0 (contact: your_email@example.com)"
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
 print(f"{GREEN}[1]{RESET} Search & Save New Article")
 print(f"{GREEN}[2]{RESET} List Local Downloaded Files")
 print(f"{GREEN}[3]{RESET} Delete a Downloaded File")
 print(f"{GREEN}[4]{RESET} Exit System")
 print(f"{CYAN}======================================{RESET}")

while True:
 draw_banner()
 choice = input(f"\n{YELLOW}{BOLD}Select an option [1-4]: {RESET}")
 
 if choice == '1':
  topic = input(f"\n{CYAN}Enter search term: {RESET}")
  if not topic.strip(): continue
  print(f"\n{YELLOW}🔍 Querying Wikipedia API...{RESET}")
  page = wiki.page(topic)
  if not page.exists():
   print(f"{RED}❌ Error: Topic page not found.{RESET}")
   input(f"\nPress Enter to return...")
   continue
  print(f"\n{GREEN}{BOLD}Title: {page.title}{RESET}")
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
EOF

```

Then you run it!

```
python wiki.py
```
# PACKAGES REQUIRED

git

python

wikipedia-api

# HOW TO INSTALL PACKAGES

*P.S: this can work on termux*

```
pkg install git
```

Then you say:

```
pkg install python
```
And THEN

```
pip install wikipedia-api
```


If it tells you something like

```
Continue with installation? [y/n]
```
Then type "y"


# IF YOU DID IT AND WANT TO DO IT AGAIN

You just say this:

```
cd mywiki
```
Then this:

```
python wiki.py
```
And that's it

# NOTES

If you ask the thing about anything, it will install a .txt file inside the folder for offline reading!
After you install the repository, you can delete files other than wiki.py! wiki.py will look empty but it kinda keeps the entire thing working, if you encounter any issues, please do say in the "issues" place! this code can work on python if you send the file AFTER doing the process!

# CREDITS

just me.

# SCREENSHOT

<img src="https://raw.githubusercontent.com/an-iq-too-high/mywiki/main/Proof.jpg">
