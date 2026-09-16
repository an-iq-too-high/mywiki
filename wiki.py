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
