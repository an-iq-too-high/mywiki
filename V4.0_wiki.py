import wikipediaapi, os, time, sys, json, urllib.request, platform, subprocess, zipfile, shutil, socket
try: import psutil
except: psutil = None
G, B, C, Y, R, X, W = "\033[92m", "\033[94m", "\033[96m", "\033[93m", "\033[91m", "\033[0m", "\033[1m"
def anim(msg):
 os.system('clear')
 for i in range(5):
  sys.stdout.write(f"\r{Y}{W}📡 ENGINE: {msg.upper()}... [{C}{'#'*i}{'.'*(4-i)}{Y}]")
  sys.stdout.flush(); time.sleep(0.05)
sys_os = "Android" if (platform.system() == "Linux" and "ANDROID_ROOT" in os.environ) else platform.system()
sys_arch = platform.machine() or "[N/A]"
bat_status = "PC"
if sys_os == "Android":
 try: bat_status = f"{json.loads(subprocess.check_output(['termux-battery-status'], stderr=subprocess.DEVNULL).decode('utf-8'))['percentage']}%"
 except:
  if os.path.exists("/sys/class/power_supply"):
   for fold in os.listdir("/sys/class/power_supply"):
    p = os.path.join("/sys/class/power_supply", fold, "capacity")
    if os.path.exists(p):
     with open(p, "r") as f: bat_status = f"{f.read().strip()}%"
     break
elif psutil and psutil.sensors_battery():
 b = psutil.sensors_battery()
 if b: bat_status = f"{b.percent}%"
ram_status = "[N/A]"
if os.path.exists("/proc/meminfo"):
 with open("/proc/meminfo", "r") as f:
  for line in f:
   if "MemTotal" in line: ram_status = f"{round(int(line.split()[1]) / (1024**2), 1)} GB"; break
elif psutil: ram_status = f"{round(psutil.virtual_memory().total / (1024**3), 1)} GB"
def get_space():
 try: total, used, free = shutil.disk_usage("."); f_gb = f"{round(free / (1024**3), 1)} GB"
 except: f_gb = "[N/A]"
 v_b = sum(os.path.getsize(f) for f in os.listdir('.') if f.endswith('.md'))
 v_sz = f"{round(v_b/(1024**2),2)} MB" if v_b >= 1024**2 else (f"{round(v_b/1024,1)} KB" if v_b >= 1024 else f"{v_b} B")
 return f_gb, v_sz
anim("Checking Connection")
offline = False
try: urllib.request.urlopen("https://google.com", timeout=3)
except:
 print(f"\n{R}{W}⚠️ NETWORK FAILURE!{X}\n[1] Offline Mode\n[2] Exit")
 if input("\nChoice: ").strip() == '1': offline = True
 else: sys.exit()
if offline: G = B = C = Y = R = X = W = ""
wiki = wikipediaapi.Wikipedia(user_agent="MyBot/4.0", language="en")
def ask_ollama(sp, uc):
 try:
  req = urllib.request.Request("http://localhost:11434/api/chat", data=json.dumps({"model":"llama3.2:1b","messages":[{"role":"system","content":sp},{"role":"user","content":uc}],"stream":False}).encode('utf-8'), headers={'Content-Type':'application/json'})
  with urllib.request.urlopen(req, timeout=10) as r: return json.loads(r.read().decode('utf-8'))['message']['content'].strip()
 except: return None
