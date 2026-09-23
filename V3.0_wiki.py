import wikipediaapi
import os
import time
import sys
import json
import urllib.request

GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

os.system('clear')
print(f"{YELLOW}{BOLD}📡 SYSTEM DIAGNOSTICS: Checking Internet Connection...{RESET}")

try:
 urllib.request.urlopen("https://google.com", timeout=4)
 print(f"{GREEN}✔ Internet Connection Found! Booting matrix dashboard...{RESET}")
 time.sleep(1)
except Exception:
 print(f"\n{RED}{BOLD}==============================================")
 print(" ⚠️  CRITICAL WARNING: NETWORK FAILURE")
 print("==============================================")
 print(" No Internet Connection Found!")
 print(" Please Check Your Device Settings or Wi-Fi.")
 print(" Please Try Again Later.")
 print(f"=============================================={RESET}")
 input(f"\n{YELLOW}Press enter to shut down...{RESET}")
 sys.exit()

UA = "MyPersonalWikiBot/3.0 (contact: your_email@example.com)"
wiki = wikipediaapi.Wikipedia(user_agent=UA, language="en")
AI_MODEL = "llama3.2:1b"
OLLAMA_URL = "http://localhost:11434/api/chat"

def draw_banner():
 os.system('clear')
 print(f"{CYAN}{BOLD}======================================")
 print(f"    📚 MY PERSONAL WIKI APP V3.0 [AI] ")
 print(f"======================================{RESET}")
 print(f"{CYAN} Search & Save New Article")
 print(f"{CYAN} Open & Read Local Saved Files")
 print(f"{CYAN} Vault File Manager (Rename/Delete)")
 print(f"{CYAN} Chat with AI Over Saved Articles")
 print(f"{CYAN} Exit System")
 print(f"{CYAN}======================================{RESET}")

def play_loading_animation(task_message):
 os.system('clear')
 frames = ["|", "/", "-", "\\"]
 print(f"\n{YELLOW}{BOLD}📡 ENGINE STATUS: {task_message.upper()}...{RESET}\n")
 for i in range(12):
  frame = frames[i % len(frames)]
  progress = "#" * i
  spaces = " " * (11 - i)
  sys.stdout.write(f"\r{CYAN}[{frame}] PROCESSING: [{GREEN}{progress}{spaces}{CYAN}] {int(i*8.5)}%")
  sys.stdout.flush()
  time.sleep(0.015)
 sys.stdout.write(f"\r{GREEN}[+] TASK COMPLETE: [############] 100%\n\n{RESET}")
 sys.stdout.flush()
 time.sleep(0.05)

