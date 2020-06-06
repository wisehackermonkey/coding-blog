# This code updates the README.md to reflect 
# changes to my other repos automatically so i dont have to edit this readme by hand
# for every new repo i create
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200605
import requests
import json
from markdown import markdown
from dateutil.parser import *

github_username = "wisehackermonkey"  # thats me! wooh!

# returns date in YYYYMMDD format
def formated_date(d):
    d = parse(d)
    day = str(d.day).rjust(2,"0")
    month = str(d.month).rjust(2,"0")
    year = d.year 

    return "{}{}{}".format(year,month,day)


if __name__ == "__main__":
    results = requests.get(f"https://api.github.com/users/{github_username}/repos?per_page=100")

    json_results = json.loads(results.text)
    html_data = markdown(open("./header.md").read())
    for repo in json_results[0:-1]:
        if repo["has_pages"] == True:
            repo_name =         repo["name"]
            repo_url =          repo["html_url"]
            repo_description =  repo["description"]
            repo_date =         repo["created_at"]
            repo_short_name = repo["full_name"]

            # convert repo date to YYYYMMDD
            repo_date = formated_date(repo_date)
            
            post_text = f"""
# [{repo_name}](https://{github_username}.github.io/{repo_name})
##### {repo_description}
##### [{repo_short_name}]({repo_url})
```
{repo_date}
```
---------------
    """
            html_data += markdown(post_text)
    with open("./index.html","w") as f:
        f.write(html_data)