while True:
 os.system('clear'); fr, vt = get_space()
 print(f"{C}{W}======================================\n    📚 MY PERSONAL WIKI APP V4.0 \n======================================{X}")
 print(f"{B}💻 OS: {sys_os}\n🏗️  Arch: {sys_arch}\n📊 RAM: {ram_status}\n🔋 Battery: {bat_status}\n💾 Free: {fr}\n📦 Vault: {vt}\n{C}======================================{X}")
 if not offline: print(f" [{C}1{X}] Search & Save New Article")
 else: print("[⚠️ SEARCH DISABLED - NO NETWORK]")
 print(f" [{C}2{X}] Open & Read Local Saved Files\n [{C}3{X}] Vault File Manager (Rename/Delete)")
 if not offline: print(f" [{C}4{X}] Chat with AI Over Saved Articles")
 else: print("[⚠️ AI DISABLED - NO NETWORK]")
 print(f" [{C}5{X}] View Global Search History\n [{C}6{X}] Clear History Logs\n [{C}7{X}] Backup Saved Articles (ZIP)\n [{C}8{X}] Exit System\n{C}======================================{X}")
 choice = input(f"\n{Y}{W}Select option [1-8]: {X}").strip()
 if choice.lower() == 'mp':
  while True:
   os.system('clear')
   print(f"{R}{W}======================================\n      🕵️‍♂️ SECRET NETWORK UTILITY       \n======================================{X}\nType 'back' to exit.")
   dom = input(f"\nEnter domain (e.g. google.com): ").strip()
   if dom.lower() == 'back': break
   if not dom: continue
   dom = dom.replace("https://","").replace("http://","").replace("www.","").split('/')[0]
   anim(f"Querying DNS for {dom}")
   try: print(f"\n{G}{W}➔ TARGET: {dom}{X}\n{Y}{W}➔ IPV4: {socket.gethostbyname(dom)}{X}\n")
   except: print(f"\n{R}❌ DNS Error: Could not resolve '{dom}'.{X}\n")
   input("Press Enter...")
 elif choice == '1' and not offline:
  topic = input(f"\nEnter search term: ").strip()
  if not topic: continue
  anim("Downloading Wikipedia content")
  p = wiki.page(topic)
  if not p.exists():
   print(f"{R}❌ Page not found.{X}"); input("Press Enter..."); continue
  with open(".wiki_history", "a", encoding="utf-8") as h: h.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {p.title}\n")
  anim("Computing AI Summary")
  summ = ask_ollama("Provide a concise, 3-sentence executive summary.", p.summary[:1500]) or "Ollama model offline."
  print(f"{G}{W}\nTitle: {p.title}{X}\n{Y}{W}🤖 AI SUMMARY:\n> {summ}{X}\nPreview: {p.summary[:200]}...")
  fn = p.title.replace(" ", "_") + ".md"
  with open(fn, "w", encoding="utf-8") as f: f.write(f"# {p.title}\n\n**🌐 URL:** {p.fullurl}\n\n## 🤖 AI SUMMARY\n> {summ}\n\n## 📖 CONTENT\n{p.text}\n")
  print(f"\n{G}💾 Saved -> {fn}{X}"); input("Press Enter...")
 elif choice == '2':
  files = [f for f in os.listdir('.') if f.endswith('.md')]
  if not files: print(f"{R}No markdown files found.{X}"); input("Press Enter..."); continue
  for idx, f in enumerate(files, 1): print(f"{G}[{idx}]{X} {f.replace('.md','')}")
  try:
   sel = int(input("\nEnter file number: "))
   if 1 <= sel <= len(files):
    os.system('clear')
    with open(files[sel-1], "r", encoding="utf-8") as f: print(f.read())
  except: print(f"{R}Invalid selection.{X}")
  input("Press Enter...")
 elif choice == '3':
  files = [f for f in os.listdir('.') if f.endswith('.md')]
  if not files: print(f"{R}No markdown files found.{X}"); input("Press Enter..."); continue
  for idx, f in enumerate(files, 1): print(f"{C}[{idx}]{X} {f}")
  try:
   sel = int(input("\nSelect file number: "))
   if 1 <= sel <= len(files):
    act = input("Choose action [1: Delete, 2: Rename]: ").strip()
    if act == '1': os.remove(files[sel-1]); print(f"{G}Deleted.{X}")
    elif act == '2':
     nn = input("New name (without .md): ").strip()
     if nn: os.rename(files[sel-1], nn.replace(" ","_")+".md"); print(f"{G}Renamed.{X}")
  except: print(f"{R}Error mapping action.{X}")
  input("Press Enter...")
 elif choice == '4' and not offline:
  files = [f for f in os.listdir('.') if f.endswith('.md')]
  if not files: print(f"{R}No files found.{X}"); input("Press Enter..."); continue
  for idx, f in enumerate(files, 1): print(f"{G}[{idx}]{X} {f.replace('.md','')}")
  try:
   sel = int(input("\nSelect file number: "))
   if 1 <= sel <= len(files):
    with open(files[sel-1], "r", encoding="utf-8") as f: ctx = f.read()
    while True:
     q = input(f"\n{C}Ask AI (or type 'back'): {X}").strip()
     if q.lower() == 'back': break
     if not q: continue
     anim("Generating AI response vectors")
     res = ask_ollama(f"Answer derived using this context snippet:\n\n{ctx[:5000]}", q)
     print(f"\n{Y}{W}🤖 AI ANSWER:\n{res or 'Ollama Server Offline.'}{X}\n")
  except: print(f"{R}Error executing interface.{X}")
  input("Press Enter...")
 elif choice == '5':
  if not os.path.exists(".wiki_history"): print(f"{R}No history records found.{X}")
  else:
   with open(".wiki_history", "r", encoding="utf-8") as h:
    for line in h.readlines()[-10:]: print(f"{C}[LOG]{X} {line.strip()}")
  input("Press Enter...")
 elif choice == '6':
  if os.path.exists(".wiki_history"): os.remove(".wiki_history"); print(f"{G}Logs wiped.{X}")
  else: print(f"{R}No logs found.{X}")
  input("Press Enter...")
 elif choice == '7':
  files = [f for f in os.listdir('.') if f.endswith('.md')]
  if not files: print(f"{R}No files to backup.{X}")
  else:
   zn = f"wiki_backup_{time.strftime('%Y%m%d_%H%M%S')}.zip"
   with zipfile.ZipFile(zn, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in files: z.write(f)
   print(f"{G}📦 Compiled -> {zn}{X}")
  input("Press Enter...")
 elif choice == '8': print(f"\n{R}Shutting down wiki matrix v4.0.{X}\n"); break
 else: print(f"{R}Invalid choice.{X}"); input("Press Enter...")
