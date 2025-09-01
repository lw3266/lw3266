import requests, datetime

username = "lw3266"
repos = requests.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5").json()

with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# Hi, I'm {username}\n\n")
    f.write("## Latest Projects\n")
    for r in repos:
        f.write(f"- [{r['name']}]({r['html_url']}) — {r['description']}\n")
    f.write(f"\n_Last updated: {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}_\n")
