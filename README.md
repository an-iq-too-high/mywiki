<p align="left">
  <img src="1789577930181.jpg" width="250" alt="MyWiki Logo">
</p>

![mywiki](https://img.shields.io/badge/github-mywiki-red?logo=github) ![version](https://img.shields.io/badge/Version-1.0-blue)


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

<img src="https://raw.githubusercontent.com/an-iq-too-high/mywiki/main/Screenshot_20260917-090741.jpg">
