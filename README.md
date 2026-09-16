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
UA = "MyPersonalWikiBot/1.0 (contact: your_email@example.com)"
wiki = wikipediaapi.Wikipedia(user_agent=UA, language="en")
while True:
 topic = input("\nEnter topic (or type 'exit'): ")
 if topic.lower() == 'exit': break
 page = wiki.page(topic)
 if not page.exists(): print("Page not found."); continue
 print("\nTitle: " + page.title + "\nURL: " + page.fullurl + "\n\nSummary:\n" + page.summary[:500] + "...")
 with open(page.title.replace(" ", "_") + ".txt", "w", encoding="utf-8") as f: f.write(page.text)
 print("Saved file successfully.")
EOF
```

Then you run it!

```
python mywiki.py
```
# PACKAGES REQUIRED

git

python

# HOW TO INSTALL PACKAGES

*P.S: this can work on termux*

```
pkg install git
```

Then you say:

```
pkg install python
```

If it tells you something like

```
Continue with installation? [y/n]
```
Then type "y"