def ask_ollama(system_prompt, user_content):
 data = {"model": AI_MODEL, "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_content}], "stream": False}
 req = urllib.request.Request(OLLAMA_URL, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
 try:
  with urllib.request.urlopen(req, timeout=10) as response:
   return json.loads(response.read().decode('utf-8'))['message']['content'].strip()
 except Exception: return None

while True:
 draw_banner()
 choice = input(f"\n{YELLOW}{BOLD}Select an option [1-5]: {RESET}").strip()
 
 if choice == '1':
  topic = input(f"\n{CYAN}Enter search term: {RESET}").strip()
  if not topic: continue
  play_loading_animation("Connecting to Wikipedia server")
  play_loading_animation(f"Downloading main text payload for '{topic}'")
  page = wiki.page(topic)
  if not page.exists():
   print(f"{RED}❌ Direct page not found. Fetching smart suggestions...{RESET}")
   print(f"\n{YELLOW}[?] Did you mean one of these?{RESET}")
   fallback_topics = [topic + " (programming language)", topic + " (disambiguation)", "Back to Main Menu"]
   for idx, alt in enumerate(fallback_topics, 1): print(f" {CYAN}[{idx}]{RESET} {alt}")
   try:
    s_choice = input(f"\n{YELLOW}Select an alternative number: {RESET}").strip()
    if s_choice in ['1', '2']:
     topic = fallback_topics[int(s_choice) - 1]
     play_loading_animation(f"Re-routing pipeline data for '{topic}'")
     page = wiki.page(topic)
     if not page.exists():
      print(f"{RED}❌ Suggestion page could not be pulled.{RESET}")
      input(f"\nPress Enter to return...")
      continue
    else: continue
   except Exception: continue
  play_loading_animation("Waking up local Ollama neural context layer")
  play_loading_animation("AI reading article and computing smart summary execution")
  ai_summary = ask_ollama("Provide a concise, intelligent, 3-sentence executive summary of the provided text layout.", page.summary[:2000])
  if not ai_summary: ai_summary = "Ollama model offline or background server not running. (To turn on AI, open a new Termux tab and run 'ollama run llama3.2:1b')."
  print(f"{GREEN}{BOLD}Title: {page.title}{RESET}\n{BLUE}URL: {page.fullurl}{RESET}")
  print(f"\n{YELLOW}{BOLD}🤖 OLLAMA AI SUMMARY REVIEW:{RESET}\n{ai_summary}")
  print(f"\n{BOLD}Wikipedia Summary Preview:{RESET}\n{page.summary[:300]}...")
  filename = page.title.replace(" ", "_") + ".txt"
  play_loading_animation(f"Writing raw document files data onto disk storage -> {filename}")
  with open(filename, "w", encoding="utf-8") as f: f.write(f"Title: {page.title}\nURL: {page.fullurl}\n\n{page.text}")
  print(f"\n{GREEN}💾 Article text saved -> {filename}{RESET}")
  input(f"\nPress Enter to return to menu...")
 elif choice == '2':
  print(f"\n{CYAN}{BOLD}--- Local Vault Files ---{RESET}")
  files = [f for f in os.listdir('.') if f.endswith('.txt') and not f.startswith('.')]
  if not files: print(f"{RED}No offline files found yet.{RESET}"); input(f"\nPress Enter to return..."); continue
  for idx, f_name in enumerate(files, 1): print(f"{GREEN}[{idx}]{RESET} {f_name.replace('_', ' ').replace('.txt', '')}")
  try:
   read_choice = int(input(f"\n{YELLOW}Enter file number to read (or 0 to cancel): {RESET}"))
   if read_choice == 0: continue
   if 1 <= read_choice <= len(files):
    target_file = files[read_choice - 1]
    play_loading_animation(f"Opening secure file stream read layout for {target_file}")
    with open(target_file, "r", encoding="utf-8") as f: file_content = f.read()
    print(f"{CYAN}{BOLD}======================================\n📖 READING: {target_file.replace('_', ' ').replace('.txt', '')}\n======================================{RESET}\n{file_content}\n{CYAN}{BOLD}======================================{RESET}")
   else: print(f"{RED}Invalid position.{RESET}")
  except ValueError: print(f"{RED}Please enter numbers only.{RESET}")
  input(f"\nPress Enter to return to menu...")
 elif choice == '3':
  print(f"\n{CYAN}{BOLD}--- Vault File Manager ---{RESET}")
  files = [f for f in os.listdir('.') if f.endswith('.txt') and not f.startswith('.')]
  if not files: print(f"{RED}No files available to manage.{RESET}"); input(f"\nPress Enter to return menu..."); continue
  for idx, f_name in enumerate(files, 1): print(f"{CYAN}[{idx}]{RESET} {f_name.replace('_', ' ')}")
  try:
   manage_choice = int(input(f"\n{YELLOW}Select file number to manage (or 0 to cancel): {RESET}"))
   if manage_choice == 0: continue
   if 1 <= manage_choice <= len(files):
    target_file = files[manage_choice - 1]
    print(f"\nTarget Selected: {target_file.replace('_', ' ')}\n {RED}{RESET} Delete File\n {YELLOW}{RESET} Rename File")
    action = input(f"\n{YELLOW}Choose an action [1-2]: {RESET}").strip()
    if action == '1':
     play_loading_animation(f"Purging targeted resource block index -> {target_file}")
     os.remove(target_file)
     print(f"\n{GREEN}🔥 Successfully deleted: {target_file.replace('_', ' ')}{RESET}")
    elif action == '2':
     new_name = input(f"\n{CYAN}Enter new filename (without .txt): {RESET}").strip()
     if new_name:
      new_file_name = new_name.replace(" ", "_") + ".txt"
      play_loading_animation(f"Re-indexing local descriptors to: {new_file_name}")
      os.rename(target_file, new_file_name)
      print(f"\n{GREEN}✏️ Successfully renamed to: {new_file_name.replace('_', ' ')}{RESET}")
     else: print(f"{RED}Rename cancelled. Empty name provided.{RESET}")
    else: print(f"{RED}Invalid action chosen.{RESET}")
   else: print(f"{RED}Invalid file number selected.{RESET}")
  except ValueError: print(f"{RED}Please enter a valid number.{RESET}")
  input(f"\nPress Enter to return to menu...")
 elif choice == '4':
  os.system('clear')
  print(f"\n{CYAN}{BOLD}--- AI Vault Knowledge Chat Interface ---{RESET}")
  files = [f for f in os.listdir('.') if f.endswith('.txt') and not f.startswith('.')]
  if not files: print(f"{RED}Error: Requires saved text articles in your vault folder.{RESET}"); input(f"\nPress Enter to return..."); continue
  for idx, f_name in enumerate(files, 1): print(f"{GREEN}[{idx}]{RESET} {f_name.replace('_', ' ').replace('.txt', '')}")
  try:
   chat_choice = int(input(f"\n{YELLOW}Select article text workspace matrix to chat with: {RESET}"))
   if 1 <= chat_choice <= len(files):
    target_file = files[chat_choice - 1]
    with open(target_file, "r", encoding="utf-8") as f: context_data = f.read()
    os.system('clear')
    print(f"{GREEN}{BOLD}======================================\n🤖 AI CONTEXT STREAM LOADED: {target_file.replace('.txt','')}\n Type 'back' anytime to return to main menu.\n======================================{RESET}\n")
    while True:
     user_query = input(f"{CYAN}{BOLD}Ask AI Question ➔ {RESET}").strip()
     if user_query.lower() == 'back': break
     if not user_query: continue
     play_loading_animation("Injecting local text context strings into AI model prompt processing window")
     play_loading_animation("Generating advanced structural response analysis vectors")
     ai_response = ask_ollama(f"Answer queries solely derived using this reference text context dataset:\n\n{context_data}", user_query)
     os.system('clear')
     print(f"{GREEN}{BOLD}======================================\n🤖 AI CONTEXT STREAM LOADED: {target_file.replace('.txt','')}\n======================================{RESET}")
     if ai_response: print(f"\n{YELLOW}{BOLD}🤖 AI ANSWER INPUT RESPONSE:{RESET}\n{ai_response}\n")
     else: print(f"{RED}Ollama background server offline. (Run 'ollama run llama3.2:1b' in another tab).{RESET}\n")
   else: print(f"{RED}Invalid assignment position.{RESET}")
  except ValueError: print(f"{RED}Invalid selection type numerical input constraints only.{RESET}")
  input(f"\nPress Enter to return to menu...")
 elif choice == '5':
  print(f"\n{RED}Shutting down wiki matrix v3.0 [AI Edition].{RESET}\n")
  break
 else: print(f"{RED}Invalid choice.{RESET}"); input(f"\nPress Enter to retry...")
